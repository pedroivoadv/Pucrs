
nTermos = int(input("informea quantidade de termos: "))
if nTermos <=0 : print('Numero de termos invalido.')
else:
    soma = 0
    cont = 1
    while cont <= nTermos:
        soma = soma + 1/cont
        cont = cont + 1
    print("Soma: ", soma)