# Python Program to read JSON file
# autor: Abhijit Rao

import os
import json

# Define required variables for program
data_dict = dict()
i = ""
os.chdir('../data')

f = open('jira_details.json')

data = json.load(f)
#print(data)

for i in data['issues']:
    print(i)
    data_dict = {"id": i["id"],
                 "key": i["key"],
                }
    print(data_dict)

# close the json file
f.close()
