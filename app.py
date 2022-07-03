#!/usr/bin/python3

# Benutzer: cumulus im Home-Verzeichnis
# source testumgebung/bin/activate

from flask import Flask
from flask import render_template

import requests
import urllib3

LEAF11 = "192.168.200.2"

# nicht schoen aber heute Nachmittag zweckmaessig
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

@app.route('/')
def start():
    return render_template("home.html")

@app.route('/alq')
def alq():
    return render_template("alq.html")

@app.route('/help')
def help():

    return render_template("help.html")

@app.route('/layout')
def layout():
    return render_template("layout.html")

@app.route('/leaf11')
def leaf11():
    mac_liste=[]
    ergebnis = requests.get('https://192.168.200.2:8765/cue_v1/bridge/domain/alq/mac-table', auth=('cumulus','CumulusLinux!'), verify=False)
    for key in ergebnis.json():
      for sub_key in  ergebnis.json()[key]:
         if sub_key == "mac":
            mac_liste.append(ergebnis.json()[key][sub_key])


    return render_template("leaf11.html", ergebnis=mac_liste)

app.run(host='::',debug=True)
