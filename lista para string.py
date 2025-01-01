lista = []
while True:
    entrada = str(input("Fragmento textual: "))
    if entrada == "sair":
        break
    lista.append(entrada)
    lista.append(" ")
conversão = "".join(lista)
print(conversão)