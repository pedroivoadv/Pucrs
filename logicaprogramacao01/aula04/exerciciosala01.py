#aula 4.1
#cálculo de raizes de eq. quadrática
import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = b * b - 4* a * c

if delta < 0:
    print("Não há raízes reais")
else: 
    if delta == 0:
        x = -b/(2*a)
        print(f"Raiz é {x}")
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(f"Raízes são {x1} e {x2}")

