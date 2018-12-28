def placarBasquete(partida):
    
    pontuacao = []
    times = []
    
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
            pontuar(partida, pontuacao, times)
        elif(opcao == 2):
            voltarPonto(pontuacao, times)
        else:
            verificarPontos(partida)
            break

def voltarPonto(pontuacao, times):
    
    print(pontuacao)
    print(times)

def adcPonto(partida, time, p2, pontuacao, times):
    
    partida[time] += p2
    
    pontuacao.append(p2)
    times.append(time)

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
    print("                     PLACAR                    ")
    print()
    print(f"Casa: {str(partida['casa'])}                                   Visitantes: {str(partida['visitante'])}")
    print()

def pontuar(partida, pontuacao, times):
    
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
    adcPonto(partida, time, p2, pontuacao, times)

partida = {'casa':0, 'visitante':0}

placarBasquete(partida)
