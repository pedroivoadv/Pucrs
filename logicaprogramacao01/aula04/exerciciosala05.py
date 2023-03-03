#Exemplo 6: determinar o dia da Páscoa em um ano específico aula 2

ano = int(input("Ano: "))
if ano < 1900 or ano > 2099:
    print("Impossível de Calcular!")
else:
    a = ano % 19
    b = ano % 4
    c = ano % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    dia = 22 + d + e
if ano == 1954 or ano == 1981 or ano == 2049 or ano == 2076:
    dia = dia - 7
if dia > 31:
    dia = dia - 31
    print(f"Dia da Páscoa: {dia} de abril")
else:
     print(f"Dia da Páscoa: {dia} de março")