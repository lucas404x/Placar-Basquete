from tkinter import*
from functools import partial
from tkinter import messagebox

class Placar(object):

    def __init__(self, janela, local, info = {'casa':0, 'visitante':0, 'listaPonto':[]}):


        self.janela = janela
        self.info = info
        self.local = local

        #Definindo Cor

        color_background = 'black'
        cor_widget = 'white'
        fonte = ("Arial", 30, "bold")

        self.janela['bg'] = color_background
        self.janela.resizable(False, False)

        #Labels

        lb_casa = Label(self.janela, text = "HOME", foreground = cor_widget, font = fonte, bg = color_background).place(x = 30, y = 100)
        lb_visitante = Label(self.janela, text = "GUEST", foreground = cor_widget, font = fonte, bg = color_background).place(x = 320, y = 100)
        self.lbponto_casa = Label(self.janela, text = str(self.info['casa']), font = ('Arial', 20, 'bold'), foreground = cor_widget, bg = color_background)
        self.lbponto_visitante = Label(self.janela, text = str(self.info['visitante']), font = ('Arial', 20, 'bold'), foreground = cor_widget, bg = color_background)
        lb_local = Label(self.janela, text = f"Local: {self.local}", font = ('Arial', 25, 'bold'), foreground = cor_widget, bg = color_background).place(x = 130, y = 10)
        lb_x = Label(self.janela, text = 'VS', font = fonte, foreground = cor_widget, bg = color_background).place(x = 220, y = 100)

        #Buttons

        self.bt_pontuar = Button(self.janela, text = "Pontuar", font = ('Arial', 14, 'bold'), foreground = 'black', command = partial(self.identificar_time, True))
        self.bt_voltarponto = Button(self.janela, text = "Voltar pontuação", font = ('Arial', 14, 'bold'), foreground = 'black', command = partial(self.voltarPonto, True))
        self.bt_finalizar = Button(self.janela, text = "Finalizar", font = ('Arial', 14, 'bold'), foreground = 'black', command = partial(self.finalizar, True))

        #Empacotamento

        self.lbponto_casa.place(x = 82, y = 160)
        self.lbponto_visitante.place(x = 372, y = 160)
        self.bt_pontuar.place(x = 150, y = 300, width = 200)
        self.bt_voltarponto.place(x = 150, y = 350, width = 200)
        self.bt_finalizar.place(x = 150, y = 400, width = 200)


    def identificar_time(self, click):

        if click is True:

            #Destruindo os botões

            self.bt_pontuar.destroy()
            self.bt_voltarponto.destroy()
            self.bt_finalizar.destroy()

            #Criando os CheckButtons e o Label

            self.cbt1 = Checkbutton(self.janela, bg = "black", command = partial(self.identificar_ponto, "casa", True))
            self.cbt2 = Checkbutton(self.janela, bg = "black", command = partial(self.identificar_ponto, "visitante", True))
            self.lb = Label(self.janela, text = "Selecione um time", bg = "black", font = ("Arial", 14, "bold"), foreground = "white")

            #Empacotando

            self.cbt1.place(x = 81, y = 200)
            self.cbt2.place(x = 371, y = 200)
            self.lb.place(x = 160, y = 220)

    def identificar_ponto(self, time, click):

        if click is True:

            #Alterando o Label
            self.time = time
            self.lb['text'] = "Quantos pontos?"
            self.lb.place(x = 160, y = 220)

            #Criando os CheckButtons

            self.cbt3 = Checkbutton(self.janela, text = "1 ponto", font = ("Arial", 14, 'bold'), bg = 'black', foreground = 'white', command = partial(self.addPonto, 1, True))
            self.cbt4 = Checkbutton(self.janela, text = "2 pontos", font = ("Arial", 14, 'bold'), bg = 'black', foreground = 'white', command = partial(self.addPonto, 2, True))
            self.cbt5 = Checkbutton(self.janela, text = "3 pontos", font = ("Arial", 14, 'bold'), bg = 'black', foreground = 'white', command = partial(self.addPonto, 3, True))

            #Empacotando

            self.cbt3.place(x =  80, y = 340)
            self.cbt4.place(x =  200, y = 340)
            self.cbt5.place(x =  320, y = 340)

    def addPonto(self, ponto, click):

        if click is True:

            self.info[self.time] += ponto
            self.info['listaPonto'].append({self.time:ponto})

            self.lb.destroy()
            self.cbt1.destroy()
            self.cbt2.destroy()
            self.cbt3.destroy()
            self.cbt4.destroy()
            self.cbt5.destroy()

            self.__init__(self.janela, self.local)

    def voltarPonto(self, click):

        if click is True:

            if len(self.info['listaPonto']) == 0:

                 erro = messagebox.showinfo("", "Você não adicionou nenhuma pontuação a base de pontos.")

            else:

                ultimoPonto = len(self.info['listaPonto']) - 1

                for i in self.info['listaPonto'][ultimoPonto].keys():

                    self.time = i

                for i in self.info['listaPonto'][ultimoPonto].values():

                    self.ponto = i

                self.info[self.time] -= self.ponto
                
                if self.time == 'casa':

                    self.lbponto_casa['text'] = self.info[self.time]

                else:

                    self.lbponto_visitante['text'] = self.info[self.time]
                    
                self.info['listaPonto'].pop() 

    def finalizar(self, click):

        if click is True:

            if self.info['casa'] > self.info['visitante']:

                venceu = messagebox.showinfo("", "O time da Casa venceu!")

            elif self.info['casa'] < self.info['visitante']:

                venceu = messagebox.showinfo("", "O time dos Visitantes venceram!")

            else:

                empate = messagebox.showinfo("", "Empate!")

            self.info['casa'] = 0
            self.info['visitante'] = 0
            self.lbponto_casa['text'] = self.info['casa']
            self.lbponto_visitante['text'] = self.info['visitante']
            self.info['listaPonto'] = []

janela = Tk()
Placar(janela, "Cajueiro")
janela.title("Placar de Basquete")
janela.geometry("500x500")
janela.mainloop()
