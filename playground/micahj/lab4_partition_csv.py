import csv
import os
from pprint import pprint
from pyhackery.utils import to_lookup


def read_csv(path):
    with open(path) as fp:
        return [dict(row) for row in csv.DictReader(fp)]

        # [row for row in csv.DictReader(fp)]

        # reader = csv.DictReader(fp)
        # for line in reader:
        #     print(line)


curr_dir = os.path.dirname(os.path.abspath(__file__))
# print(curr_dir)
path = os.path.join(curr_dir, 'customer.csv')
# print(path)
# print(os.path.exists(path))
data = read_csv(path)
pprint(data)

import json
lookup_by_name = to_lookup(collection=data, key_func=lambda row: row['name'])
print(json.dumps(lookup_by_name, indent=3, sort_keys=True))

for key, results in lookup_by_name.items():
    print(key)
    print(json.dumps(results))

jimbobs = lookup_by_name['jimbob']
print(jimbobs)