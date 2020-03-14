from project.models.model import Model

class Pessoa(Model):

    def __init__(self, valores=[]):
        self.atributos = ['id','fname','lname']
        self.tabela = 'pessoa'
        
        if(valores == []):
            self.campo_fname = ''
            self.campo_lname = ''
        else:
            self.campo_id = valores[0]
            self.campo_fname = valores[1]
            self.campo_lname = valores[2]

        Model.__init__(self)
