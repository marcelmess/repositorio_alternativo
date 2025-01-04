while True:
    def soma(a,b):
        return(a+b)
    def subtração (a,b):
        return(a-b)
    def multiplicação(a,b):
        return(a*b)
    def divisão(a,b):
        return(a/b)

    entrada1 = int(input("Digite o primeiro número:\n"))
    operação1 = str(input("Insira o nome da operação que você deseja realizar.\nAs opções são: (soma, subtração, multiplicação e divisão)\n"))
    entrada2 = int(input("Digite o segundo número:\n"))

    if operação1 == "soma":
        print(soma(entrada1, entrada2))
    elif operação1 == "subtração":
        print(subtração(entrada1, entrada2))
    elif operação1 == "multiplicação":
        print(multiplicação(entrada1, entrada2))
    elif operação1 == "divisão":
        print(divisão(entrada1, entrada2))
    else:
        print("Operação inválida. Tente novamente.")