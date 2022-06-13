from flask import g
from repository.db_atlas import db_atlas


def get_db_atlas():
    if 'db_atlas' not in g:
        g.db_atlas = db_atlas

    return g.db_atlas