#aula 3 exercicio 9

#calculo de IMC

print("Cálculadora de IMC")
altura = float(input("Qual é sua altura em metros: "))
peso = float(input("Qual é seu peso em kg: "))

imc = peso/altura**2
print(f"Seu IMC é {imc}: ")

if imc < 18.6:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso ideal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade grau I")
elif imc < 40:
    print("Obesidade grau II (severa)")
else:
    print("Obesidade grau III (mórbida)")
