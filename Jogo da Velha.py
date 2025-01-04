while True:
    plataforma1 = [" 1  ", "|", " 2  ", "|", " 3  "]
    linha1 = ["----|----|----"]
    plataforma2 = [" 4  ", "|", " 5  ", "|", " 6  "]
    linha2 = ["----|----|----"]
    plataforma3 = [" 7  ", "|", " 8  ", "|", " 9  "]
    string1 = "".join(plataforma1)
    string2 = "".join(linha1)
    string3 = "".join(plataforma2)
    string4 = "".join(linha2)
    string5 = "".join(plataforma3)
    contador = True
    jogar = False

    jogar_entrada = str(input("Digite 'jogar' para iniciar o Jogo da Velha: ").lower())
    if jogar_entrada == "jogar":
        jogar = True
        print("Digite o número correspondente do bloco que você deseja marcar")
        print(string1)
        print(string2)
        print(string3)
        print(string4)
        print(string5)
    else:
        print("Você encerrou o programa.")
    while jogar == True:
        if (
                (plataforma1[0] == " X  " and plataforma1[2] == " X  " and plataforma1[4] == " X  ") or
                (plataforma2[0] == " X  " and plataforma2[2] == " X  " and plataforma2[4] == " X  ") or
                (plataforma3[0] == " X  " and plataforma3[2] == " X  " and plataforma3[4] == " X  ") or
                (plataforma1[0] == " X  " and plataforma2[0] == " X  " and plataforma3[0] == " X  ") or
                (plataforma1[2] == " X  " and plataforma2[2] == " X  " and plataforma3[2] == " X  ") or
                (plataforma1[4] == " X  " and plataforma2[4] == " X  " and plataforma3[4] == " X  ") or
                (plataforma1[0] == " X  " and plataforma2[2] == " X  " and plataforma3[4] == " X  ") or
                (plataforma1[4] == " X  " and plataforma2[2] == " X  " and plataforma3[0] == " X  ")
        ):
            print("O primeiro jogador ganhou!")
            jogar = False
            break
        elif (
                (plataforma1[0] == " O  " and plataforma1[2] == " O  " and plataforma1[4] == " O  ") or
                (plataforma2[0] == " O  " and plataforma2[2] == " O  " and plataforma2[4] == " O  ") or
                (plataforma3[0] == " O  " and plataforma3[2] == " O  " and plataforma3[4] == " O  ") or
                (plataforma1[0] == " O  " and plataforma2[0] == " O  " and plataforma3[0] == " O  ") or
                (plataforma1[2] == " O  " and plataforma2[2] == " O  " and plataforma3[2] == " O  ") or
                (plataforma1[4] == " O  " and plataforma2[4] == " O  " and plataforma3[4] == " O  ") or
                (plataforma1[0] == " O  " and plataforma2[2] == " O  " and plataforma3[4] == " O  ") or
                (plataforma1[4] == " O  " and plataforma2[2] == " O  " and plataforma3[0] == " O  ")
        ):
            print("O segundo jogador ganhou!")
            jogar = False
            break
        else:
            entrada = int(input("Números de 1 a 9: "))
            if entrada == 1:
                if contador:
                    plataforma1[0]= " X  "
                    contador = False
                else:
                    plataforma1[0]= " O  "
                    contador = True
                print(contador)
                string1 = "".join(plataforma1)
                print(string1)
                print(string2)
                print(string3)
                print(string4)
                print(string5)
            elif entrada == 2:
                if contador:
                    plataforma1[2] = " X  "
                    contador = False
                else:
                    plataforma1[2] = " O  "
                    contador = True
                string1 = "".join(plataforma1)
                print(contador)
                print(string1)
                print(string2)
                print(string3)
                print(string4)
                print(string5)
            if entrada == 3:
                if contador:
                    plataforma1[4] = " X  "
                    contador = False
                else:
                    plataforma1[4] = " O  "
                    contador = True
                string1 = "".join(plataforma1)
                print(string1)
                print(string2)
                print(string3)
                print(string4)
                print(string5)
            if entrada == 4:
                if contador:
                    plataforma2[0] = " X  "
                    contador = False
                else:
                    plataforma2[0] = " O  "
                    contador = True
                string3 = "".join(plataforma2)
                print(string1)
                print(string2)
                print(string3)
                print(string4)
                print(string5)
            if entrada == 5:
                if contador:
                    plataforma2[2] = " X  "
                    contador = False
                else:
                    plataforma2[2] = " O  "
                    contador = True
                string3 = "".join(plataforma2)
                print(string1)
                print(string2)
                print(string3)
                print(string4)
                print(string5)
            if entrada == 6:
                if contador:
                    plataforma2[4] = " X  "
                    contador = False
                else:
                    plataforma2[4] = " O  "
                    contador = True
                string3 = "".join(plataforma2)
                print(string1)
                print(string2)
                print(string3)
                print(string4)
                print(string5)
            if entrada == 7:
                if contador:
                    plataforma3[0] = " X  "
                    contador = False
                else:
                    plataforma3[0] = " O  "
                    contador = True
                string5 = "".join(plataforma3)
                print(string1)
                print(string2)
                print(string3)
                print(string4)
                print(string5)
            if entrada == 8:
                if contador:
                    plataforma3[2] = " X  "
                    contador = False
                else:
                    plataforma3[2] = " O  "
                    contador = True
                string5 = "".join(plataforma3)
                print(string1)
                print(string2)
                print(string3)
                print(string4)
                print(string5)
            if entrada == 9:
                if contador:
                    plataforma3[4] = " X  "
                    contador = False
                else:
                    plataforma3[4] = " O  "
                    contador = True
                string5 = "".join(plataforma3)
                print(string1)
                print(string2)
                print(string3)
                print(string4)
                print(string5)