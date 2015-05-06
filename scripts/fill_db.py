#!/usr/bin/env python

import json
from pprint import pprint

with open('db_fill/course.json') as data_file:
    data = json.load(data_file)

pprint(data)

#print data["CourseType"]
#print data["Course"]
#print data["Course"][0]["id"]
#print data["Course"][0]

import urllib2,json

url = 'http://localhost:8000/api/course/'
postdata = data["Course"][0]

req = urllib2.Request(url)
req.add_header('Content-Type','application/json')
data = json.dumps(postdata)

response = urllib2.urlopen(req,data)

