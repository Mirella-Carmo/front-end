class Palestrante:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.nome_evento = ''
        self.img = ''
    
    def set_id(self, id):
        self.id = id
    
    def get_id(self):
        return self.id
    
    def set_nome(self, nome):
        self.nome = nome
    
    def set_nome_evento(self, nome):
        self.nome_evento = nome
    
    def set_imagem(self, img):
        self.img = img
    
    def get_nome(self):
        return self.nome
    
    def get_nome_evento(self):
        return self.nome_evento
    
    def get_imagem(self):
        return self.img