#Com base no exemplo dos meses, escreva um programa que determine a quantidade de dias existentes em um mês e ano informados. • Lembre-se que alguns meses têm 30, outros têm 31 e um deles tem 28 (ou 29, se o ano for bissexto).

mes = int(input("Mês: "))
ano = int(input("Ano: "))

if mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        dias = 29
    else:
        dias = 28
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias =30
else:
    dias = 31

print(f"Total de dias: {dias}")