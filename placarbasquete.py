class placarBasquete:

    def __init__(self, casa = 0, visitante = 0, listaPonto = []):

        self.listaPonto = listaPonto
        self.casa = casa
        self.visitante = visitante

    def addPonto(self, ponto, time):

        if(time == "Casa"):
            self.casa += ponto
            aux = {time:ponto}
        else:
            self.visitante += ponto
            aux = {time:ponto}
        self.listaPonto.append(aux)

    def voltarPonto(self):

        posicaoTime = len(self.listaPonto) - 1

        for i in self.listaPonto[posicaoTime].keys():
            time = i
        for i in self.listaPonto[posicaoTime].values():
            valor = i
        if(time == "Visitante"):
            self.visitante = self.visitante - valor
        else:
            self.casa = self.casa - valor
        self.listaPonto.pop()


    def imprimirPlacar(self):
        print()
        print("               PLACAR                        ")
        print()
        print(f"Casa: {self.casa}          X          Visitantes: {self.visitante}")
        print()

def main(placarBasquete):

    placar = placarBasquete()
    opcao = -1
    while(opcao != 4):
        print()
        print("[1] - Pontuar")
        print("[2] - Voltar pontuação")
        print("[3] - Visualizar o placar")
        print("[4] - Sair")
        print()
        opcao = int(input("O que deseja fazer? "))
        while(opcao < 1 and opcao > 4):
            opcao = int(input("O que deseja fazer? "))
        if(opcao == 1):
            pontuarTime(placar)
        elif(opcao == 2):
            placar.voltarPonto()
        elif(opcao == 3):
            placar.imprimirPlacar()
        elif(opcao == 4):
            resultadoFinal(placar)

def pontuarTime(placar):

    placar.imprimirPlacar()
    print("[1] - Casa")
    print("[2] - Visitante")
    print()
    opcao = int(input("Qual time deseja pontuar? "))
    print()
    print("[1] - 1 ponto")
    print("[2] - 2 pontos")
    print("[3] - 3 pontos")
    print()
    ponto = int(input("Quantos pontos? "))
    while(ponto < 1 and ponto > 3):
        ponto = int(input("Quantos pontos? "))
    if(opcao == 1):
        placar.addPonto(ponto, "Casa")
    else:
        placar.addPonto(ponto, "Visitante")

def resultadoFinal(placar):
    if(placar.casa > placar.visitante):
        print()
        print("Vitória para o time da Casa!")
        print()
    elif(placar.casa < placar.visitante):
        print()
        print("Vitória para o time dos Vistantes!")
        print()
    else:
        print()
        print("Empate!")
        print()
    placar.imprimirPlacar()

main(placarBasquete)
