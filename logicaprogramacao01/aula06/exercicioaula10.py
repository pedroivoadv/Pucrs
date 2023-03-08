#2. Implemente um programa que escreve os n primeiros números primos.

quant = int(input("Informe a quantidade de números primos: "))
while quant<=0:
    print("Valor invalido. A quantidade deve ser positiva")
    quant = int(input("Informe a quantidade de números primos: "))

num = 2
contPrimos = 1 #vai contar o quanto de primos eu contei

while contPrimos <= quant: #contar aquantidade que o usuario queria de primos
    contaDivisores = 0
    d = 1 # candidato a divisor
    while d <= num: # verificar se o numero é primo na sequencia
        if num % d == 0: contaDivisores = contaDivisores + 1
        d = d + 1
    if contaDivisores == 2:
        print(num)
        contPrimos = contPrimos + 1
    num = num + 1

