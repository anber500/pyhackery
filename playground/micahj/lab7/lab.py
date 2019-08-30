from openpyxl import load_workbook
import json
import hug
import os

# from .snippets import dict_factory
# import sqlite3 as sqlite
# print(dict_factory)
print(__file__)
CURR_DIR = os.path.dirname(os.path.abspath(__file__))


def mygen():
    start = 10
    yield start + 1
    yield start + 2
    yield start + 4


@hug.cli()
def fetch_it():
    path = os.path.join(CURR_DIR, 'Book1.xlsx')
    wb = load_workbook(filename=path)
    # print(wb)
    ws = wb.active
    # header

    row_gen = ws.rows
    #
    # headers = [c.value for c in next(row_gen)]
    # print(headers)

    rows = []
    for row in row_gen:
        rows.append([c.value for c in row])
    headers = rows[0]
    data = rows[1:]
    #
    # print(headers)
    # print(data)

    a = list(zip([1,2], [3,4]))
    # print(a)

    data_dict = [dict((zip(headers, r))) for r in data]
    # print(data_dict)
    return json.dumps(data_dict, indent=2)

def load_data_to_sqlite():
    pass
