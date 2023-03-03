#4 valores ordem crescente
v1 = int(input("Informe o primeiro valor: " ))
v2 = int(input("Informe o segundo valor: " ))
v3 = int(input("Informe o terceiro valor: " ))

if v2<v1:
    aux = v1
    v1 = v2
    v2 = aux

if v3<v1:
    aux = v1
    v1 = v3
    v3 = aux

if v3<v2:
    aux = v2
    v2 = v3
    v3 = aux

print("Ordem crescente", v1, v2, v3)
print("Ordem decrescente", v3, v2, v1)
