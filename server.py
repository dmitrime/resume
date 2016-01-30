# -*- coding: utf-8 -*-

import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing():
    js = None
    with open('data/resume.json') as f:
        js = json.load(f)
    return render_template('index.html', **js)

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0')
