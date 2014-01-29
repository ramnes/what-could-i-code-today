from random import choice
from flask import current_app


languages = ["C", "C-ANSI", "C++", "C#",
             "Python", "Python2.7", "Python3",
             "Java",
             "Javascript",
             "Bash", "SH", "PHP",
             "Whitespace", "Brainfuck", "Lua", "ASM"]

whats = ["a random coding subject generator", "a {language} compiler",
         "{language} bindings", "a {language}-based library wrapper",
         "a {provider} API wrapper", "a {techno} client"]

technos = ["Heroku", "Amazon AWS", "Firebase",
           "MongoDB", "PostgreSQL", "MySQL", "Cassandra", "MySQL", "Riak",
           "Docker", "VirtualBox", "VMWare",
           "CUDA", "OpenGL", "Unity",
           "my dick", "my feets"]

providers = ["Youtube", "Facebook", "DailyMotion", "Yahoo"]


def random_subject(app=current_app):
    what = choice(whats)
    what = what.format(language=choice(languages),
                       provider=choice(providers),
                       techno=choice(technos))
    language = choice(languages)
    techno = choice(technos)
    return "{} in {} with {}".format(what, language, techno)


__all__ = ["random_subject"]
