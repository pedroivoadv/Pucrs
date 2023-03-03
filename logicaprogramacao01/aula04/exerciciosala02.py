
print("Com base na umidade e temperatura será dado o resultado")

temp = float(input("Qual a temperatura: "))
umidade = int(input("Qual é a medição da umidade?: "))

if temp > 30 :
    if umidade > 60:
        print('Quente e úmido')
    else: 
        print('Quente')
else:
    if temp <=30 and temp >=20:
        print("Ameno")
    else: 
        if temp <20 and temp>=10:
            print("Frio")
        else:
            print("Muito Frio")