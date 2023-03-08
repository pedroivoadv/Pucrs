#exer 15 • Variável com escopo local não podem ser acessadas fora da
# função que as define:

def calcula(base,taxa,duracao):
    final = base * (1+taxa) ** duracao #calculo de juros composto
    return final


b = float(input("Valor inicial: "))
t = float(input("Taxa de juros mensal: "))
d = int(input("Duração (meses): "))
res = calcula(b,t,d)
print(f"Valor no final do período: {res:.2f}")