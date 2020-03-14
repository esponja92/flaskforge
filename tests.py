from project.tests.test_model_pessoa import *

if __name__ == "__main__":

    insere_pessoa_no_banco('silvio','santos')

    pessoa = obter_pessoa_por_campos({'fname':'silvio','lname':'santos'})
    print(pessoa)

    atualizar_pessoa_por_id(pessoa.campo_id, 'Hebe','Camargo')

    pessoa = obter_pessoa_por_campos({'fname':'Hebe','lname':'Camargo'})
    print(pessoa)

    pessoa.deletar()

    pessoa = obter_pessoa_por_campos({'fname':'Hebe','lname':'Camargo'})
    print(pessoa)