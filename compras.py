import os 

s = 1

while s == 1:

    x = int(input("Informe o produto que deseja:"))

    if (x==1):
        print("Arroz, R$10,00")
    elif (x==2):
        print("Feijão, R$20,00")
    elif (x==3):
        print("Macarrão, R$30,00")
    elif (x==4):
        print("Carne, R$40,00")
    elif (x==5):
        print("Açucar, R$50,00")
    else:
        print("Produto solicitado não existe.")
    
    y = int(input("Se quiser sair, digite 1:"))

    if y == 1:
        s == 0
    

    
