#aula 5

diaSemana = int(input("Digite um número de 1 a 7 para ter o correpondente no dia da semana: "))

if diaSemana<=0 or diaSemana>7 : print('Valor inválido')
else:
    if diaSemana==1 : print('O dia correspondente em dia da semana é segunda')
    if diaSemana==2 : print('O dia correspondente em dia da semana é terça')
    if diaSemana==3 : print('O dia correspondente em dia da semana é quarta')
    if diaSemana==4 : print('O dia correspondente em dia da semana é quinta')
    if diaSemana==5 : print('O dia correspondente em dia da semana é sexta')
    if diaSemana==6 : print('O dia correspondente em dia da semana é sábado')
    if diaSemana==7 : print('O dia correspondente em dia da semana é domingo')
