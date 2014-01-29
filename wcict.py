#!/usr/bin/env python3.3
import logging
import postgresql

from flask import Flask, render_template
from subject import random_subject
from options import options, define


define("config", type=str, help="apply this config")
app = Flask(__name__)


def init_app():
    app.config.from_pyfile("config/default.py")
    if options.config:
        app.config.from_pyfile(options.config)
    app.db = init_db()
    return app


def init_db():
    return postgresql.open(app.config["POSTGRES_URL"])


@app.route('/', methods=['GET'])
def get_home():
    return render_template("home.html", subject=random_subject())


init_app()
if __name__ == '__main__':
    app.run()
