from tkinter import *

def apertousim():
    print('voce apertou o botao sim')

def apertounao():
    print('voce apertou o botao nao')
    
quantsim = IntVar()
quantsim.set(0)
quantnao = IntVar()
quantnao.set(0)


app = Tk()
app.title("Janela em Python")
app.geometry('1000x700+0+0')

rotulo = Label(app, text ='faca sua escolha')
rotulo.pack(pady = 100)

lab1 = Label = (app, textVariable = quantsim)
lab1.pack(side ="left")

lab2 = Label =( app, textVariable = quantnao)
lab2.pack(side = "right")

b1 = Button(app,text = "Sim", width = 10, command = apertousim)
b1.pack(side = "left",padx = 10 , pady = 10)

b2 = Button (app,text = "Não", width = 10, command = apertounao)
b2. pack(side = "right",padx =10 , pady = 10)


app.mainloop()
