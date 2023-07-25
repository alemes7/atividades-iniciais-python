import os

s = 1

while s == 1:
        #Programa que verifica se um número é par ou ímpar.

    x = int(input("Escolha um número:"))

    if x%2 == 0:
        print("Par")
    else:
        print("Ímpar")
    
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
    
