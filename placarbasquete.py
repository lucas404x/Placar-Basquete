def adcPonto(partida, time, p2):
    partida[time] += p2

def verificarPontos(partida):

    print()
    if(partida['casa'] > partida['visitante']):
        print("Time da Casa venceu o jogo!")
    elif(partida['casa'] < partida['visitante']):
        print("Time dos Visitantes venceram o jogo!")
    else:
        print("Empate!")
    
def mostrarPlacar(partida):

    print()
    print("                 PLACAR                    ")
    print()
    print("Casa: " + str(partida['casa']) + "                    " + "Visitantes: " + str(partida['visitante']))
    print()

def placar(partida):

    while True:
        mostrarPlacar(partida)
        print("[1] - Casa")
        print("[2] - Visitante")
        p = int(input("Quem fez o ponto? "))
        while(p != 1 and p != 2):
            print("[1] - Casa")
            print("[2] - Visitante")
            p = int(input("Quem fez o ponto? "))
        print("[1] - 1 ponto")
        print("[2] - 2 pontos")
        print("[3] - 3 pontos")
        p2 = int(input("Quantos pontos fez? "))
        while(p2 != 1 and p2 != 2 and p2 != 3):
            print("[1] - 1 ponto")
            print("[2] - 2 pontos")
            print("[3] - 3 pontos")
            p2 = int(input("Quantos pontos fez? "))
        if(p == 1):
            time = 'casa'
        else:
            time = 'visitante'
        adcPonto(partida, time, p2)
        p3 = input("Deseja continuar? [S/N]: ").upper()
        while(p3 != 'S' and p3 != 'N'):
            p3 = input("Deseja continuar? [S/N]: ").upper()
        if(p3 == 'S'):
            pass
        else:
            break
    verificarPontos(casa, visitante)

partida = {'casa':0, 'visitante':0}

placar(partida)
