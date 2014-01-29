from flask import current_app


def random_subject(app=current_app):
    return app.db


__all__ = ["random_subject"]
