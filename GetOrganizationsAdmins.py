import requests

headers = {'X-Cisco-Meraki-API-Key': '891ef09d8119700d9a9b3dd2982252241f2eb962',
    'content-type': 'application/json'}

url= 'https://api.meraki.com/api/v1/organizations/942504/admins'

def requst_filter():
     res = requests.get(url, headers=headers)
     #print('kuku_requestfilter' + res.text)
     return res.text

#print(requst_filter())