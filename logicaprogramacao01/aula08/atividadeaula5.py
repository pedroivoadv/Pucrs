# aula 3 Exercício 1 – Foram vendidas 50 peças de roupa. De cada peça
#foram coletados os seguintes dados: tamanho (P,M ou G) e cor
#(branco, preto ou azul). O programa deve ler os dados das peças
#de roupas e organizá-los em uma lista de tuplas, onde cada tupla
#é da forma (tamanho, cor). O programa deve ainda calcular e
#escrever: o tamanho que mais vendeu, a quantidade de peças de
#tamanho M que foram vendidas e a cor preferida pelos clientes.

import random

lista = []
cont = 1
for i in range(1,6):
   tamanho = random.choice(["P", "M", "G"])
   cor = random.choice(["branco", "preto", "azul"])
   lista.append((tamanho, cor))

print(lista)


tamanhoP = []
contp = 0
for item in lista: 
   if "P" in item:
    contp = contp + 1
   tamanhoP.append(item[0])

print(contp)


tamanhoM = []
contm = 0
for item in lista:
   if "M" in item:
      contm = contm + 1
   tamanhoM.append(item[0])

tamanhoG = []
for item in lista:
   tamanhoG.append(item[0])


print("A quantidade de tamanho P azuis vendidas foi", tamanhoP.count("P"))
print("A quantidade de tamanho M vendidas foi", tamanhoM.count("M"))
print("A quantidade de tamanho G vendidas foi", tamanhoG.count("G"))
