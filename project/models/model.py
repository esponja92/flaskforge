import sqlite3 as sql
from project.repository.database import Database

class Model(object):

    atributos = []
    database = ''
    tabela = ''
    campo_id = ''

    def __init__(self, valores=''):
        self.db = Database()

    def obter(self, query_sql ='', args=(), one=False):
        if(query_sql == ''):
            query_sql = 'SELECT ' + ','.join(self.atributos) + ' FROM '+self.tabela

        rows = self.db.query_db(query_sql, args, one, header=False)

        if(one):
            model = self.__class__([i for i in rows])
            return model

        else:
            lista_resultados = []
            for row in rows:

                model = self.__class__([i for i in row])
                lista_resultados.append(model)
            
            return lista_resultados

    def obterPorId(self, id):
        pessoa = self.obter('SELECT * FROM '+self.tabela+' WHERE id = ?',(id),one=True)

        return pessoa

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

    def atualizar(self, query_sql=''):
        atributos_sem_id = [a for a in self.atributos]
        atributos_sem_id.remove('id')

        if(query_sql == ''):
            query_sql = 'UPDATE ' + self.tabela + ' SET '
            
            campos = [k for k in atributos_sem_id]
            valores = []

            for campo in campos[0:-1]:
                query_sql += campo + ' = ?, '
                valores.append(self.__dict__['campo_'+campo])
            
            query_sql += campos[-1] + ' = ? WHERE id = ?'
            valores.append(self.__dict__['campo_'+campos[-1]])
            valores.append(self.campo_id)

        self.db.execute(query_sql, valores)