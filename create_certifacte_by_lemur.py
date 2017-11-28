#!/usr/bin/python
import json
import requests
##username/password to login lemur to perform the desired action 
login = requests.request("POST","http://192.168.10.80/api/1/auth/login",data=json.dumps({'username': "lemur", 'password': "lemur"}),headers={'content-type': 'application/json'})


print login.json()

Auth = {'Authorization': 'token %s' %login.json()["token"], 'content-type': 'application/json'}




cert_req = requests.request("POST","http://192.168.10.80/api/1/certificates",data=json.dumps({"owner": "aa12@exddamplea.net","commonName": "aa1.example.net","country": "PA","replacements": [{"id": 1 }],"notify": "true","validityEnd": "2026-01-01T08:00:00.000Z", "authority": {"name": "authority_CA" }, "organization": "CODEF.", "location": "Los Gataaos", "state": "Caldifornia", "user": { "username": "abb1","active": "true","email": "aa@example.com"}, "roles": [{"id": 1, "description": "admin role", "name": "aaa@eaaaxample.com"}],"validityStart": "2017-11-11T04:19:48.000Z","organizationalUnit": "Operations"}),headers=Auth)


print cert_req.json()


