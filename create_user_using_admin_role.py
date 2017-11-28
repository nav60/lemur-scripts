#!/usr/bin/python
import json
import requests
login = requests.request("POST","http://192.168.10.80/api/1/auth/login",data=json.dumps({'username': "lemur", 'password': "lemur"}),headers={'content-type': 'application/json'})
print login.json()
Auth = {'Authorization': 'token %s' %login.json()["token"], 'content-type': 'application/json'}





test = requests.request("POST","http://192.168.10.80/api/1/users",data=json.dumps({'username': "aa", 'aaa': "aaa" ,"email":"aaa@gmail.com","active": "true", "roles": [{'id':1}or{'name': 'myRole'}]}),headers=Auth)


print test.json()
