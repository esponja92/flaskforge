import sqlite3 as sql
import os

try:
    from project.config.env import *
except ImportError:
    import sys
    sys.path.append('../')
    from config.env import *

class Database(object):

    DATABASE = DATABASE_PATH
    db = None

    def __init__(self):
        print(os.path.abspath(self.DATABASE))

    def get_db(self):

        if self.db is None:
            self.db = sql.connect(self.DATABASE)
            self.db.row_factory = sql.Row

        return self.db

    def query_db(self, query, args=(), one=False, header=False):

        cur = self.get_db().execute(query, args)
        cabecalho = [description[0] for description in cur.description]
        linhas = [row for row in cur.fetchall()]
        if(one):
            linhas = [linhas[0]]
        if(header):
            rv = [cabecalho] + linhas
        else:
            rv = linhas
        cur.close()

        return rv

    def execute(self, query, args):

        db = self.get_db()
        db.execute(query, args)
        db.commit()