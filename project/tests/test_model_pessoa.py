from project.models.pessoa import Pessoa

def obter_pessoa_por_campos(campos):
    pessoa = Pessoa().obter(onde = campos, one = True)
    print(pessoa)
    
    print("#------------------------------------#")

def obter_todas_pessoas():
    pessoas = Pessoa().obter()

    for pessoa in pessoas:
        print(pessoa)

    print("#------------------------------------#")


def obter_pessoas_id(id):

    pessoa = Pessoa().obterPorId(id)
    print(pessoa)

    print("#------------------------------------#")

def insere_pessoa_no_banco(fname,lname):
    pessoa = Pessoa()
    pessoa.campo_fname = fname
    pessoa.campo_lname = lname
    pessoa.criar()

def atualizar_pessoa_por_id(id, fname, lname):
    pessoa = Pessoa().obterPorId(id)
    pessoa.campo_fname = fname
    pessoa.campo_lname = lname
    pessoa.atualizar()

def deletar_pessoa_por_id(id):
    pessoa = Pessoa().obterPorId(id)
    pessoa.deletar()
