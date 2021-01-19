# ShutAllInterfaces

Shut all the interfaces of a provided device

![Theme](https://github.com/CiscoTestAutomation/DevNetAutomationExchange/blob/main/ShutAllInterface/ShutAllInterface.svg)
 
## Use Case Description

> How can I shut all the interfaces on a specific device.

At Cisco Live, an attendee asked me this very question. He had to shut multiple devices, but wanted to make sure it would not affect his production network. Though, he did not want to waste his time shutting thousand of interfaces manually.

We sat together, and coded this small but very useful script. 

This script becomes very important when wanting to decomission a device. It allow to make sure the network is performing as expecting without this device being operational. However, it can be brought back in a few seconds if needed.

The "Un shut" configuration is provided at the end of the run, to quickly revert if needed.


Other ideas to enhance this script could be:

* Take operation snapshot of the surounding device, to make sure nothing important has been lost. This would automatically let the user know of what has changed.
* Connect to each device in parallel
* Do the shut for each device in parallel
* Use [device.api](https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/apis) to simplify the code and share re-usable libraries to pyATS.

## Installation


This script requires pyATS. Follow the instruction on the [previous page](../README.md).

Then you will need a Testbed file. Follow this [guide](https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/quickstart/manageconnections.html#) on how to create one.

A testbed file is a way to represent your devices. It contains the devices name, credentials and ip address on how to reach it. You can find a testbed example [here](testbed.yaml).

## Usage

To execute it, just do the following:

```bash
# Shut all interfaces of csr1000v-1
python shutinterfaces.py --testbed-file testbed.yaml  --devices csr1000v-1

# Shut all interfaces of csr1000v-1 and nx-osv-1
python shutinterfaces.py --testbed-file testbed.yaml  --devices csr1000v-1 nx-osv-1

# Shut all interfaces of csr1000v-1 Except Loopback0 and Loopback1
python shutinterfaces.py --testbed-file ../../training/genie-bootcamp/tb.yaml  --devices csr1000v-1 --exclude csr1000v-1:Loopback0,Loopback1
```

This script works on all Cisco main OS (XR, IOSXE, NXOS and IOS).

![Theme](https://github.com/CiscoTestAutomation/DevNetAutomationExchange/blob/main/ShutAllInterface/Theme.png)

## Arguments

There is 3 arguments to this scripts

```text
--testbed-file: pyATS Testbed file (Mandatory argument)
--devices: Space separed device name to shut interfaces on. Must exists in the testbed file (Mandatory argument)
--exclude: Interfaces to NOT shut. Example --exclude device_name1:int1 int2 int3 device_name2:int3 int5 (Optional argument)

```

## DevNet Sandbox

This Code Exchange will work on any DevNet sandbox - For example on the [CML Entreprise Lab](https://devnetsandbox.cisco.com/RM/Diagram/Index/45100600-b413-4471-b28e-b014eb824555?diagramType=Topology)

## Getting help

If you have questions, concerns, bug reports, etc., please create an issue against this repository.

## Author(s)

This project was written and is maintained by the following individuals:

* Jean-Benoit Aubin <jeaubin@cisco.com>
* pyats-support@cisco.com
