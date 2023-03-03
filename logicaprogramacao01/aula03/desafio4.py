#Exercicio1: Implemente um programa que determina o preço de venda dos produtos de uma loja conforme o preço de custo desses produtos. O programa deve ler o preço de custo e calcular o valor de venda conforme a tabela abaixo.

valorProduto = float(input("Digito o valor do produto para calcular a venda com base no lucro: " ))

if valorProduto<0: print('Valor inválido')

else:

    if valorProduto>0 and valorProduto<10 : print('O valor do produto atualizado será', valorProduto * 0.70 + valorProduto )

    if valorProduto>=10 and valorProduto<=30 : print('O valor do produto atualizado será', valorProduto * 0.50 + valorProduto )

    if valorProduto>30 and valorProduto<50 : print('O valor do produto atualizado será', valorProduto * 0.40 + valorProduto )

    if valorProduto>=50: print('O valor do produto atualizado será', valorProduto * 0.30 + valorProduto )


