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
# python script (OTX_recent_pulses.py) shows the basics of accessing  
# recently updated pulses via API.
# ---------------------------------------------------------------------------
# PREREQUISITES
# To use the OTX Direct Connect service you will need to establish an account
# at otx.alienvault.com.  Your account will have a unique "OTX Key" for API
# access (see your OTX profile).  You will also need to install 
# OTX-Python-SDK into your python environment.
# ---------------------------------------------------------------------------
# Imports - OTXv2 is the main module in the OTX-Python-SDK
from OTXv2 import OTXv2
import datetime
# ---------------------------------------------------------------------------


# instantiate the otx opject with your OTX Key
otx = OTXv2("insert your OTX Key here")

# Choose how many DAYS back you wish the query to go
days_back = 5
# Generate an ISO fromated date for 'days_back' days ago
recent_date = datetime.datetime.now() - datetime.timedelta(days_back)

# Query the OTX API for a list of pulses that have been recently updated
pulses = otx.getsince(recent_date.isoformat())

# Print a summary for each of the pulses returned from the OTX service
print("\n\r\n\r")
print("Open Threat Exchange Pulses modified in the last " + str(days_back) + " days:\n\r")
print("-------------------------+----------------------------+-------------------")

print("        Pulse ID         |       Last Modified        |    Pulse Name  ")
print("-------------------------+----------------------------+-------------------")

i = 0
if len(pulses) > 0: #only print if the query returned at least one pulse
    while i < (len(pulses)):
        print(pulses[i]["id"] + " | " + pulses[i]["modified"] + " | " + pulses[i]["name"] + "\n\r")
        i += 1

print("\n\r\n\r -----     run completed     -----\n\r\n\r")


#----------------------------------------------------------------------------
# end of file
#----------------------------------------------------------------------------



