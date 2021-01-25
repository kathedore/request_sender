import GetOrganisations as go
import GetNetworksinOrg as gn
import GetDevicesinOrg as gd
import GetNetworkClients as gc
import GetDeviceSerials as gs
import DBconnection as db
import GetDeviceSerials as gu
import GetLldp_Cdp as lc
import GetLossandLatency as ll
import GetDevicePerfomrmance as gp
import GetDeviceClients as gdc
import GetNetworkClient as nc
import GetNetworkClientEvents as ge
import GetNetworkClientLatency as gcl
import GetNetworkClientPolicy as gcp
import GetNetworkClientSplashAuthorStatus as gsas
import GetNetworkClientTraffic as gct
import GetNetworkClientUsage as gcu
import GetOrganizationsAdmins as goa

from flask import Flask, render_template, request, url_for, jsonify
app = Flask(__name__)


@app.route('/organisations')
def getorganisations():
    url = go.url
    resp = go.requst_filter()
    request_type = "organisations"
    record_to_insert = (url, resp, request_type)
    #print('kukuroute' + resp)
    #print('kukuroute_url= '+url+'  resp= '+resp + 'kuku_request_type= '+ request_type)
    #print('kuku_request_type= '+ request_type)
    db.database(record_to_insert)
    #json2string(url, resp, request_type)
    return resp

@app.route('/networks')
def getnetworksinorg():
    url = gn.url
    resp = gn.requst_filter()
    #print('kukuroute' + resp)
    request_type = "networks"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/devices')
def getdevicesinorg():
    url = gd.url
    resp = gd.requst_filter()
    request_type = "devices"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/nclients')
def getneworkclinets():
    url = gc.url
    resp = gc.requst_filter()
    request_type = "network clients"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/ndevices')
def getdeviceserials():
    url = gs.url
    resp = gs.requst_filter()
    request_type = "device serials"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/uplink')
def getndeviceuplink():
    url = gu.url
    resp = gu.requst_filter()
    request_type = "device uplink"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/llcp_cdp')
def getlldp_cdp():
    url = lc.url
    resp = lc.requst_filter()
    request_type = "device llcp cdp"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/lossAndLatencyHistory')
def getlossAndLatencyHistory():
    url = ll.url
    resp = ll.requst_filter()
    request_type = "device llcp cdp"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/performance')
def getdevideperformance():
    url = gp.url
    resp = gp.requst_filter()
    request_type = "device performance"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/qualityAndRetentionSettings')
def getqualityAndRetentionSettings():
    url = gp.url
    resp = gp.requst_filter()
    request_type = "quality and retention settings"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/dclients')
def getdeviceclients():
    url = gdc.url
    resp = gdc.requst_filter()
    request_type = "device clients"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/nclient')
def getnetworkclient():
    url = nc.url
    resp = nc.requst_filter()
    request_type = "network client"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/events')
def getnetworkclientevents():
    url = ge.url
    resp = ge.requst_filter()
    request_type = "network client events"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/latencyHistory')
def getnetworkclientlatency():
    url = gcl.url
    resp = gcl.requst_filter()
    request_type = "network client latency history"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/policy')
def getnetworkclientpolicy():
    url = gcp.url
    resp = gcp.requst_filter()
    request_type = "network client policy"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/splashAuthorizationStatus')
def getnetworkclientsplashAuthorStatus():
    url = gsas.url
    resp = gsas.requst_filter()
    request_type = "network client splash authorization status"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/traffic')
def getnetworkclienttraffic():
    url = gct.url
    resp = gct.requst_filter()
    request_type = "network client traffic"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/usageHistory')
def getnetworkclientusage():
    url = gcu.url
    resp = gcu.requst_filter()
    request_type = "network client usage history"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/admins')
def getorganizationadmins():
    url = goa.url
    resp = goa.requst_filter()
    request_type = "organization admins"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

#def json2string(url,resp,request_type):
   # record_to_insert = (url, resp, request_type)
   # db.database(record_to_insert)

if __name__ == '__main__':
    app.run(debug=True)