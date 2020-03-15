from project.tests.test_model_pessoa import *

if __name__ == "__main__":

    insere_pessoa_no_banco('silvio','santos')

    obter_pessoa_por_campos({'fname':'silvio','lname':'santos'})

    pessoa = Pessoa().obter({'fname':'silvio','lname':'santos'},one=True)
    atualizar_pessoa_por_id(pessoa.campo_id, 'Hebe','Camargo')

    obter_pessoa_por_campos({'fname':'Hebe','lname':'Camargo'})
    pessoa = Pessoa().obter({'fname':'Hebe','lname':'Camargo'},one=True)

    if(pessoa):
        pessoa.deletar()

    pessoa = obter_pessoa_por_campos({'fname':'Hebe','lname':'Camargo'})