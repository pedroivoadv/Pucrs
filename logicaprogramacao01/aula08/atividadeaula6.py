#Exercício 1 – Foram vendidas 50 peças de roupa. De cada peça
#foram coletados os seguintes dados: tamanho (P,M ou G) e cor
#(branco, preto ou azul). O programa deve ler os dados das peças
#de roupas e organizá-los em uma lista de tuplas, onde cada tupla
#é da forma (tamanho, cor). O programa deve ainda calcular e
#escrever: o tamanho que mais vendeu, a quantidade de peças de
#tamanho M que foram vendidas e a cor preferida pelos clientes.

pecas = []
for i in range (1,6):
    print("cont: ", i)
    tamanho = input("Informe o tamanho usando os valores P, M, G: ")
    while(tamanho!="P" and tamanho!="p" and tamanho!="M" and tamanho!="m" and tamanho!="G" and tamanho!="g"):
        tamanho = input("Informe o tamanho usando os valores P, M, G: ")
    op = int(input("Informe a cor usando 1-Branco, 2-Preto e 3-Azul: "))
    while(op<1 or op>3):
        op = int(input("Informe a cor usando 1-Branco, 2-Preto e 3-Azul: "))
    if op==1: tupla = (tamanho, "branco")
    else:
        if op==2: tupla = (tamanho, "preto")
        else: tupla = (tamanho, "azul")
    pecas.append(tupla)
print(pecas)

contP = 0
contM = 0
contG = 0
cores = []
for item in pecas:
    if item[0]=='P' or item[0]=='p': contP = contP + 1 #procura o item na posição 0
    else:
        if item[0]=='M' or item[0]=='m': contM = contM + 1
        else:
            contG = contG + 1
    cores.append(item[1])

totalizaTamanho = []
totalizaTamanho.append(("Pequeno", contP))
totalizaTamanho.append(("Medio", contM))
totalizaTamanho.append(("Grande", contG))
print(totalizaTamanho)
maior = 0
tamanho = ""
for item in totalizaTamanho:
    if item[1] > maior:
        maior = item[1]
        tamanho = item[0]
print("Tamanho que mais vendeu: ", tamanho, "vendeu", maior, "peças")
print("Quantidade de tamanho M vendido: ", totalizaTamanho[1])
print("Quantidade de peças vendidas brancas: ", cores.count("branco"))
print("Quantidade de peças vendidas pretas: ", cores.count("preto"))
print("Quantidade de peças vendidas azuis: ", cores.count("azul"))
