#aula 5Exercício 1 –Construa um programa que escreve o fatorial dos 100 primeiros inteiro.

fat = 1
aux = 2

for num in range (1, 6):
   print(">>Numero: ", num)
   while aux <= num:
      fat = fat * aux
      aux = aux + 1
      print("Fatorial: ", fat)
