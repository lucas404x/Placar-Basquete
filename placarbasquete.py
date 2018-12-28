def verificarPontos(casa, visitante):

    print()
    if(casa > visitante):
        print("Time da Casa venceu o jogo!")
    elif(casa < visitante):
        print("Time dos Visitantes venceram o jogo!")
    else:
        print("Empate!")
    
def mostrarPlacar(casa, visitante):

    print()
    print("                 PLACAR                    ")
    print()
    print("Casa: " + str(casa) + "                    " + "Visitantes: " + str(visitante))
    print()

def pontosAdc(casa, visitante):

    while True:
        mostrarPlacar(casa, visitante)
        p = int(input("[1] - Casa\n[2] - Visitante\nQuem fez o ponto? "))
        while(p != 1 and p != 2):
            p = int(input("[1] - Casa\n[2] - Visitante\nQuem fez o ponto? "))
        p2 = int(input("[1] - 1 ponto\n[2] - 2 pontos\n[3] - pontos\nQuantos pontos fez? "))
        while(p2 != 1 and p2 != 2 and p2 != 3):
            p2 = int(input("[1] - 1 ponto\n[2] - 2 pontos\n[3] - pontos\nQuantos pontos fez? "))
        if(p == 1):
            casa += p2
        else:
            visitante += p2
        p3 = input("Deseja continuar? [S/N]: ").upper()
        while(p3 != 'S' and p3 != 'N'):
            p3 = input("Deseja continuar? [S/N]: ").upper()
        if(p3 == 'S'):
            pass
        else:
            break
    verificarPontos(casa, visitante)

casa = 0
visitante = 0

pontosAdc(casa, visitante)
