#!/usr/bin/python3
# source testumgebung/bin/activate

from flask import Flask
from flast import render_template


app = Flask(__name__)

# logo hamburg-lab

@app.route('/')
def start():
    return  render_template("home.html")


app.run(host='::',debug=True)
