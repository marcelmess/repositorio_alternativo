from tkinter import *
from tkinter import ttk

cor1="#4b4452" #cinza
cor2="#ff4746" #salmão
cor3="#487d76" #azul marinho
cor4="#e8da5e" #amarelo
cor5="#92b55f" #verde
cor6="#f9f6ec" #branco

janela =Tk()
janela.title("Calculadora")
janela.geometry("408x526")

frame_tela = Frame(janela, width=408, height=100, bg=cor6)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=408, height=426, bg=cor1)
frame_corpo.grid(row=1, column=0)

#botões

botão_resultado= Button(frame_corpo, text="=", width=28, height=5)
botão_resultado.place(x=205,y=341)

#operadores
botão_limpar= Button(frame_corpo, text="Limpar", width=28, height=5)
botão_limpar.place(x=0,y=0)

botão_porcentagem= Button(frame_corpo, text="%", width=13, height=5)
botão_porcentagem.place(x=206,y=0)

botão_multiplicar= Button(frame_corpo, text="x", width=13, height=5)
botão_multiplicar.place(x=307,y=0)

botão_divisão= Button(frame_corpo, text="/", width=13, height=5)
botão_divisão.place(x=307, y=85)

botão_somar= Button(frame_corpo, text="+", width=13, height=5)
botão_somar.place(x=307,y=170)

botão_subtrair= Button(frame_corpo, text="-", width=13, height=5)
botão_subtrair.place(x=307,y=255)

#números


botão_número_1=Button(frame_corpo, text="1", width=14, height=5)
botão_número_1.place(x=-3,y=85)

botão_número_2=Button(frame_corpo, text="2", width=13, height=5)
botão_número_2.place(x=105,y=85)

botão_número_3=Button(frame_corpo, text="3", width=13, height=5)
botão_número_3.place(x=206,y=85)

botão_número_4=Button(frame_corpo, text="4", width=14, height=5)
botão_número_4.place(x=-3,y=170)

botão_número_5=Button(frame_corpo, text="5", width=13, height=5)
botão_número_5.place(x=105,y=170)

botão_número_6=Button(frame_corpo, text="6", width=13, height=5)
botão_número_6.place(x=206,y=170)

botão_número_7=Button(frame_corpo, text="7", width=14, height=5)
botão_número_7.place(x=-3,y=255)

botão_número_8=Button(frame_corpo, text="8", width=13, height=5)
botão_número_8.place(x=105,y=255)

botão_número_9=Button(frame_corpo, text="9", width=13, height=5)
botão_número_9.place(x=206,y=255)

botão_número_0=Button(frame_corpo, text="0", width=13, height=5)
botão_número_0.place(x=105,y=341)

#outros botões

botão_ponto=Button(frame_corpo, text=".", width=14, height=5)
botão_ponto.place(x=-3,y=341)

janela.mainloop()