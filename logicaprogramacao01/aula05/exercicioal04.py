#exemplo 4: algoritmo de Heron para calcular aproximação de raiz quadrada

num = int(input("Valor desejado: "))
total = int(input("Qtd. de repetições: "))

aprox = 1
for cont in range(1, total + 1): #repete "total" de vezes
    aprox = (aprox + num/aprox) / 2
    print(f"{cont:3}: {aprox:.5f}")

print(f"Raiz aproximada: {aprox:5f}")