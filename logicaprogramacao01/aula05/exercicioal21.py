#aula 4 Programa para verificar se uma string digitada corresponde ao contrário (palíndromo) solução 2
#sopapos, radar, revivier, osso, ovo, anilina, arara

texto = input("Digite uma frase: ")

print(f"Invertida: {texto[::1]}")
if texto != texto[::-1]:
    print("A frase não é um palíndromo...")
else:
    print("A frase é um palíndromo!")