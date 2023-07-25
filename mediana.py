A = int(input("Informe o 1° valor de sua mediana: ")) 
B = int(input("Informe o 2° valor de sua mediana: ")) 
C = int(input("Informe o 3° valor de sua mediana: "))

if A > B and A > C:
            MAX1 = A
            if B > C:
                print(f"A mediana é: {B}")
            else:
                print(f"A mediana é: {C}")
if B > A and B > C:
            MAX1 = B
            if A > C:
                print(f"A mediana é: {A}")
            else:
                print(f"A mediana é: {C}")
if C > A and C > B:
            MAX1 = C 
            if A > B:
                print(f"A mediana é: {A}")
            else:
                print(f"A mediana é: {B}")