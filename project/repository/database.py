import sqlite3 as sql

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

    def query_db(self, query, args=(), one=False):

        cur = self.get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

    def execute(self, query, args):

        db = self.get_db()
        db.execute(query, args)
        db.commit()