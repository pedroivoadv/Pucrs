#valores perfeitos 
num = int(input("Informe um valor inteiro e positivo: "))
while num <=0:
    print("Erro, o valor deve ser positivo.")
    num = int(input("Informe um valor inteiro e positivo: "))

soma = 0
d = 1
while d<num/2: #COLOCAR 2 PQ NAO TEM COMO DIVIR UM NUMERO PELA METADE MAIOR DELE
    if num%d ==0: soma = soma + d
    d = d + 1

if soma == num: print("Número perfeito")
else: print("Número não é perfeito")

# exemplo mil não é perfeito entao ele testou até o 999 por isso deve se colocar ACIMA 