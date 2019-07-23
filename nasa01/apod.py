#!/usr/bin/env python3
import urllib.request
import json
import webbrowser
from pprint import pprint as pp # part of standard library


# Define some constants
NASAAPI = 'https://api.nasa.gov/planetary/apod?' # this is our api to all
MYKEY = 'api_key=gZle6ZJVOYpcRhQl21RvAnk4zL7AKhgxb63o8Eds'

## pretty print json
def main():
    """run-time code"""
    nasaapiobj = urllib.request.urlopen(NASAAPI + MYKEY) # call the webservice
    nasaread = nasaapiobj.read() # parse the JSON blob returned
    convertedjson = json.loads(nasaread.decode('utf-8')) # convert json

    # show converted json
    print(convertedjson) # show converted json
    input('\nThis is converted json. Press ENTER to continue.') # pause for enter

    # show Pretty Print json
    pp(convertedjson) # this is Pretty Print in action
    # pprint.pprint(convertedjson)
    input('\nThis is pretty printed JSON. Press ENTER to continue.')

    print(convertedjson['explanation'])
    input('\nPress ENTER to view this photo of the day')

    webbrowser.open(convertedjson['hdurl'])

main()


