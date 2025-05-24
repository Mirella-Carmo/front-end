class Palestrante:
    def __init__(self):
        self.id = 0
        self.foto = ''
        self.nome = ''
        self.descricao_carreira = ''
        self.data_hora = ''
        self.nome_evento = ''
    
    def set_id(self, id):
        self.id = id
    
    def get_id(self):
        return self.id
    
    def set_foto(self, img):
        self.foto = img
    
    def get_foto(self):
        return self.foto
    
    def set_nome(self, nome):
        self.nome = nome
    
    def get_nome(self):
        return self.nome
    
    def set_descricao_carreira(self, descricao):
        self.descricao_carreira = descricao
    
    def get_descricao_carreira(self):
        return self.descricao_carreira
    
    def set_data_hora(self, data):
        self.data_hora = data
    
    def get_data_hora(self):
        return self.data_hora
    
    def set_nome_evento(self, nome):
        self.nome_evento = nome
    
    def get_nome_evento(self):
        return self.nome_evento