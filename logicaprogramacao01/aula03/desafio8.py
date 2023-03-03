#aula5

saldoConta = float(input("Informe o saldo médio: "))

if saldoConta<500 : print("Sua conta não possui Limite")
if saldoConta>=500 and saldoConta<1000 : print("Limite de: ", saldoConta * 0.08)
if saldoConta>1000 : print("Limite", saldoConta * 0.15)
