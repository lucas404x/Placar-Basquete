def placarBasquete(partida):
        
    while True:

        mostrarPlacar(partida)

        print()
        print('[1] - Pontuar')
        print('[2] - Voltar pontuação')
        print('[3] - Sair')
        print()

        opcao = int(input("O que você deseja fazer? "))
        
        while(opcao != 1 and opcao != 2 and opcao != 3):
            opcao = int(input("O que você deseja fazer? "))
        if(opcao == 1):
            pontuar(partida)
        elif(opcao == 2):
            voltarPonto(partida)
        else:
            verificarPontos(partida)
            break

def voltarPonto(partida):

    qnt = len(partida['historico'])
    print(partida)

    if(qnt == 1):
        print("Não há registro de pontuação.")

    else:
        cont = 0

        if(partida['historico'][qnt - 1]['casa'] != partida['historico'][qnt - 2]['casa']):
            cont += 1
        elif(partida['historico'][qnt - 1]['visitante'] != partida['historico'][qnt - 2]['visitante']):
            pass

        if(cont == 1):
            time = 'casa'
        else:
            time = 'visitante'

        print(time)
        partida['historico'].pop(qnt - 1)
        print(partida)


def adcPonto(partida, time, p2):

    print(partida)

    partida["placar"][time] += p2

    add = f"Casa: {partida['placar']['casa']}, Visitantes: {partida['placar']['visitante']}"

    partida['historico'].append(add)

    print(partida)

def verificarPontos(partida):

    print()
    if(partida['placar']['casa'] > partida['placar']['visitante']):
        print("Time da Casa venceu o jogo!")
    elif(partida['placar']['casa'] < partida['placar']['visitante']):
        print("Time dos Visitantes venceram o jogo!")
    else:
        print("Empate!")
    
def mostrarPlacar(partida):

    print()
    print("                     PLACAR                    ")
    print()
    print(f"Casa: {str(partida['placar']['casa'])}                                   Visitantes: {str(partida['placar']['visitante'])}")
    print()

def pontuar(partida):
    
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

partida = {"placar":{'casa':0, 'visitante':0}, "historico":[]}

placarBasquete(partida)
