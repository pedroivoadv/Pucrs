ref_arquivo = open("dados.txt" , "w")
cont=1
while cont <=3:
  nome = input("Informe o nome: ")
  ref_arquivo.write(nome + "\n")
  cont = cont + 1
ref_arquivo.close()