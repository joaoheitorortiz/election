from Pessoa import Pessoa


def ler_dados():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    estado = input("Qual o seu Estado? ")
    pessoaLida = Pessoa(nome, idade, estado)
    return pessoaLida
