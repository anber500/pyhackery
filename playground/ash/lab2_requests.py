import requests
import json
from collections import namedtuple

title = namedtuple("Title", "title,id")


def budd(i):
    return title(title=i['title'], id=i['id'])


def condition(i):
    return i['completed']


res = requests.get(url='https://jsonplaceholder.typicode.com/todos')
data = res.json()
result = [budd(item).id for item in data if condition(item)]
pretty = json.dumps(result, indent=3, sort_keys=True)
print(pretty)
print(len(result))
