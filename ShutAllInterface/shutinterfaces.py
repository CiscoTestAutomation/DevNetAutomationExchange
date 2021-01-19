# Shut all the interfaces
# return the list of interfaces that were shut
import argparse
from genie.testbed import load

def generate_shut_config(device, exclude):
    # Device -> device object
    # exclude -> [int1, int2]

    # Get the list of interfaces up
    interface_to_shut = interfaces_up(device)

    # For each of them, generate the configuration to shut them down, and unshut them
    configuration = []
    unconfiguration = []
    for interface in interface_to_shut:
        if interface in exclude:
            continue
        configuration.append('interface {intf}\nshut'.format(intf=interface))
        unconfiguration.append('interface {intf}\nno shut'.format(intf=interface))
    return device, configuration, unconfiguration

def get_excluded_interfaces(exclude):
    # If no exclude interface has been provided, then return empty dict
    excludes = {}
    if not exclude:
        return excludes

    # Convert device:int1,int2 device2:int1,int5
    # Into {device:[int1, int2],
    #       device2:[int1, int5]}
    for group in exclude:
        # ['device:int1,int2', 'device2:int1,int5']
        splitd = group.split(':')
        # splitd = [device, int1,int2]
        excludes[splitd[0]] = splitd[1].split(',')
    return excludes

def interfaces_up(device):
    if device.os == 'iosxe':
        output = device.parse('show interfaces')
    else:
        output = device.parse('show interface')

    return output.q.contains_key_value('oper_status', 'up').get_values('[0]')


if __name__ == '__main__':

    # Get the testbed argument
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--testbed-file',
                        type=str,
                        help='Testbed file')
    parser.add_argument('--devices',
                        nargs='*',
                        type=str,
                        help='devices to shut all interface')
    parser.add_argument('--exclude',
                        nargs='*',
                        type=str,
                        default=None,
                        help='Interface to exclude to shut\nformat: device:int1,int2 device2:int1,int5')
    args = parser.parse_known_args()[0]

    # Load the testbed object
    tb = load(args.testbed_file)

    # Convert the string provided into a dictionary
    excludes = get_excluded_interfaces(args.exclude)

    # Shut for each devices provides
    to_shut = []
    for device in args.devices:
        try:
            dev_obj = tb.devices[device]
        except KeyError as e:
            raise KeyError("'{d}' does not exists in the testbed file "
                           "'{tb} - Terminating"
                           "'\n{e}".format(d=device,
                                           tb=args.testbed_file,
                                           e=e))

        # Connect
        try:
            dev_obj.connect()
        except Exception as e:
            raise Exception("Could not connect to '{d}' - "
                            "Terminating\n{e}".format(d=device, e=e))

        # Collecting configuration. We are not shutting right away -
        # we want to have a clean log - where we can see all the configuration
        # being applied and not being hidden by the show commands
        to_shut.append(generate_shut_config(dev_obj, excludes.get(device, [])))

    for configuration in to_shut:
        device, config, unconfiguration = configuration
        print("Shutting down interfaces of device '{d}'".format(d=device.name))
        device.configure(config)

    for configuration in to_shut:
        device, config, unconfiguration = configuration
        print("Unshut configuration for device '{d}' "
              "is:\n{c}".format(d=device.name, c='\n'.join(unconfiguration)))
