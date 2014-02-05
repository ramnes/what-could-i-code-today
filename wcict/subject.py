from random import choice
from flask import current_app


languages = ["C", "C-ANSI", "C89", "C++", "C#", "Objective-C", "Go",
             "Python", "Python2.7", "Python3",
             "Java", "Scala", "Clojure", "Groovy",
             "Javascript", "Node.js",
             "Ruby", "Ruby on Rails",
             "Bash", "PHP", "Perl",
             "ADA", "Fortran", "Pascal", "Perfect Developer",
             "Lisp", "Scheme",
             "Whitespace", "Brainfuck", "Lua", "ASM"]

whats = ["a random coding subject generator", "a {language} compiler",
         "{language} bindings", "a {language}-based library wrapper",
         "a {provider} API wrapper", "a {techno} client",
         "a key-value store", "a NoSQL database", "a SQL database",
         "a multiplayer game", "an OS", "a kernel module",
         "a MVC framework", "a {language} packages install tool",
         "a biomolecules simulator", "an new altcoin"]

technos = ["Heroku", "Amazon AWS", "Firebase", "Amazon S3",
           "MongoDB", "PostgreSQL", "MySQL", "Cassandra", "MySQL", "Riak",
           "Docker", "VirtualBox", "VMWare",
           "CUDA", "OpenGL", "Unity",
           "Sphinx",
           "my feets"]

providers = ["Youtube", "DailyMotion",
             "Facebook", "Twitter", "Google+", "LinkedIn"
             "Yahoo", "Google", "Bing",
             "Deezer", "Grooveshark", "Spotify",
             "Github", "Bitbucket",
             "Pastebin", "Pastie"]


def random_subject(app=current_app):
    what = choice(whats)
    what = what.format(language=choice(languages),
                       provider=choice(providers),
                       techno=choice(technos))
    language = choice(languages)
    techno = choice(technos)
    return "{} in {} with {}".format(what, language, techno)


__all__ = ["random_subject"]
