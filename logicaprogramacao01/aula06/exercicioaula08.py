#exercicio aula 3 para indeterminado

#aula 3

cont = 0
somaIdade = 0
somaAltura = 0
meninas = 0
mais20 = 0
maiorIdade = 0
maiorAltura = 0
while True:
    print("Cont: ", cont)
    print("Para encerrar a repetição, informe uma idade negativa")
    idade = int(input("informe a sua idade: "))
    if idade < 0:
        print("Fim de programa")
        break

    while idade <= 0 or idade >= 120:
        print("> Idade Invalida. Deve estar no intervalo (0;120).")
        idade = int(input("> Informe novamente a sua idade: "))
    
    altura = float(input("Informe a sua altura: "))
    while altura<=0 or altura>=2.5: 
        print("> Alturada invalida. Deve estar no internovalo de (0, 2.50)")
        altura = float(input("> Informe novamente a sua altura: "))

    genero = int(input("Informe o seu genero usando 1 para feminino e 2 para masculino: "))
    while genero!=1 and genero!=2:
        print("> Genero invalido. Deve ser 1 ou 2.")
        genero = int(input("> Informe novamente o seu genero usando 1 para feminino e 2 para masculino"))
    # item (a)
    somaIdade = somaIdade + idade
    cont = cont + 1
    # item (b)
    if genero == 1:
        somaAltura = somaAltura + altura
        meninas = meninas + 1
    # item (c)
    if idade > 20: mais20 = mais20 + 1
    # item (d)
    if idade > maiorIdade:
        maiorIdade = idade
        maiorAltura = altura


print("==================================================================================")
if cont==0:
    print("Dados não informados")
else:
    print("Media de idade dos estudantes: ", somaIdade/cont)
    if meninas==0 : print("Não foram informados dados de meninas")
    else: print("Media de altura das meninas: ", somaAltura/meninas)
    print("Percentual de alunos com mais de 20 anos: ", mais20*100/cont)
    print("Alturado mais velho: ", maiorAltura, "Idade do mais velho:", maiorIdade)
