#!/usr/local/bin/python3
import pprint


test_dict = {'name': 'Boardwalk', 'cost': '400', 'location': 39, 'type': 'property',
                'base_rent': '50', 'group': 'darkblue', 'owner': None}


#pprint.pprint(test_dict)
for key in test_dict:
    print(key, test_dict[key])

for test_dict['name'] in test_dict:
    print(test_dict[key])