#!/usr/bin/env python3

def main():
    # Read in our list data
    networklists = []
    with open('driverip.txt', 'r') as driverip:
        for sline in driverip: # single line from our file is sline
            # append adds to the end of our list
            networklists.appen(sline.rstrip("\n").split(' '))

    print(networklists)

    for driveandip in networklists:
        print('SSH to ' + driveandip[1] + ' using driver ' + driveandip[0]

main()

