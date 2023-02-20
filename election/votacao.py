from Pessoa import Pessoa
from Candidato import Candidato
from le_dados import ler_dados


def pode_votar(idade):
    resultado = ""
    if idade >= 16 and idade < 18 or idade  >= 60:
        resultado = "pode"
    elif idade >= 18:
        resultado ="deve"
    else:
        resultado = "nao pode"
    return resultado

def votacao(eleitores):
    pessoa = ler_dados()
    acao = ""
    acao = pode_votar(pessoa.idade)
    print("Caro cidadao {}, voce {} votar".format(pessoa.nome , acao))
    if acao != "nao pode":
        jair = Candidato("Jair", 22, "Presidente")
        lula = Candidato("Lula", 13, "Presidente")
        msg = "Escolha: " + jair.__str__() + " ou " + lula.__str__() + ""
        voto = input(msg)
        pessoa.voto = voto
    eleitores.append(pessoa.__str__())