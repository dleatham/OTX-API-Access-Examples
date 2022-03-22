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
# python script (OTX_pulse_iocs.py) shows the basics of extracting the
# specific "incidences of concern" associated with a threat pulse.
# ---------------------------------------------------------------------------
# PREREQUISITES
# To use the OTX Direct Connect service you will need to establish an account
# at otx.alienvault.com.  Your account will have a unique "OTX Key" for API
# access (see your OTX profile).  You will also need to install 
# OTX-Python-SDK into your python environment.
# ---------------------------------------------------------------------------
# Imports - OTXv2 is the main module in the OTX-Python-SDK
from OTXv2 import OTXv2, IndicatorTypes
# ---------------------------------------------------------------------------


# instantiate the otx opject with your OTX Key
otx = OTXv2("insert your OTX Key here")

# Use an OTX pluse ID to get all the IOCs associated with that specific pulse
a_pulse_id = "606d75c11c08ff94089a9430"
pulse = otx.get_pulse_details(a_pulse_id)

# Retrieve all the IOCs associated with the pulse
indicators = otx.get_pulse_indicators( a_pulse_id )


# Print a summary for each of the IOCs returned from the OTX service
print("\n\r\n\r")
print("Open Threat Exchange has the following Pulse and associated IOCs:")
print("Pulse Name:" + pulse["name"])
print("---------------+------+-------------------")
print("    IOC ID     | Type |    IOC Title  ")
print("---------------+------+-------------------")

num_of_IOCs_to_print = 5

if len(indicators) > 0: #only print if the query returned at least one IOC
    for indicator in indicators[:num_of_IOCs_to_print]:
        print(indicator["indicator"] + " | " + indicator["type"] + " | " + indicator["title"] + "\r\n")

print("\n\r\n\r -----     run completed     -----\n\r\n\r")


#----------------------------------------------------------------------------
# end of file
#----------------------------------------------------------------------------









# for indicator in indicators[:3]:
#    print(indicator["indicator"] + "\r\n" + indicator["type"] + "\r\n" + indicator["title"] + "\r\n")




