from votacao import votacao


i = "s"
eleitores = []
while i != "n":
    votacao(eleitores)
    escolha = input("Deseja continuar? digite 'n' para sair: ")
    i = escolha

print("eleitores = ", eleitores)
   