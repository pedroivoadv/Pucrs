#Exercício 3 –Elabore um programa que gera uma lista com 30
#valores inteiros, cria e escreve uma outra lista com os 10 maiores pg. 64

import random

lista = []

for i in range(1,31):
   lista.append(random.randint(1,21))
print("Os 30 valores", lista)

lista.sort()
lista.reverse()

indice = 0
maiores =[]

while(indice<10): #nunca pode mais, pode menos
   maiores.append(lista[indice])
   indice = indice + 1

print("Lista em ordem decrescente: ", lista)
print("Lista com os 10 maiores", maiores)
