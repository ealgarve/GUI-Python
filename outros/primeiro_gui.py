from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master) # criado conteiner widget1 e referenciado como pai
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack(side=TOP)
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique Aqui" # self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.mudaTexto) # self.sair["command"] =self.widget1.quit
        self.sair.pack(side=TOP)

    def mudaTexto(self, event):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"

root = Tk()
Application(root)
root.mainloop()