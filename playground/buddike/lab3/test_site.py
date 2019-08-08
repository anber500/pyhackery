from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("test.html")

@app.route("/test2")
def about():
    return render_template("test2.html")