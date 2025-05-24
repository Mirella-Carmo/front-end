class Evento:
    def __init__(self):
        self.id = 0
        self.banner = ''
        self.titulo = ''
        self.data_hora = ''
        self.local = ''
        self.descricao = ''
        self.nome_palestrante = ''
        self.foto_palestrante = ''
        
    def set_id(self, id):
        self.id = id
    
    def get_id(self):
        return self.id
    
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