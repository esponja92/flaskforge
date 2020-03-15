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
        campos = ['campo_'+campo for campo in self.atributos]
        for i in range(len(campos)):
            chave = self.atributos[i]
            valor = self.__obtemValorDoCampo(campos[i], string=True)
            stringify += chave+' = '+valor+' / '
            
        return stringify

    def __row_to_model(self, row, cabecalho):

        novos_atributos = []
        for coluna in cabecalho:

            novos_atributos.append(row[coluna])

        model = self.__class__(novos_atributos)
        return model

    def __obtemValorDoCampo(self,campo, string=False):
        campos = self.__obtemCampos()
        campo = campos[campo]
        if(string):
            campo = str(campo)
        return campo

    def __obtemCampos(self):
        campos = [k for k in self.__dict__.keys() if 'campo_' in k]
        atributos = { campo: self.__dict__[campo] for campo in campos }

        return atributos

    def obter(self, onde = {}, one=False):

        args = []

        query_sql = 'SELECT * FROM {tabela}'.format(tabela=self.tabela) 

        if(onde != {}):
            query_sql += ' WHERE '
            qtd_keys = len(onde.keys())

            for key in onde.keys():
                #testa se eh o ultimo elemento
                if(qtd_keys > 1):
                    query_sql += '{parametro} = ? AND '.format(parametro=key)
                else:
                    query_sql += '{parametro} = ?'.format(parametro=key)
                args.append(onde[key])
                qtd_keys -= 1

        # print(query_sql)
        # print(args)

        rows = self.db.query_db(query_sql, args, one, header=True)
        resultado = []

        cabecalho = rows[0]
        for row in rows[1::]:
            # print(row)
            if(one):
                if(row):
                    return self.__row_to_model(row,cabecalho)
            else:
                model = self.__row_to_model(row,cabecalho)
                resultado.append(model)

        return resultado

    def obterPorId(self, id):
        pessoa = self.obter(onde=({'id':id}),one=True)

        return pessoa

    def criar(self):

        query_sql=''
        valores = []
        atributos_sem_id = [a for a in self.atributos]
        atributos_sem_id.remove('id')

        query_sql = 'INSERT INTO {tabela} ({atributos}) VALUES ({valores})'.format(
            tabela=self.tabela,
            atributos=','.join(atributos_sem_id),
            valores='?,'*(len(atributos_sem_id)-1) + "?"
        )

        campos = self.__obtemCampos()
        for campo in campos.keys():
            valores.append(self.__dict__[campo])

        # print(query_sql)
        # print(valores)

        self.db.execute(query_sql, valores)

    def atualizar(self):

        valores = []
        query_sql = 'UPDATE {tabela} SET '.format(tabela=self.tabela)

        atributos_sem_id = [a for a in self.atributos]
        atributos_sem_id.remove('id')
        
        campos = [k for k in atributos_sem_id]
        qtd_keys = len(campos)

        for campo in campos:
            #testa se eh o ultimo elemento
            if(qtd_keys > 1):
                query_sql += '{campo} = ?,'.format(campo=campo)
            else:
                query_sql += '{campo} = ? WHERE id = ?'.format(campo=campos[-1])

            valores.append(self.__obtemValorDoCampo('campo_'+campo))
            qtd_keys-=1        

        valores.append(self.campo_id)

        # print(query_sql)
        # print(valores)

        self.db.execute(query_sql, valores)

    def deletar(self):

        valores = []
        query_sql = 'DELETE FROM {tabela} WHERE '.format(tabela=self.tabela)

        campos = [k for k in self.atributos]
        qtd_keys = len(campos)

        for campo in campos:
            #testa se eh o ultimo elemento
            if(qtd_keys > 1):
                query_sql += '{campo} = ? AND '.format(campo=campo)
            else:
                query_sql += '{campo} = ?'.format(campo=campos[-1])
            valores.append(self.__obtemValorDoCampo('campo_'+campo))
            qtd_keys-=1

        # print(query_sql)
        # print(valores)
        self.db.execute(query_sql, valores)
