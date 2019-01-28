class time:

    def __init__(self, casa = 0, visitante = 0, listaPonto = {'time':[], 'ponto':[]}):

        self.listaPonto = listaPonto
        self.casa = casa
        self.visitante = visitante

    def addPonto(self, ponto, time):

        if(time == "Casa"):

            self.casa += ponto

        else:

            self.visitante += ponto

        self.listaPonto['ponto'].append(ponto)
        self.listaPonto['time'].append(time)
    
    def voltarPonto(self):

        self.listaPonto['ponto'].pop()
        pontoAnterior = len(self.listaPonto['ponto']) - 1
        timePonto = len(self.listaPonto['time']) - 1
        if(timePonto == "Casa"):
            self.casa = self.listaPonto['ponto'][pontoAnterior]
        else:
            self.visitante = self.listaPonto['ponto'][pontoAnterior]
        

class placar(time):
    
    def imprimirPlacar(self):
        print()
        print("               PLACAR                        ")
        print()
        print(f"Casa: {self.casa}          X          Visitantes: {self.visitante}")
        print()

placar = placar()
