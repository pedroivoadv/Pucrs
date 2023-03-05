#Aula 4 O operador de pertencimento (in) ajuda a resolver o problema:

texto = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
totalVogais = 0

for letra in texto:
    if letra in vogais:
        totalVogais += 1

print(f"Quantidade de vogais: {totalVogais}")
