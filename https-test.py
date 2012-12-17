#!/usr/bin/python

import json, httplib

url="/0.1/rutgers-dining.txt"
conn = httplib.HTTPSConnection("rumobile.rutgers.edu")
conn.request("GET",url)
resp = conn.getresponse()

#menu = json.loads(resp.read())

print(resp.read())
