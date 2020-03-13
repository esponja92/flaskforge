import sqlite3 as sql
from project.repository.database import Database

class Model(object):

    atributos = []
    database = ''
    tabela = ''

    def __init__(self):
        self.db = Database()

    def obter(self, query_sql =''):
        if(query_sql == ''):
            query_sql = 'SELECT ' + ','.join(self.atributos) + ' FROM '+self.tabela

        resultado = self.db.query_db(query_sql)
        return resultado

    def criar(self, query_sql=''):

        atributos_sem_id = [a for a in self.atributos]
        atributos_sem_id.remove('id')

        if(query_sql == ''):
            query_sql = 'INSERT INTO '+self.tabela+'('+','.join(atributos_sem_id)+') VALUES ('
            query_sql += '?,'*(len(atributos_sem_id)-1) + "?"
            query_sql += ')'

        campos = [k for k in self.__dict__.keys() if 'campo' in k]
        valores = []
        for campo in campos:
            valores.append(self.__dict__[campo])

        self.db.execute(query_sql, valores)