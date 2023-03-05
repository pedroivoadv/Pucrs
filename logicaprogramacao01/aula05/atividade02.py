#foram entrevistados 200 habitantes de uma cidade
# de cada habitante foram coletados os seguintes dados:
# - idade
# - renda
# - gênero
# - número de filhos

#calcular:
# a) media de renda
# b) media de idade de quem tem mais de 3 filhos
# c) quantidade de homenscom menos de 30 anos
# d) media do número de filhos
# e) renda dos homem mais velho
# f) idade da mulher com maior renda

import random

somaRendas = 0
somaIdades = 0
qtdMais3Filhos = 0
qtdHomensMenor30 = 0
somaFilhos = 0
rendaHomemMaisVelho = 0
idadeHomemMaisVelho = 0
idadeMulherMaiorRenda = 0
mulherMaiorRenda = 0


totalHab = 2000

for cont in range(2000): 

    #sorteio
    idade = random.randint(18,80)
    renda = random.randint(1200,12000)
    genero = random.choice(["m","f"])
    filhos = random.randint(0,5)

# 1. Media de renda

somaRendas += renda

# 2. Média de idades com mais de 3 filhos

if filhos > 3: 
    somaIdades += idade
    qtdMais3Filhos += 1 

# 3. Quantidade de homenscom menos de 30 anos

if genero == "m" and idade < 30:
    qtdHomensMenor30 += 1

# 4. Media do número de filhos    
somaFilhos += filhos 

# 5. Renda dos homem mais velho

if genero == "m" and idade > idadeHomemMaisVelho:
    idadeHomemMaisVelho = idade
    rendaHomemMaisVelho = renda

# 6. idade da mulher com maior renda

if genero == "f" and renda > mulherMaiorRenda:
    idadeMulherMaiorRenda = idade
    mulherMaiorRenda = renda

# Mostra Resultado

mediaRenda = somaRendas / totalHab
mediaMais3Filhos = somaIdades // qtdMais3Filhos
mediaFilhos = somaFilhos / totalHab

print(f"Media de Renda: {mediaRenda}")
print(f"Media de idade com mais de 3 filhos: {mediaMais3Filhos}")
print(f"Total de homens com menos de 30 anos: {qtdHomensMenor30}")
print(f"Media no. de filhos: {mediaFilhos}")
print(f"Renda do homem mais velho: {rendaHomemMaisVelho}")
print(f"Idade da mulher com maior renda: {idadeMulherMaiorRenda}")




