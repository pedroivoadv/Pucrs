#Exercício 2 –Defina uma lista com a idade de 20 pessoas. Seu
#programa deve calcular e escrever: média de idade, maior e
#menor idade. pg 63

#import random

#lista = []
#for i in range(1,20):
#    lista.append(random.randint(0,85))
#print("idade: ", lista)

#media = sum(lista)/len(lista)
#print("O valor da média de idades é: ", media)

#print("O valor máximo da lista é: ", max(lista))
#print("O valor minimo da lista é: ", min(lista))

#forma professora

lista = []
for cont in range(1,6):
    notas = float(input("informe o valor da nota: "))
    lista.append(notas)
print(lista)

media = sum(lista)/len(lista)
max = max(lista)
menor = min(lista)

print("Media: ", media)
print("Maior: ",max)
print("Menor", menor)
