#----------------------------------------------------------------------------
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Don Leatham
# Created Date: 2022/March/20
# version ='1.0'
# ---------------------------------------------------------------------------
# DESCRIPTION
# This script is one of a collection describing basic API access to the Alien
# Vault Open Threat Exchange (OTX) leveraging the OTX-Python-SDK:
#     https://github.com/AlienVault-OTX/OTX-Python-SDK
# OTX organizes threat information around the concept of "pulses", and this
# python script (OTX_search_pulses.py) shows the basics of searching OTX, via
# API, for pulses that contain a specific string.
# ---------------------------------------------------------------------------
# PREREQUISITES
# To use the OTX Direct Connect service you will need to establish an account
# at otx.alienvault.com.  Your account will have a unique "OTX Key" for API
# access (see your OTX profile).  You will also need to install 
# OTX-Python-SDK into your python environment.
# ---------------------------------------------------------------------------
# Imports - OTXv2 is the main module in the OTX-Python-SDK
from OTXv2 import OTXv2
# ---------------------------------------------------------------------------


# instantiate the otx opject with your OTX Key
otx = OTXv2("insert your OTX Key here")

# Choose a text string to search for in the OTX system and cal the search api
query_str = "taliban"
found_pulses = otx.search_pulses(query_str)

# The search result is formatted as JSON, and the results field contains
# the lsit of pulses found in the search
pulses = found_pulses.get("results")

# Print a summary for each of the pulses returned from the OTX service
print("\n\r\n\r")
print("Open Threat Exchange Pulses containing: " + query_str +  "\n\r")
print("-------------------------+----------------------------+-------------------")
print("        Pulse ID         |       Creation Date        |    Pulse Name  ")
print("-------------------------+----------------------------+-------------------")


i = 0
if len(pulses) > 0: #only print if the query returned at least one pulse
    while i < (len(pulses)):
        print(pulses[i]["id"] + " | " + pulses[i]["created"] + " | " + pulses[i]["name"] + "\n\r")
        i += 1

print("\n\r\n\r -----     run completed     -----\n\r\n\r")



#----------------------------------------------------------------------------
# end of file
#----------------------------------------------------------------------------

