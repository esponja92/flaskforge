from project.tests.test_model_pessoa import *

if __name__ == "__main__":

    insere_pessoa_no_banco('silvio','santos')

    pessoa = Pessoa().obter({'fname':'silvio','lname':'santos'}, one=True)
    print(pessoa)

    atualizar_pessoa_por_id(pessoa.campo_id, 'Hebe','Camargo')

    pessoa = Pessoa().obter({'fname':'Hebe','lname':'Camargo'}, one=True)
    print(pessoa)

    pessoa.deletar()

    pessoa = Pessoa().obter({'fname':'Hebe','lname':'Camargo'}, one=True)
    print(pessoa)