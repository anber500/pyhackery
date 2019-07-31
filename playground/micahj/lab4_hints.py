import os

from playground.micahj.scratchpad import jprint
from pyhackery.csv_hack import read_a_simple_csv

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def try_csv():
    data = read_a_simple_csv(path=os.path.join(CURRENT_DIR, 'customer.csv'))
    jprint(data)


try_csv()

# run with
# python -m playground.micahj.lab4_hints
