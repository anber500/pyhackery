import hug
import requests


@hug.get()
def fetch():
    return requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()


@hug.get('/home', output=hug.output_format.html)
def home():
    with open("web/index.html") as fp:
        return fp.read()
