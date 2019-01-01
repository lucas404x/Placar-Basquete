import os
def clear():
    os.system('cls')

def placarBasquete(partida):
    opcao = -1
    while(opcao != 3):
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
        elif(opcao == 3):
            verificarPontos(partida)


def voltarPonto(partida):
    qnt = len(partida['historico'])
    print(partida)
    if(qnt < 1):
        print("Não há registro de pontuação.")
    elif(qnt == 1):
        partida['placar']['casa'] = 0
        partida['placar']['visitante'] = 0
        partida['historico'].pop()
        partida['marcatimeponto'].pop()
    else:
        marcatime = partida['marcatimeponto'][len(partida['marcatimeponto']) - 1]
        for t in marcatime.keys():
            time = t
            print(time)
        for v in marcatime.values():
            valor = v
        print(time)
        print(valor)
        partida['placar'][time] = partida['placar'][time] - valor
        partida['historico'].pop()
        partida['marcatimeponto'].pop()
        print(partida)


def adcPonto(partida, time, ponto):
    print(partida)
    partida["placar"][time] += ponto
    casa = partida['placar']['casa']
    visitante = partida['placar']['visitante']
    add = {"casa": casa, "visitante":visitante}
    aux = {time:ponto}
    partida['historico'].append(add)
    partida['marcatimeponto'].append(aux)
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
    #clear()
    print()
    print("                     PLACAR                    ")
    print()
    print(f"Casa: {str(partida['placar']['casa'])}                                   Visitantes: {str(partida['placar']['visitante'])}")
    print()

def pontuar(partida):
    print("[1] - Casa")
    print("[2] - Visitante")
    pergunta = int(input("Quem fez o ponto? "))
    while(pergunta != 1 and pergunta != 2):
        print("[1] - Casa")
        print("[2] - Visitante")
        pergunta = int(input("Quem fez o ponto? "))
    print("[1] - 1 ponto")
    print("[2] - 2 pontos")
    print("[3] - 3 pontos")
    ponto = int(input("Quantos pontos fez? "))
    while(ponto != 1 and ponto != 2 and ponto != 3):
        print("[1] - 1 ponto")
        print("[2] - 2 pontos")
        print("[3] - 3 pontos")
        ponto = int(input("Quantos pontos fez? "))
    if(pergunta == 1):
        time = 'casa'
    else:
        time = 'visitante'
    adcPonto(partida, time, ponto)

partida = {"placar":{'casa':0, 'visitante':0}, "historico":[], "marcatimeponto":[]}

placarBasquete(partida)
