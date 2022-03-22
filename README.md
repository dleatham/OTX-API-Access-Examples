
# OTX API Access Examples

This project is designed to be a simple quick-start guide to accessing community threat data via the **AlienVault “Open Threat Exchange” (OTX) DirectConnect API**.  The project also leverages the **OTX-Python-SDK** which provides python methods to access many of the key OTX DirectConnect API.  The project’s goal is to simplify and accelerate developers’ access to the OTX community threat data and aid them in evaluating the data for use in security projects and processes.  

The project has the following scripts:

- **OTX_search_pulses.py** – This script demonstrates searching the OTX pulses for a specific text string using the “otx.search_pulses()” method

- **OTX_recent_pulses.py** – This script shows how to search for threat pulses that have been updated/active in the past X days using the “otx.getsince()” method

- **OTX_pulse_iocs.py** – This script shows how to extract incidents of concern (IOC) from a specific threat pulse using the “otx.get_pulse_details()” method

Together these three scripts enable a security developer to find recent or specific pules and extract IOCs from these pulses for use in various security efforts.


## Documentation

The scripts in this project have the following prerequisites and dependencies:

**OTX User Account** – To access the OTX threat data via API an “OTX Key” is required.  This key is provided with a free user account that can be created at: https://otx.alienvault.com

**OTX-Python-SDK** – Each script must include the OTX-Python-SDK module which is available at: https://github.com/AlienVault-OTX/OTX-Python-SDK 


To execute these scripts, complete the following steps:

- Install the OTX-Python-SDK with the following command: ```pip install OTXv2```
- Download the script files to a local directory
- In each of the scripts replace the text string “insert your OTX Key here” with your OTX Key (as at text string in quotes)
  
The scripts can then be executed from the CLI using the python command.  Each script prints a few pulse/IOC information fields to the console.  


Additional information about the **OTX DirectAccess API** is available under the "Docs" tab at: https://otx.alienvault.com/api

Detailed information about the **OTX-Python-SDK** is available in that project's documentation.


## Author

- [@dleatham](https://github.com/dleatham)

