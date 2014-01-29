#!/usr/bin/env python3.3
import logging
import postgresql

from flask import Flask, render_template
from subject import random_subject
from options import options, define, parse_command_line


define("config", type=str, help="apply this config")
define("host", type=str, help="bind to this host", default="0.0.0.0")
define("port", type=int, help="bind to this port", default=8000)

app = Flask(__name__)


def init_app():
    app.config.from_pyfile('config/default.py')
    if options.config:
        logging.info("Loading config %s" % options.config)
        app.config.from_pyfile("config/%s" % options.config)
    app.db = init_db()
    return app


def init_db():
    url = app.config["POSTGRES_URL"]
    logging.info("Connecting to %s", url)
    return postgresql.open(url)


@app.route('/', methods=['GET'])
def get_home():
    return render_template("home.html", subject=random_subject())


if __name__ == '__main__':
    argv = parse_command_line()
    init_app()
    app.run(host=options.host, port=options.port)
