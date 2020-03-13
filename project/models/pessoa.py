from project.models.model import Model

class Pessoa(Model):

    def __init__(self):
        self.atributos = ['id','fname','lname']
        self.tabela = 'pessoa'
        self.campo_fname = ''
        self.campo_lname = ''

        Model.__init__(self)