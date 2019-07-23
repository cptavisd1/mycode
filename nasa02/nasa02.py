#!/usr/bin/env python3
import urllib.request
import json

## define NEOapi
neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startdate = 'start_date=2018-06-01'
enddate = '&end_date=END_DATE'
mykey = '&api_key=gZle6ZJVOYpcRhQl21RvAnk4zL7AKhgxb63o8Eds'

neourl = neourl + startdate + mykey

# call the webservice
neourlobj = urllib.request.urlopen(neourl)

# read the file-like object
neoread = neourlobj.read()

#decode jason to python structure
decodeneo = json.loads(neoread.decode('utf-8'))

# display our pythonic data
print("\n\nConverted python data")
print(decodeneo)


