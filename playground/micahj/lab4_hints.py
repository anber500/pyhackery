import os

from playground.micahj.scratchpad import jprint
from pyhackery.csv_hack import read_a_simple_csv
from pyhackery.utils import to_lookup

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# load csv file data
data = read_a_simple_csv(path=os.path.join(CURRENT_DIR, 'customer.csv'))
jprint(data, "data from csv file")

# turn the list into a lookup - group on name : just like in dotnet lambdas
# are a quick inline way of writing a function
# go and have a look at the to_lookup function
lookup = to_lookup(data, key_func=lambda item: item['name'].lower())
jprint(lookup, "converted to a lookup using inline lambda function")


def key_selector(item):
    return item['name'].lower()


# we can use the function 'key_selector' instead of the inline lambda if
# you find that clearer - the result will be the same
lookup = to_lookup(data, key_func=key_selector)
jprint(lookup, "converted to a lookup using a function (def)")

# run with
# python -m playground.micahj.lab4_hints
