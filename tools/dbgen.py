import sqlite3

def create():
    
    nome_tabela = input("Informe o nome da tabela a ser criada: ")    

    criar = "s"

    nomes_campo = []
    tipos_campo = []

    while(criar == "s"):
        nome_campo = input("Informe o nome do novo campo: ")
        tipo_campo = input("Informe o tipo do novo campo: (1-NULL, 2-INTEGER, 3-REAL, 4-TEXT, 5-BLOB): ")
        try:
            #conferindo se o usuario informou o tipo correto
            if tipo_campo not in ["1","2","3","4","5"]:
                raise Exception("Tipo informado não corresponde a lista dos tipos permitidos para criação de novos campos")   

            nomes_campo.append(nome_campo)
            tipos_campo.append(tipo_campo)

        except Exception as e:
            print(str(e))
        
        finally:
            criar = input("Deseja criar um novo campo?: (S/n)")
            if criar == "":
                criar = "s"


    #criando a tabela
    try:
        conn = sqlite3.connect('../database.db')

        sql = 'CREATE TABLE ' + nome_tabela + '('
        if len(nomes_campo) != len(tipos_campo):
            raise Exception("A quantidade de nomes de campos e tipos informados não estão iguais")

        sql = sql + "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            
        for i in range(len(nomes_campo)):
            sql = sql + nomes_campo[i] + " "

            if tipos_campo[i] == "1":
                sql = sql + "NULL"
            if tipos_campo[i] == "2":
                sql = sql + "INTEGER"
            if tipos_campo[i] == "3":
                sql = sql + "REAL"
            if tipos_campo[i] == "4":
                sql = sql + "TEXT"
            if tipos_campo[i] == "5":
                sql = sql + "BLOB"

            if i != len(nomes_campo) - 1:
                sql = sql + ","
        
        sql = sql + ')'

        conn.execute(sql)
        print("Tabela criada com sucesso!")

    except Exception as e:
        print("Ocorreu um erro na criação da tabela:")
        print(str(e))

    finally:
        conn.close()

if __name__ == "__main__":
    print("Selecione a operação que deseja realizar:")
    print("1 - criar uma nova tabela")
    #print("4 - consultar registros em uma tabela criada")
    #print("2 - inserir registros em uma tabela criada")
    #print("3 - atualizar registros em uma tabela criada")
    #print("5 - remover registros em uma tabela criada")

    opcao = input("Digite a opção: ")

    if opcao == "1":
        create()