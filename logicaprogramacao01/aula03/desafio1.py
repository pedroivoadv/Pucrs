#Exercício 1 – Faça um programa que leia a altura de uma pessoa em metros e o seu gênero (use 1 para feminino e 2 para masculino). A seguir, o programa deve escrever o peso ideal dessa pessoa conforme descrito a seguir:• Para homens, o peso ideal corresponde a 72.7 × altura − 58 • Para mulheres, use 62.1 × altura − 44.7
import math

sexo = int(input('Informe seu sexo, sendo 1 para masculino e 2 para feminino: '))
altura = float(input('Informe a sua altura em metros: '))

if sexo !=1 and sexo !=2 : 
    print('Genero invalido. Peso Ideal não calculado')
    peso = 0
if sexo==1 : peso = 72.7 * altura - 58
if sexo==2 : peso = 62.1 * altura - 44.7
print('Peso ideal: ', peso)
