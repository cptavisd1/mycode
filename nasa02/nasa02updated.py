#!/usr/bin/env python3

import requests ##3rd party URL lookup

def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API url
    startdate = 'start_date=2018-06-01'
    enddate = '&end_date=END_DATE'
    mykey = '&api_key=gZle6ZJVOYpcRhQl21RvAnk4zL7AKhgxb63o8Eds'

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

    print(neojson)

main()


