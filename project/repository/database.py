import sqlite3 as sql
from .database_singleton import DatabaseSingleton

@DatabaseSingleton
class Database(object):

    DATABASE = 'database.db'
    db = None

    def __init__(self):
        pass

    def get_db(self):

        if self.db is None:
            self.db = sql.connect(self.DATABASE)
            self.db.row_factory = sql.Row

        return self.db

    def close_db(self, cur):
        cur.close()
        self.db = None

    def query_db(self, query, args=(), one=False, header=False):

        cur = self.get_db().execute(query, args)
        cabecalho = [description[0] for description in cur.description]
        linhas = [row for row in cur.fetchall()]
        if(one):
            linhas = [linhas[0]] if len(linhas) else [[]]
        if(header):
            rv = [cabecalho] + linhas
        else:
            rv = linhas

        self.close_db(cur)

        return rv

    def execute(self, query, args):

        db = self.get_db()
        db.execute(query, args)
        db.commit()
        self.close_db(db)