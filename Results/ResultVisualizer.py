#!/usr/bin/env python

import yaml

with open("Default/Abilene-fw1chain-source0-2019-07-29_00-51-32_7480.yaml", 'r') as stream:
    try:
        #print(yaml.safe_load(stream))
        for data in yaml.load_all(stream):
            for dat in data:
                print(dat)
    except yaml.YAMLError as exc:
        print(exc)