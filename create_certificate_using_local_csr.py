#!/usr/bin/python
import json
import requests
##change username/password here 
login = requests.request("POST","http://192.168.10.80/api/1/auth/login",data=json.dumps({'username': "lemur", 'password': "lemur"}),headers={'content-type': 'application/json'})

print login.json()

Auth = {'Authorization': 'token %s' %login.json()["token"], 'content-type': 'application/json'}




#it is working
csr_req = requests.request("POST","http://192.168.10.80/api/1/certificates",data=json.dumps({"owner": "aaaa@exddamplea.net","commonName": "aaaa.eaaxample.net","authority": {"name": "aaaaa" },"csr":"-----BEGIN CERTIFICATE REQUEST-----\nMIICxzCCAa8CAQAwgYExCzAJBgNVBAYTAkFVMQ0wCwYDVQQIDARQQUtJMRIwEAYD\nVQQHDAlJU0xBTUFCQUQxDTALBgNVBAoMBElJSUkxDDAKBgNVBAsMA0dHRzEQMA4G\nA1UEAwwHdXNlcjEyMzEgMB4GCSqGSIb3DQEJARYRdXNlcjEyM0BnbWFpbC5jb20w\nggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDzzV4H1epwXODPs9AkioTv\nQLRtea12vCbZJhKkH59hWhDMjqNRkh8qc4R9gk83lingdWK+L35OkGNi6DG9zseh\ncVRf68sNpTeFg+eXGRmEdTallBqPd5NS3JlMmXxbLEWrELiw4gPp3JpNAzoYZUxb\n4Uk4ho9EN8Fd1/lGmubvyvkYJ1mbpsK1LfaFohGYu+7nMvU4tn1Av/zyTGcIikVu\nU4UA23jKAMzjlSKdTJH/nmqvMi2wltRtb7DNpI/5HAancrnyEzeXC5IN+sPV/5oh\nxdxCyAkp1kDrWhC2yvoffzipoqEFESWmfFrJ8riTiQZqOIWqW+ZasZtu4GDqm4CL\nAgMBAAGgADANBgkqhkiG9w0BAQsFAAOCAQEAH/PKs5kTmMPRW2Icy4Yj7vdzjpaA\n/r1glm0voMR5ytPo0+lXHDTQwt/1ObQvr8FnT2z8iqRvfXiv6WWruLzwEEVWsCFL\ny7RAa+K0wqP23CfxzCy/S4ZwCcR+wQb3UnWui8eMxgU1IBjupCR9kPFhL//aA+lm\njBi5YruBgX7MdlW+AlkuVDljzXm1orFYZFzS7OlybH5jh/B3Z2ygbC++Y24XI3qm\n5IYpsxFbOmrj7y3IXN/990305blCcKhpaG+FMTKhNqkXMYKYsZseIO3xdO4Ufjl/\nqS2jjsE1sFxmKbabhguhTT06oGimT+TbgoYVkc0DWhIdLcrOdxhGsFwdqg==\n-----END CERTIFICATE REQUEST-----"}),headers=Auth)



print csr_req.json()
