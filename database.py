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

    def insere(self, tabela, colunas, valores):
        query_sql = "INSERT INTO " + tabela + " ("
        
        values_sql = ''

        for coluna in colunas:
            query_sql += coluna
            values_sql += "?"
            
            if(coluna == colunas[-1]):
                query_sql += ")"
                values_sql += ")"
            else:
                query_sql += ","
                values_sql += ","

        query_sql += " VALUES (" + values_sql        
        
        self.execute(query_sql, valores)
        return

    def atualiza(self, tabela, colunas, valores, where_colunas, where_valores):
        query_sql = "UPDATE " + tabela + " SET "

        for i in range(len(colunas)):
            query_sql += colunas[i] + " = ?" 
            
            if(colunas[i] != colunas[-1]):
                query_sql += ","

        query_sql += " WHERE "

        for i in range(len(where_valores)) :
            query_sql += where_colunas[i] + " = ?"
            
            if(where_colunas[i] != where_colunas[-1]):
                query_sql += " AND "

        valores.extend(where_valores)

        self.execute(query_sql, valores)
        return

    def obtem(self, tabela, colunas='*', where_colunas='', where_valores='', one=False):
        query_sql = "SELECT "+colunas+" FROM " + tabela + " "

        if where_colunas != '' and where_valores != '':
            query_sql += " WHERE "
            for i in range(len(where_colunas)):
                query_sql += where_colunas[i] + "= ?"

                if i != len(where_colunas) - 1:
                    query_sql += " AND "

        try:

            rows = self.query_db(query_sql, where_valores, one)

        except Exception as e:
            print(str(e))
            return

        return rows

    def deleta(self, tabela, where_colunas, where_valores):
        query_sql = "DELETE FROM "+tabela+ " WHERE "

        if where_colunas != '' and where_valores != '':

            for i in range(len(where_colunas)):
                query_sql += where_colunas[i] + " = ?"

                if i != len(where_colunas) - 1:
                    query_sql += " AND "

        try:

            self.execute(query_sql, where_valores)

        except Exception as e:
            print(str(e))
            return

        return

if __name__ == "__main__":
    d = Database()
    # d.insere("pessoa", ['fname', 'lname'], ('caco','antibes'))
    # d.atualiza("pessoa", ['fname'], ["joão"],['fname'], ["caco"])
    # d.deleta('pessoa', where_colunas = ["fname"], where_valores = ["joão"])

    for row in d.obtem('pessoa'):
        print("id = {0}, fname = {1}".format(row['id'],row['fname']))