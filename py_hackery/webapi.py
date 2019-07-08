#!venv/bin/python3

# now see here : http://flask.pocoo.org/
from flask import Flask
from awesomeness.awesome import something_awesome
app = Flask(__name__)


@app.route("/")
def hello():
    return f"<h1>{something_awesome()}</h1>"


if __name__ == '__main__':
    app.run(port='8081')