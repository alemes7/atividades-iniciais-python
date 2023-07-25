import os

#Programa que verifica a categoria de um nadador de acordo com a idade(Infantil A, Infantil B, Juvenil A, Juvenil B, Adulto)

x = int(input("Indique a idade do nadador:"))

a= 8
B= 12
c= 16
d= 22
e= 30

if x <= 8:
    print("Infantil A")
elif x > 8 and x <= 12:
    print("Infantil B")
elif x > 12 and x <= 16:
    print("Juvenil A")
elif x > 16 and x <= 22:
    print("Juvenil B")
elif x > 22 and x <= 40:
    print("Adulto")
else:
    print("Não tem atletas dessa idade")

os.system("pause") 