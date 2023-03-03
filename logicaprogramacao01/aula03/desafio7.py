import math
a = float(input('Informe o valor do a: '))
b = float(input('Informe o valor do b: '))
c = float(input('Informe o valor do c: '))

delta = math.pow(b,2) - 4 * a * c
if delta<0 or a==0 : print('Erro. Delta negativo ou divisão por 0')
else: 
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print('x1: ', x1)
    print('x2: ', x2)
