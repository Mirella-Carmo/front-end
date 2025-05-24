class Categorias:
    def __init__(self):
        self.nome = ''
        self.imagem =''
        self.id_evento = 0
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_nome(self):
        return self.nome
    
    def set_imagem(self, img):
        self.imagem = img
    
    def get_imagem(self):
        return self.imagem
    
    def set_id_evento(self, id):
        self.id_evento = id
    
    def get_id_evento(self):
        return self.id_evento.get_id()