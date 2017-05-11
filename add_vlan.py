#!/usr/bin/python

#imports
import requests
import json
import cred

#custom variables for the program imported from the cred.py file located in the same directory
organization = cred.organization
key = cred.key
hub = cred.hub


#Main URL for the Meraki Platform
dashboard = "https://dashboard.meraki.com"
#api token and other data that needs to be uploaded in the header
headers = {'X-Cisco-Meraki-API-Key': (key), 'Content-Type': 'application/json'}

#variables for testing ***** Need to switch to an argument or something else
store = input("What store needs a new vlan? The store must already exist in Meraki Console: ")
VLANLAN = input("Vlan Subnet: ")
VLANGW = input("Gateway: ")
VLANNAME = input("Name of the VLAN: ")
VLANID = input("Vlan #: ")


#pull back all of the networks for the organization
get_network_url = dashboard + '/api/v0/organizations/%s/networks' % organization

#request the network data
get_network_response = requests.get(get_network_url, headers=headers)

#puts the data into json format
get_network_json = get_network_response.json()

#pull back the network_id of the store that you are configuring
for i in get_network_json:
    if i["name"] == str(store):
        network_id=(i["id"])

#Vlan to add

#Buil the JSON for the VLAN we are adding to the appliance
VLANADD = {}
VLANADD["id"] = VLANID
VLANADD["name"] = VLANNAME
VLANADD["applianceIp"] = VLANGW
VLANADD["subnet"] = VLANLAN + "/28"

#Create the URL
get_network_vlan2jsonurl = dashboard + '/networks/%s/vlans' % network_id

#perform the update
get_network_vlan2json = requests.post(get_network_vlan2jsonurl, data=json.dumps(VLANADD), headers=headers)
