class Pessoa:
    def __init__(self, nome, idade, estado):
        self.nome = nome
        self.idade = idade
        self.estado = estado
        self.voto = ""
    def __str__(self):
        return f"{self.nome}, {self.idade}, {self.estado}, {self.voto}"

