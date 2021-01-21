import json

import GetOrganisation as go
import GetNetwork as gn
import GetDevice as gd
import GetClient as gc
import DBconnection as db

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
def getnetworks():
    url = gn.url
    resp = gn.requst_filter()
    #print('kukuroute' + resp)
    request_type = "networks"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/devices')
def getdevices():
    url = gd.url
    resp = gd.requst_filter()
    request_type = "devices"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

@app.route('/clients')
def getclinets():
    url = gc.url
    resp = gc.requst_filter()
    request_type = "clients"
    record_to_insert = (url, resp, request_type)
    db.database(record_to_insert)
    return resp

#def json2string(url,resp,request_type):
   # record_to_insert = (url, resp, request_type)
   # db.database(record_to_insert)

if __name__ == '__main__':
    app.run(debug=True)