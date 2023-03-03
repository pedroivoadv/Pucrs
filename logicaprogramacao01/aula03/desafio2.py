#Faça um programa que leia o horário de inicio de um jogo, em horas e minutos, e o horário de fim desse jogo, também em hora e minutos. Sabendo que a duração máxima do jogo é de 24 horas, determine o tempo de duração do jogo em horas e minutos

print('Calculadora de tempo de jogo')

inicio_horas = int(input('Informe o horário de inicio do jogo em horas: '))
inicio_min = int(input('Informe o horário de inicio do jogo em minutos: '))
fim_horas = int(input('Informe o horário de termino do jogo em horas: '))
fim_min = int(input('Informe o horário de termino do jogo em minutos: '))

if inicio_horas<=0 and inicio_horas>=24 : print('Digite um valor certo para horário em horas de inicio')
if fim_horas<=0 and fim_horas>=24 : print('Digite um valor certo para horário em horas de termino')
if inicio_min<=0 and inicio_min>=60 : print('Digite um valor certo para horário em minutos de inicio')
if fim_min<=0 and fim_min>=60 : print('Digite um valor certo para horário em minutos de termino')

#transformar tudo em minuto para mais facil.

horarioInicial = inicio_horas * 60 + inicio_min
horarioFinal = fim_horas * 60 + fim_min

if horarioInicial < horarioFinal : duracao = horarioFinal - horarioInicial
else: duracao = 24*60  - horarioInicial + horarioFinal

print('Horas: ', duracao//60 )
print('Minutos: ', duracao%60)




