'''
Essa é uma calculadora simples de 4 operações. 
Escolha qual operação você deseja realizar.
Você deseja realizar outra operação?
Sim - y
Não - n
se sim, print escolha qual operação deseja realizar
se não: Você deseja sair?
Sim - y
Não - n
'''

import os

# Nesse trecho, utilizamos o comando "print" para as mensagens iniciais de nossa calculadora serem exibidas na tela

print("Essa é uma calculadora simples de 4 operações:")
print("- Adição +")
print("- Subtração -")
print("- Multiplicação *")
print("- Divisão /")
print(" ")

# Utilizamos o "while" para fazer com que nossa calculadora funcione continuamente

w = 1

while w == 1:

# Nesse trecho selecionamos as variáveis de cada operação

    Adição = "a"
    Subtração = "s"
    Multiplicação = "m"
    Divisão = "d"

# Utilizamos o "print" e o "input" para o usuário escolher qual operação deseja realizar

    print("Qual operação você deseja realizar?")
    print("Adição = a")
    print("Subtração = s")
    print("Multiplicação = m")
    print("Divisão = d")
    print(" ")
    
    z = input(" ")

    print(" ")

# Utilizamos novamente o "input" para após o usuário selecionar qual operação deseja realizar, ele poder digitar os números que deseja operacionar
# O "float" foi utilizado para ser possivel realizar operações com números decimais

    x = float(input("Digite o 1° valor que deseja realizar a operação: "))
    b = float(input("Digite o 2° valor que deseja realizar a operação: "))

# Selecionamos uma váriavel para cada opção de operação que o usuário resolvesse utilizar 

    g = (x + b)
    h = (x - b)
    i = (x * b)
    j = (x / b)

# Nesse trecho utilizamos "if", "elif" e "else" para cada opração que fosse realizada

    if z == Adição:
        print(f"A soma será: {x} + {b}")
        print(f"O resultado será: {g}")
    elif z == Subtração:
        print(f"A subtração será: {x} - {b}")
        print(f"O resultado será: {h}")
    elif z == Multiplicação:
        print(f"A multiplicação será: {x} * {b}")
        print(f"O resultado será: {i}")
    elif z == Divisão:
        print(f"A divisão será: {x} / {b}")
        print(f"O resultado será: {j}")
    else:
        print("Operação solicitada não pode ser efetuada.")

# Para finalizar usamos o "while", "if", "elif" e "else" para mandar as mensagens finais.


    sim = "y"
    não = "n"

    if w == 1:
        print("Você deseja realizar outra operação?")
        print("Sim = y")
        print("Não = n")

    c = (input(" "))

            
    if c == sim:
        w = 1
    elif c == não:
        w = 0
    else:
        print(" ")
        print("Opção Inválida")
        print(" ")

    while w == 0:

            if w == 0:
                print("Você deseja sair?")
                print("Sim = y")
                print("Não = n")

            c = (input(" "))

                    
            if c == sim:
                w = 2
            elif c == não:
                w = 1
            else:
                print(" ")
                print("Opção Inválida")
                print(" ")
