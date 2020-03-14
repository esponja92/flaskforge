from project.models.pessoa import Pessoa

def insere_pessoa_no_banco_test():
    pessoa = Pessoa()
    pessoa.campo_fname = 'Asdrubal'
    pessoa.campo_lname = 'de Mello Dantas'
    pessoa.criar()


def obter_pessoa_por_campos():
    pessoas = Pessoa().obter(onde = {'fname':'Asdrubal', 'lname':'de Mello Dantas'})

    for pessoa in pessoas:
        print(pessoa)
    
    print("#------------------------------------#")

def obter_todas_pessoas():
    pessoas = Pessoa().obter()

    for pessoa in pessoas:
        print(pessoa)

    print("#------------------------------------#")


def obter_pessoas_id():
    pessoas = Pessoa().obter()
    id = pessoas[0].campo_id

    pessoa = Pessoa().obterPorId(id)
    print(pessoa)

    print("#------------------------------------#")
