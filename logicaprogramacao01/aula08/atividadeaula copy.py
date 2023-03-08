#Exercício 1 –Construa um programa que gera uma lista com as
#avaliações de 25 pessoas. Cada pessoa avaliou a gestão do
#prefeito de uma cidade com notas de 5 a 1, onde 5 corresponde
#a Excelente, 4 a Bom, 3 a Regular, 2 a Ruim e 1 a Péssimo. Seu
#programa deve calcular e escrever:
#• A quantidade de votos em cada conceito

import random


lista = []
for i in range(1,26):
    lista.append(random.randint(1,5))
print("Notas: ", lista)

nota5 = 0
nota4 = 0
nota3 = 0
nota2 = 0
nota1 = 0

for nota in lista:
    if nota ==5 : nota5 += 1
    if nota ==4: nota4 += 1
    if nota ==3: nota3 += 1
    if nota ==2: nota2 += 1
    if nota ==1: nota1 += 1

print("quantidade de votos 5: ", nota5)
print("quantidade de votos 4: ", nota4)
print("quantidade de votos 3: ", nota3)
print("quantidade de votos 2: ", nota2)
print("quantidade de votos 1: ", nota1)
