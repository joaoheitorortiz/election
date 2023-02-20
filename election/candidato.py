class Candidato:
    def __init__ (self, nome, numero, cargo):
        self. nome = nome
        self.numero = numero
        self.cargo = cargo
    
    def __str__ (self):
        return f"{self.nome} {self.numero} {self.cargo}"