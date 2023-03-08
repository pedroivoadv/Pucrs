#Exercício 1 –Construa um programa que gera uma lista com as
#avaliações de 25 pessoas. Cada pessoa avaliou a gestão do
#prefeito de uma cidade com notas de 5 a 1, onde 5 corresponde
#a Excelente, 4 a Bom, 3 a Regular, 2 a Ruim e 1 a Péssimo. Seu
#programa deve calcular e escrever:
#• A quantidade de votos em cada conceito

import random
lista = [] #lista vazia
for i in range(1,26):
    lista.append(random.randint(1,6))
print("Nota: ", lista)

# duas lista para cada uma receber o rotulo do conceito e a outra a quantidade correspondente a relação das duas listas está posicional
conceito = []
quantidade = []
conceito.append('Excelente')  
quantidade.append(lista.count(5))
conceito.append('Bom')
quantidade.append(lista.count(4))
conceito.append('Regular')
quantidade.append(lista.count(3))
conceito.append('Ruim')
quantidade.append(lista.count(2))
conceito.append('Pessimo')
quantidade.append(lista.count(1))
maiorQuantidade = quantidade [0]
maiorConceito = conceito[0]

for i in range(0,5): #i para percorrer a lista
    print(conceito[i], " - ", quantidade [i])
    if quantidade[i] > maiorQuantidade:
        maiorQuantidade = quantidade[i]
        maiorConceito = conceito[i]
print("Conceitomais votado: ", maiorConceito)
print("Recebeu", maiorQuantidade, "votos")