import os
s = 1

while s == 1:

    x=int(input("Digite um valor para contagem regressiva:"))


    while x >= 0:
        print(x)
        x = x -1

    sim = "y"
    não = "n"

    if s == 1:
        print("Deseja sair?")
        print(" sim - y ")
        print(" não - n ")

        z=(input(" "))

    if z == sim:
        s = 0
    elif z == não:
        S = 1
    else:
        print(" ")
        print("Código invalido")
        print(" ")
    
        