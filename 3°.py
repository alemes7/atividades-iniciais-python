import os

#Verifica se é ano bissexto ou não.

x = int(input("Digite um ano:"))

if x%4 ==0:
    print("É um ano bissexto")
else:
    print("Não é um ano bissexto")

os.system("Pause")


