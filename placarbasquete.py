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
        lbponto_casa = Label(self.janela, text = str(self.info['casa']), font = ('Arial', 20, 'bold'), foreground = cor_widget, bg = color_background)
        lbponto_visitante = Label(self.janela, text = str(self.info['visitante']), font = ('Arial', 20, 'bold'), foreground = cor_widget, bg = color_background)
        lb_local = Label(self.janela, text = f"Local: {self.local}", font = ('Arial', 25, 'bold'), foreground = cor_widget, bg = color_background).place(x = 130, y = 10)
        lb_x = Label(self.janela, text = 'VS', font = fonte, foreground = cor_widget, bg = color_background).place(x = 220, y = 100)

        #Buttons

        self.bt_pontuar = Button(self.janela, text = "Pontuar", font = ('Arial', 14, 'bold'), foreground = 'black', command = partial(self.identificar_time, True)).place(x = 150, y = 300, width = 200)
        self.bt_voltarponto = Button(self.janela, text = "Voltar pontuação", font = ('Arial', 14, 'bold'), foreground = 'black', command = partial(self.voltarPonto, True)).place(x = 150, y = 350, width = 200)
        self.bt_sair = Button(self.janela, text = "Finalizar", font = ('Arial', 14, 'bold'), foreground = 'black').place(x = 150, y = 400, width = 200)

        #Empacotamento

        lbponto_casa.place(x = 82, y = 160)
        lbponto_visitante.place(x = 372, y = 160)
        
        
    def identificar_time(self, click):

        if click is True:

            self.mb = Menubutton(self.janela, text = "Qual time você quer pontuar?\nClique aqui", bg = 'black', foreground = 'white')
            self.mb.menu = Menu(self.mb)
            self.mb['menu'] = self.mb.menu
            self.mb.menu.add_command(label = "HOME", command = partial(self.identificar_ponto, "casa", True))
            self.mb.menu.add_command(label = "GUEST", command = partial(self.identificar_ponto, "visitante", True))
            self.mb.place(x = 175, y = 230)
            
    def identificar_ponto(self, time, click):
            
        if click is True:

            self.time = time
            self.mb['text'] = "Quantos pontos?"
            self.mb.menu.delete('HOME')
            self.mb.menu.delete('GUEST')
            self.mb.menu.add_command(label = "1 ponto", command = partial(self.addPonto, 1, True))
            self.mb.menu.add_command(label = "2 pontos", command = partial(self.addPonto, 2, True))
            self.mb.menu.add_command(label = "3 pontos", command = partial(self.addPonto, 3, True))
            
    def addPonto(self, ponto, click):

        if click is True:
            
            self.info[self.time] += ponto
            self.info['listaPonto'].append({self.time:ponto})
            self.mb.menu.destroy()
            self.mb.destroy()
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
                self.info['listaPonto'].pop()
                self.__init__(self.janela, self.local)
    
janela = Tk()
Placar(janela, "Cajueiro")
janela.title("Placar de Basquete")
janela.geometry("500x500")
janela.mainloop()
