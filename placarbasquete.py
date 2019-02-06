from tkinter import*
from functools import partial

class Placar(object):

    def __init__(self, janela, local, info = {'casa':0, 'visitante':0, 'listaPonto':[]}, pontos = None):

        self.janela = janela
        self.info = info
        self.local = local
        self.pontos = pontos

        #Definindo Cor

        color_background = 'black'
        cor_widget = 'white'
        fonte = ("Arial", 30, "bold")

        self.janela['bg'] = color_background
        self.janela.resizable(False, False)

        #Labels
        
        lb_casa = Label(self.janela, text = "HOME", foreground = cor_widget, font = fonte, bg = color_background).place(x = 30, y = 100)
        lb_visitante = Label(self.janela, text = "GUEST", foreground = cor_widget, font = fonte, bg = color_background).place(x = 320, y = 100)
        lbponto_casa = Label(self.janela, text = str(self.info['casa']), font = ('Arial', 20, 'bold'), foreground = cor_widget, bg = color_background).place(x = 82, y = 160)
        lbponto_visitante = Label(self.janela, text = str(self.info['visitante']), font = ('Arial', 20, 'bold'), foreground = cor_widget, bg = color_background).place(x = 372, y = 160)
        lb_local = Label(self.janela, text = f"LOCAL: {self.local}", font = ('Arial', 25, 'bold'), foreground = cor_widget, bg = color_background).place(x = 100, y = 10)
        lb_x = Label(self.janela, text = 'VS', font = fonte, foreground = cor_widget, bg = color_background).place(x = 220, y = 100)

        #Buttons

        self.bt_pontuar = Button(self.janela, text = "Pontuar", font = ('Arial', 14, 'bold'), foreground = 'black', command = partial(self.addPonto, True)).place(x = 150, y = 300, width = 200)
        self.bt_voltarponto = Button(self.janela, text = "Voltar pontuação", font = ('Arial', 14, 'bold'), foreground = 'black').place(x = 150, y = 350, width = 200)
        self.bt_sair = Button(self.janela, text = "Finalizar", font = ('Arial', 14, 'bold'), foreground = 'black').place(x = 150, y = 400, width = 200)

    def addPonto(self, click):

        if click is True:

            self.mb = Menubutton(self.janela, text = "Qual time pontuar?\nClique aqui", bg = 'black', foreground = 'white')
            self.mb.menu = Menu(self.mb)
            self.mb['menu'] = self.mb.menu
            self.mb.menu.add_command(label = "HOME", command = partial(self.identificar_time, "casa"))
            self.mb.menu.add_command(label = "GUEST", command = partial(self.identificar_time, "visitante"))
            self.mb.place(x = 190, y = 230)
            
    def identificar_time(self, time):
        pass
    
janela = Tk()
Placar(janela, "CAJUEIRO")
janela.title("Placar de Basquete")
janela.geometry("500x500")
janela.mainloop()
