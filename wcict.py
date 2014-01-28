#!/usr/bin/env python3.3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "It works. :-D"
