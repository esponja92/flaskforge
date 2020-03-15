from project.models.model import Model

class Pessoa(Model):

    def __init__(self, valores=[]):
        Model.__init__(self, 'pessoa', ['id','fname','lname'], valores)