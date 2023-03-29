#Exercício 3 - – Foi feita uma pesquisa entre os habitantes de uma
#região. Foram coletados os dados de idade, sexo (1-masculino/2-
#feminino) e salário. Faça um programa que leia os dados
#necessário e informe:

#(a)a média de salário do grupo;
#(b) maior e menor idade do grupo;
#(c) quantidade de mulheres com salário até R$3500,00.
#Encerre a entrada de dados quando for digitada uma idade
#negativa

somaSalario = 0
pessoas = 0
maior = 0
menor = 120
mulheres = 0
while True:
    print("Informe uma idade negativa para encerrrar a entrada de dados.")
    idade = int(input("Informe uma idade: "))
    if idade <0:
        print("Fim do programa")
        break 

    while idade<=0 or idade>=120:
        print("> Idade invalida. Deve estar no intervalo de (0;120).")
        idade = int(input("Informe uma idade valida: "))

    genero = int(input("Informe o genero, usando 1 para feminino e 2 para masculino: "))
    while genero!=1 and genero !=2:
        print("> Genero invalido. ")
        genero = int(input("> Informe novamente o genero, usando 1 para feminino e 2 para masculino: "))

    salario = float(input("Informe o salario: "))
    while salario<0:
        print("> Salario invalido.")
        salario = float(input("> Informe novamente o salario: "))

    somaSalario = somaSalario + salario
    pessoas = pessoas + 1
    if idade > maior : maior = idade
    if idade < menor : menor = idade
    if genero == 1 and salario<=3500: mulheres = mulheres + 1


print("===============")
if pessoas == 0: print("Dados não informados")
else:
    print("Media salario", somaSalario/pessoas)
    print("Maior idade do grupo: ", maior)
    print("Menor idade do gruopo: ", menor)
    print("Quantidade de mulheres que ganham até R$ 3500", mulheres)