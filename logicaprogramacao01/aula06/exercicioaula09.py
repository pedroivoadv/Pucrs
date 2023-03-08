#aula 5 repetição alinhada 1. Implemente um programa que escreve os divisores dos 100 primeiros valores inteiros.

for num in range(1,101):
    print(">>Numero: ", num)
    d = 1
    while d <= num:
        if num %d == 0: print(d, " divide ", num)
        d = d + 1
