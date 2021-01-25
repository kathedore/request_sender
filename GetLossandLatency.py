import requests

headers = {'X-Cisco-Meraki-API-Key': '891ef09d8119700d9a9b3dd2982252241f2eb962',
    'content-type': 'application/json'}

url = 'https://api.meraki.com/api/v0/organizations/942504//networks/L_706502191543765788/devices/Q2KD-7PL3-MNNR/lossAndLatencyHistory'

parameter1 = '?timespan=25090'
parameter2 = '?t0=1.12&t1=4.12'
parameter3 = '?uplink='
parameter4 = '&ip=192.168.50.114'
#fourth is the destination ip da chems ro vutiteb ....
def requst_filter():
     res = requests.get(url+parameter1+parameter4, headers=headers)
     return res.text

#print(requst_filter())
