#Implementar o popular Jogo da Forca, onde
#o objetivo é descobrir a palavra escolhida
#pelo computador:
#• No início, o computador escolhe uma palavra
#• A cada jogada, o usuário “chuta” uma letra
#• Se a letra não existir na palavra, ele perde a
#jogada
#• Se a letra existir, ela é exibida na posição correta
#na palavra
#• Se completar o desenho do homem na forca, o
#jogo é encerrado

import random

def sorteio():
  return random.choice(["amarelo", "amiga", "amor", "ave", "bala", "bela", "bolo", "branco",
     "cama", "caneca", "celular", "clube", "copo", "doce", "elefante", "escola",
     "estojo", "faca", "foto", "garfo", "geleia", "girafa", "janela", "limonada",
     "meia", "noite", "ovo", "pai", "parque", "passarinho", "peixe",
     "pijama", "rato", "umbigo"])

def forca(vidas):
  if vidas == 0:
    print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''')
  elif vidas == 1:
    print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''')
  elif vidas == 2:
    print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''')
  elif vidas == 3:
    print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
  elif vidas == 4:
    print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''')
  elif vidas == 5:
    print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''')
  else:
    print('''
  +---+
  |   |
      |
      |
      |
      |
=========
''')
# 1. Sorteia a palavra
palavra = sorteio()
print(palavra)

#2 Gera uma palavra com _

tam = len(palavra)
adivinhada = "_" * tam #letras já adivinhadas
vidas = 6
letras = "" #letras já escolhidas

#print(adivinhada)


jogoAtivo = True

# 3. Enquanto o jogo estiver ativo:
while jogoAtivo:
  
  # 4.Exibi estado do jogo
  print()#pular espaço
  forca(vidas)
  print(adivinhada)
  print()
  print(f"Letras já escolhidas: {letras}")

  # 5. Aguarda a digitação de uma letra válida (ainda não escolhida)
  valida = False
  while not valida:
    letra = input("Escolha uma letra: ")
    if letra not in letras:
        valida = True
    else:
        print("Esta letra já foi escolhida!")

    # 6. Verifica se a letra está na palavra:
    
    #- Se não tiver, perde uma vida e verifica se o jogador perdeu
    if letra in palavra:
        #- Se estiver, troca os _
        pass
    else:
      print("Essa letra não está na plavra...")
      vidas -= 1

    # 7. verifica se o jogador ganhou

  