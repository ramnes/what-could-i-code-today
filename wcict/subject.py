from random import choice
from flask import current_app


language = ["C", "C++", "Python", "Java", "Whitespace", "Brainfuck"]

what = ["a random coding subject generator",
        "a {} compiler".format(choice(language)),
        "a {} prepocessor".format(choice(language))]

tech = ["Heroku", "Amazon AWS", "Emacs", "my feets"]

def random_subject(app=current_app):
    return "{} in {} with {} and {}".format(choice(what), choice(language), choice(tech), choice(tech))


__all__ = ["random_subject"]
