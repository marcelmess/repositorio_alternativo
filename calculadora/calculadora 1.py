from tkinter import *

cor1="#090f13"
cor2="#c90a02"
cor3="#171f25"
cor4="#752e2b"
cor5="#92b55f"
cor6="#f0f2dc"
corbranca="#ffffff"

janela =Tk()
janela.title("Calculadora do Marcel")
janela.geometry("408x526")
janela.resizable(False, False)

frame_tela = Frame(janela, width=408, height=100, bg=cor1)
frame_tela.grid(row=0, column=0)


frame_corpo = Frame(janela, width=408, height=426, bg=cor1)
frame_corpo.grid(row=1, column=0)

valor_texto = StringVar()

resultado = ""


def resultados(event):
    global resultado
    resultado= str(resultado) + str(event)
    valor_texto.set(resultado)

def limpar():
    global resultado
    resultado = ""
    valor_texto.set("")

def calcular():
    global resultado
    resultado = eval(resultado)
    valor_texto.set(str(resultado))

#tela

tela = Label(frame_tela, textvariable=valor_texto, width=23, height=3, padx=20, relief=FLAT, anchor="e", justify=RIGHT, font="Verdana 20 bold", bg=corbranca, fg=cor1)
tela.place(x=-65, y=0)

#botões

botão_resultado= Button(frame_corpo, command= calcular, text="=", width=28, height=5, bg=cor2, fg=corbranca)
botão_resultado.place(x=205,y=341)

#operadores
botão_limpar= Button(frame_corpo, command= limpar, text="Limpar", width=28, height=5, bg=cor2, fg=corbranca)
botão_limpar.place(x=0,y=0)

botão_porcentagem= Button(frame_corpo, command= lambda: resultados("%"), text="%", width=13, height=5, bg=cor3, fg=corbranca)
botão_porcentagem.place(x=206,y=0)

botão_multiplicar= Button(frame_corpo, command= lambda: resultados("*"), text="X", width=13, height=5, bg=cor3, fg=corbranca)
botão_multiplicar.place(x=307,y=0)

botão_divisão= Button(frame_corpo, command= lambda: resultados("/"), text="/", width=13, height=5, bg=cor3, fg=corbranca)
botão_divisão.place(x=307, y=85)

botão_somar= Button(frame_corpo, command= lambda: resultados("+"), text="+", width=13, height=5, bg=cor3, fg=corbranca)
botão_somar.place(x=307,y=170)

botão_subtrair= Button(frame_corpo, command= lambda: resultados("-"), text="-", width=13, height=5, bg=cor3, fg=corbranca)
botão_subtrair.place(x=307,y=255)

#números


botão_número_1=Button(frame_corpo, command= lambda: resultados("1"), text="1", width=14, height=5, bg=cor6)
botão_número_1.place(x=-3,y=85)

botão_número_2=Button(frame_corpo, command= lambda: resultados("2"), text="2", width=13, height=5, bg=cor6)
botão_número_2.place(x=105,y=85)

botão_número_3=Button(frame_corpo, command= lambda: resultados("3"), text="3", width=13, height=5, bg=cor6)
botão_número_3.place(x=206,y=85)

botão_número_4=Button(frame_corpo, command= lambda: resultados("4"), text="4", width=14, height=5, bg=cor6)
botão_número_4.place(x=-3,y=170)

botão_número_5=Button(frame_corpo, command= lambda: resultados("5"), text="5", width=13, height=5, bg=cor6)
botão_número_5.place(x=105,y=170)

botão_número_6=Button(frame_corpo, command= lambda: resultados("6"), text="6", width=13, height=5, bg=cor6)
botão_número_6.place(x=206,y=170)

botão_número_7=Button(frame_corpo, command= lambda: resultados("7"), text="7", width=14, height=5, bg=cor6)
botão_número_7.place(x=-3,y=255)

botão_número_8=Button(frame_corpo, command= lambda: resultados("8"), text="8", width=13, height=5, bg=cor6)
botão_número_8.place(x=105,y=255)

botão_número_9=Button(frame_corpo, command= lambda: resultados("9"), text="9", width=13, height=5, bg=cor6)
botão_número_9.place(x=206,y=255)

botão_número_0=Button(frame_corpo, command= lambda: resultados("0"), text="0", width=13, height=5, bg=cor6)
botão_número_0.place(x=105,y=341)

#outros botões

botão_ponto=Button(frame_corpo, text=".", width=14, height=5, bg=cor4, fg=corbranca)
botão_ponto.place(x=-3,y=341)

janela.mainloop()
