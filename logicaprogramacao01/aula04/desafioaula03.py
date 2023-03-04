#exercício 3: Cálculo do salário líquido

bruto = float(input("Salário Bruto: "))
dep = int(input("Total de dependentes: "))

#de acordo com a faixa de salário, determina
#a alíquota do INSS e a parcela a deduzir

if bruto < 1212.01: 
    alinss = 0.075
    parcinss = 0
    #inss = bruto * 0.075
elif bruto <= 2427.35: 
    alinss = 0.09
    parcinss = 18.18
    #inss = bruto * 0.09 - 18.18
elif bruto <= 3641.03:
    alinss = 0.12
    parcinss = 91
    #inss = bruto * 0.12 - 91
else:
    alinss = 0.14
    parcinss = 163.82
    #inss = bruto * 0.14 -163.82

inss = bruto * alinss - parcinss

#verifica se desconto do INSS não passou do teto da última faixa
if inss > 828.39:
    inss = 828.39 #nesse caso, limita

print("INSS:", inss)

# Base para cáculo do IRRF
base = bruto - inss - 189.59 * dep

print("Base para cálculo de IRRF:", base)

# De acordo com a faixa salário, determina
# a alíquota do imposto e a parcela a deduzir

if base <= 1903.98:
    aliqirrf = 0
    parcirrf = 0
elif base <= 2826.65:
    aliqirrf = 0.075
    parcirrf = 142.8
elif base <= 3751.05:
    aliqirrf = 0.15
    parcirrf = 354.8
elif base <= 4664.68:
    aliqirrf = 0.225
    parcirrf = 636.13
else:
    aliqirrf = 0.275
    parcirrf = 869.36

# IRRF é a alíquota (%) aplicada à base de cálculo, subtraída da parcela a deduzir
irrf = base * aliqirrf - parcirrf

print("Imposto retido na fonte:", irrf)

#Salário líquido é o bruto, subtraído do inss e do IRRF calculado
liquido = bruto - inss - irrf

print("Salário líquido:", liquido)


