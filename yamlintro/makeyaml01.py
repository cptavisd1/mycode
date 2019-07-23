#!/usr/bin/env python3

# yaml is not part of standard library
# python3 -m pip install pyyaml
import yaml

def main():
    ## create blob of data to work with
    hitchhikers = [{'name': "Zaphod Beeblebrox", "species": "Betelgeusian"}, {"name": "Arthur Dent", "species": "Human"}]

    print(hitchhikers)

    yamlstring + yaml.dump(hitchhikers)
    
    print(yamlstring)

main()

