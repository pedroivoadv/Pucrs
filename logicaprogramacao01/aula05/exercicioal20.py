#aula 4 Programa para verificar se uma string digitada corresponde ao contrário (palíndromo)
#sopapos, radar, revivier, osso, ovo, anilina, arara

texto = input("Digite uma frase: ")
dif = False
for pos in range(len(texto)//2):
    if texto[pos] != texto[-1-pos]:
        dif = True
        break
if dif:
    print("A frase não é um palíndromo...")
else:
    print("A frase é um palíndromo!")
