# exercicio 26

def binomial2(n,k):
    prod = 1
    total = k
    if n-k < k:
        total = n-k
    for i in range(1,total+1):
        prod = prod * ((n+1-i)/i)
    return int(prod)

print(binomial2(4,2)) #dentro de 4 pessoas eu quero duas
print(binomial2(20,10)) #dentro 20 quero 10
