class Evento:
    def __init__(self):
        self.id_evento = 0
        self.id_palestrante = 0
        self.banner = ''
        self.titulo = ''
        self.data_hora = ''
        self.local = ''
        self.descricao = ''
        self.nome_palestrante = ''
        self.foto_palestrante = ''
        self.curriculo_palestrante = ''
        
    def set_id(self, id_evento):
        self.id_evento = id_evento
    
    def get_id(self):
        return self.id_evento

    def set_id_palestrante(self, id):
        self.id_palestrante = id
    
    def get_id_palestrante(self):
        return self.id_palestrante
    
    def set_banner(self, link):
        self.banner = link
    
    def get_banner(self):
        return self.banner
    
    def set_titulo(self, nome):
        self.titulo = nome
    
    def get_titulo(self):
        return self.titulo
    
    def set_data_hora(self, data_hora):
        self.data_hora = data_hora
    
    def get_data_hora(self):
        return self.data_hora
    
    def set_local(self, local):
        self.local = local
    
    def get_local(self):
        return self.local
    
    def set_descricao(self, descricao):
        self.descricao = descricao
    
    def get_descricao(self):
        return self.descricao
    
    def set_nome_palestrante(self, nome):
        self.nome_palestrante = nome
    
    def get_nome_palestrante(self):
        return self.nome_palestrante
    
    def set_foto_palestrante(self,img):
        self.foto_palestrante = img
    
    def get_foto_palestrante(self):
        return self.foto_palestrante
    
    def set_curriculo_palestrante(self, curriculo):
        self.curriculo_palestrante = curriculo
    
    def get_curriculo_palestrante(self):
        return self.curriculo_palestrante