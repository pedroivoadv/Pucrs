#aula 1 dinamica 1

num = int(input("Informe um número natural: "))

cont = 0
d = 1
while d<=num:
    if num % d == 0 : cont = cont + 1
    d = d + 1
if cont == 2: print(num, "é primo")
else : print(num, "não é primo")
    
