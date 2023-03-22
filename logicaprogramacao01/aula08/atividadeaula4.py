#aula 3
#Uma empresa de estatística analisou os 5 melhores jogadores de
#uma liga profissional de basquete e registrou os pontos,
#assistências e rebotes de cada um. Para isso, crie uma lista de
#tuplas, onde cada tupla é da forma (nome do jogador, pontos,
#assistência, rebotes). Ao final, o programa deve percorrer a lista
#e informar a tupla do jogador que tem as melhores estatísticas
#((pontos+assistências+rebotes)/3).

jogadores = []
cont= 1
while cont<=3:
    print("Cont: ", cont)
    nome = input("Informe o nome do jogador: ")
    pontos = int(input("Quantos pontos ele fez?: "))
    assistencias = int(input("Quantas assistencias ele fez?: "))
    rebotes = int(input("Quantos rebotes ele pegou?: "))
    jogadores.append((nome,pontos,assistencias,rebotes)) #estou colocando dentro parenteses para que ele faça uma tupla
    cont = cont + 1
print(jogadores)

estatisticas = []
for dados in jogadores:
    soma = 0 #media aritmetica das somas precisa criar soma
    for i in range (1, 4):
            soma = soma + dados[i] # dados i é cada valor lido
    media = soma/3
    estatisticas.append((dados[0], media))
print (estatisticas)

#melhor = estatisticas [0]
#for item in estatisticas:
#    if item > melhor : melhor = item #vai ser na posição 1 pq é a posição da média  
#print("Melhor jogador: ", melhor)

#correção 
melhor = estatisticas[0]
for item in estatisticas:
  if item[1]>melhor[1]: melhor = item
print("Melhor jogador: ", melhor)
