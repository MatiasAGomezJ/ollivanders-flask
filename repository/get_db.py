from flask import g
from repository.db import db


def get_db():
    if 'db' not in g:
        g.db = db

    return g.db