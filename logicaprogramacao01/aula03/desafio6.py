#aula 5

v1 = float(input("Informe a primeira nota: " ))
v2 = float(input("Informe a segunda nota: " ))
v3 = float(input("Informe a terceiro nota: " ))

if v1<0 or v1>10 or v2<0 or v2>10 or v3<0 or v3>10 : print("Notas Invalidadas - intervalo tem que ser 0 a 10")
else:
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

nota = (v3 * 5 + v2* 2.5 + v1 * 2.5)/10
print("A média ponderada das notas é: ", nota)