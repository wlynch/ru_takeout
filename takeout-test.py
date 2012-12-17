#!/usr/local/bin/python2.7

import json, httplib

#url="/0.1/rutgers-dining.txt"
#conn = httplib.HTTPSConnection("rumobile.rutgers.edu")
#conn.request("GET",url)
#conn.getresponse()
#resp = conn.getresponse()

resp = open('rutgers-dining.txt')
menu = json.loads(resp.read())

#print(type(resp))
#print(type(menu))

print(menu[0].keys())

for item in menu:
    print(item['location_name'])

print
#print menu[1]['meals']
i=3
print(menu[i]['location_name'])
print(menu[i]['meals'][0].keys())
for a in menu[i]['meals']:
    print(a['meal_name'])

print
print(menu[1]['meals'][3]['meal_name'])
print(menu[1]['meals'][3]['meal_avail'])
#print(menu[1]['meals'][3]['genres'])

print
for b in menu[1]['meals'][2]['genres']:
    print(b['genre_name'])
    for c in (b['items']):
        print("\t"+c)
