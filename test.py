from project.models.pessoa import Pessoa

def insere_pessoa_no_banco_test():
    pessoa = Pessoa()
    pessoa.campo_fname = 'Asdrubal'
    pessoa.campo_lname = 'de Mello Dantas'
    pessoa.criar()

if __name__ == "__main__":

    pessoas_obtidas = Pessoa().obter(onde = {'fname':'Asdrubal', 'lname':'de Mello Dantas'})

    for pessoa in pessoas_obtidas:
        print(pessoa)
    
    print("#------------------------------------#")
    
    pessoas_obtidas = Pessoa().obter()

    for pessoa in pessoas_obtidas:
        print(pessoa)