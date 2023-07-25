import os #para abrir uma biblioteca
s = 0 

t = int(input("Digite um número:"))#sequencia de números

while t >= 0:
    print(t)
    t = t -1 #ele vai diminuindo o valor inserido pelo usúario por 1 até chegar em N. 
while s == 0: #while para ficar repetindo e não sair.
    x = int(input("Por favor, digite um valor para o software identificar se é divisível por 3 ou 5:"))
    if x%3==0: #utilizei o if para o software saber se o número inserido pelo usuario é divisível ou não.
        print("Senai")
    elif x%5==0: # a % foi usada para dividir o valor
        print("Jundiaí")
    elif x%3==0 and x%5==0:
        print("SenaiJundiai")
    else:
        print(x) #se não for divisivel por 3,5 ou 3 e 5, ele tem que inserir o número que o usuario colocou.
os.system("pause")

#outra forma

n = int(input("Digite um número inteiro positivo: "))

for i in range(1, n+1):
    if 1 % 3 == 0 and i % 5 == 0:
        print("SenaiJundiai")
    elif i % 3 == 0:
        print("Senai")
    elif i % 5 == 0:
        print("Jundiai")
    else:
        print(i)
