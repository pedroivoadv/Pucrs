#exercicio 1

#Jogo da advinhação
# - 10 tentativas para adivinhar um número sorteado entre 1 e 100
# - computador informa se o número é maior ou menor que o digitado

import random

sorteado = random.randint(1, 100)
#print(f"Sorteado: {sorteado}")

acertou = False

for tent in range(1,11):
    print(f"Tentativa {tent}: ", end=" ")
    num = int(input())
    if num < sorteado:
        print("Tente um número maior...")
    elif num > sorteado:
        print("Tente um número menor...")
    else:
        acertou = True
        break
if acertou:
    print("Parabéns! Você acertou")
else:
    print(F"Que pena, você perdeu... O número sorteado era {sorteado}")

