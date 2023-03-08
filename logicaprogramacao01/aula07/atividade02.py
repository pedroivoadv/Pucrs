# exemplo 13

def imc(peso, altura):
    return peso / altura ** 2

p = float(input("Peso: "))
a = float(input("Altura: "))
print(f"IMC: {imc(p,a)}")
