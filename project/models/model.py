import sqlite3 as sql

from project.repository.database import Database

class Model(object):

    atributos = []
    database = ''
    tabela = ''
    campo_id = ''

    def __init__(self, valores=''):
        self.db = Database.getInstance()

    def __str__(self):
        stringify = ''
        for atributo in self.atributos:
            stringify+= atributo+' = '+str(self.__dict__['campo_'+atributo])+' / '
        return stringify

    def obter(self, onde = {}, one=False):

        args = []

        query_sql = 'SELECT * FROM '+self.tabela

        if(onde != {}):
            query_sql += ' WHERE '
            qtd_keys = len(onde.keys())

            for key in onde.keys():
                #testa se eh o ultimo elemento
                if(qtd_keys > 1):
                    query_sql += key + ' = ? AND '
                else:
                    query_sql += key + ' = ?'
                args.append(onde[key])
                qtd_keys -= 1

        # print(query_sql)
        # print(args)

        rows = self.db.query_db(query_sql, args, one, header=True)

        resultado = []

        if(one):
            cabecalho = rows[0]
            row = rows[1]
            novos_atributos = []


            for i in range(len(cabecalho)):
                novos_atributos.append(row[str(cabecalho[i])])

            resultado = self.__class__(novos_atributos)

        else:
            cabecalho = rows[0]
            for row in rows[1::]:
                novos_atributos = []
                for i in range(len(cabecalho)):
                    novos_atributos.append(row[str(cabecalho[i])])

                model = self.__class__(novos_atributos)
                resultado.append(model)

        return resultado

    def obterPorId(self, id):
        pessoa = self.obter(onde=({'id':id}),one=True)

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

        # print(query_sql)
        # print(valores)

        self.db.execute(query_sql, valores)

    def atualizar(self, query_sql='', valores=[]):

        if(query_sql == ''):
            atributos_sem_id = [a for a in self.atributos]
            atributos_sem_id.remove('id')
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

    def deletar(self, query_sql='', valores=[]):

        valores = []
        if(query_sql == ''):
            query_sql = 'DELETE FROM '+self.tabela+' WHERE '

            campos = [k for k in self.atributos]

            for campo in campos[0:-1]:
                query_sql += campo + ' = ? AND '
                valores.append(self.__dict__['campo_'+campo])
            
            query_sql += campos[-1] + ' = ?'
            valores.append(self.__dict__['campo_'+campos[-1]])

        # print(query_sql)
        # print(valores)
        self.db.execute(query_sql, valores)
