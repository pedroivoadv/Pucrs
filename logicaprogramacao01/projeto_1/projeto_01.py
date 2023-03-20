import string 
import csv

mes = int(input("Digite um mês válido: "))
while mes <= 0 or mes >= 13:
    print("Digite um valor válido para mês de 1 a 12")
    mes = int(input("Digite um mês valido: "))

ano = int(input("Digite um ano válido entre 1961 a 2016: "))
while ano < 1961 or ano > 2016:
    print("Digite novamente um valor válido para ano entre 1961 a 2016")
    ano = int(input("digite um mês válido: "))

messtrg = str(mes)
anostrg = str(ano)
procura = (messtrg+"/"+anostrg)
mesAno = {procura}
print(procura)

planilha = ()

with open("/content/projetomini.csv") as arquivo_csv: 
  leitor_csv = csv.reader(arquivo_csv)

  for linha in leitor_csv: 
    dados = linha[-1].split(";") 
    planilha.ad

print(planilha)