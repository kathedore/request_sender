import requests

headers = {'X-Cisco-Meraki-API-Key': '891ef09d8119700d9a9b3dd2982252241f2eb962',
    'content-type': 'application/json'}

url = 'https://api.meraki.com/api/v0/organizations/942504/networks/L_706502191543765788/devices/Q2KD-7PL3-MNNR/performance'

def requst_filter():
     res = requests.get(url, headers=headers)
     return res.text

# Only primary MX devices supported. so yvelaferze ar imushavebs
#print(requst_filter())