[![published](https://pubhub.devnetcloud.com/media/pyats-genie-docs/docs/imgs/pyats.png#developer.cisco.com)

# pyATS DevNet Automation Exchange Submissions

This repository contains all pyATS DevNet Automation Exchange submission.

## General Information

- pyATS/Genie Portal: https://cs.co/pyats
- Documentation Central: https://developer.cisco.com/docs/pyats/
  - Getting Started: https://developer.cisco.com/docs/pyats-getting-started/
  - API Browser: https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/
- Support Email: pyats-support-ext@cisco.com

## Repository content

* [ShutAllInterface](https://github.com/CiscoTestAutomation/DevNetAutomationExchange/tree/main/ShutAllInterface): Shut all interfaces on specific devices

## Requirements

- Mac OSX, Linux or Windows 10 [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
- Python 3.6, 3.7 or 3.8
- Network connectivity (for downloading PyPI packages)

## Preparation Instructions

**Step 1: Create a Python Virtual Environment**

In a new terminal window:

```bash
# go to your workspace directory
# (or where you typical work from)
cd ~/workspace

# create python virtual environment
python3 -m venv pyats

# activate virtual environment
cd pyats
source bin/activate

# update your pip/setuptools
pip install --upgrade pip setuptools
```

**Step 2: Install pyATS & Genie**

```bash
# install our packages 
pip install pyats[full]
```

> Note:
>
> The install target `pyATS[full]` performs a *full* installation, that is, 
> including the core framework pyATS, the standard libraries Genie, and 
> additional components such as RobotFramework support etc.

**Step 3: Clone This Repository**

```bash
# clone this repo
git clone git@github.com:CiscoTestAutomation/DevNetAutomationExchange.git

# cd to the directory
cd DevNetAutomationExchange
```

and now you should be ready to get going!


