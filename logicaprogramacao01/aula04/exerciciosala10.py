#aula 4 pedra papel tisoura - O jogo Pedra, Papel e Tesoura

import random
jogador = input("Sua escolha [Pe]dra, [Pa]pel, [T]esoura? ")
comp = random.choice (["Pe","Pa","T"])
print(f"Computador escolheu: {comp}")

if jogador == comp:
    print(f"Empate!")
elif jogador == "Pe":
    if comp == "T":
     print("Pe quebra T! Você ganhou")
    else: 
       print("Pa cobre Pe! Você perdeu")
elif jogador == "Pa":
    if comp == "Pe":
       print("Pa cobre Pe! Você ganhou")
    else:
       print("T corta Pa! Você perdeu")
elif comp == "Pa":
   print("T corta Pa! Você ganhou!")
else:
   print("Pe quebra T! você perdeu")
