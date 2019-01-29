class placarBasquete:

    def __init__(self, casa = 0, visitante = 0, listaPonto = []):

        self.listaPonto = listaPonto
        self.casa = casa
        self.visitante = visitante

    def addPonto(self, ponto, time):

        if(time == "Casa"):
            self.casa += ponto
            aux = {time:self.casa}
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
        print(time)
        print(valor)
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

placar = placarBasquete()
