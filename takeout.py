#!/usr/bin/python

import json, httplib

url="/0.1/rutgers-dining.txt"
conn = httplib.HTTPSConnection("rumobile.rutgers.edu")
conn.request("GET",url)
resp = conn.getresponse()

#resp = open('rutgers-dining.txt')
menu = json.loads(resp.read())

#print(menu[0].keys())

#for item in menu:
#    print(item['location_name'])

#print
#print menu[0]['meals']
#i=3
#print(menu[i]['location_name'])
#print(menu[0]['meals'][0].keys())
#for a in menu[0]['meals']:
#    print(a['meal_name'])

#print
#print(menu[1]['meals'][3]['meal_name'])
#print(menu[1]['meals'][3]['meal_avail'])
#print(menu[1]['meals'][3]['genres'])

i=1
print(menu[i]['location_name'])
#print(menu[i]['meals'][4])
#print

for b in menu[i]['meals'][3]['genres']:
    print(b['genre_name'])
    #print(b)
    for c in (b['items']):
        print("\t"+c)
