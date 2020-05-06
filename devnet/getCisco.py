#!/usr/bin/env python
import requests

HOST = 'ios-xe-mgmt.cisco.com'
USER = 'root'
PASS = 'D_Vay!_10&'

url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/ietf-interfaces:interfaces"

headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

response = requests.get(url, auth=(USER, PASS), headers=headers, verify=False)

interfaces = response.json()

iname = interfaces['ietf-interfaces:interfaces']['interface'][0]['name']
iaddr = interfaces['ietf-interfaces:interfaces']['interface'][0]['ietf-ip:ipv4']['address'][0]['ip']

print(iname, " ", iaddr)
