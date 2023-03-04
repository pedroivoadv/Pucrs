#desafio aula 5 exercicios de fixação - Determinar se um ano é bissexto 

ano = int(input("Ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto!")
else:
    print("Não é bissexto...")