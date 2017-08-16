import json
from pprint import pprint
import sys
from pkgutil import simplegeneric


#with open('authors.json', 'w') as data_file:
   # for obj in data_json
  #  data = json.load(data_file)
#pprint(data)
   # string = json.dumps(data)
with open('authors.json', 'r') as f:
  data_json=json.load(f)

with open('test.json', 'w') as outfile:
    for obj in data_json:
        outfile.write(json.dumps(obj) + "\n")
        

pprint(outfile)
