#Passando por todos os caracteres de uma string, usando acesso por índice

texto = input("Digite uma frase: ")
for pos in range(len(texto)):
  print(f"{pos}: {texto[pos]}")  
  #print(texto[pos])


