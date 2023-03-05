#aula 2Estudo de caso, 50 alunos verificado idade, curso, semestre = verificado mais velho e que curso, media de idade e quantidade de alunos no 5° semestre

import random

somaIdades = 0
cursoMaisVelho = ""
idadeMaisVelho = 0
qtdAlunos5oSem = 0

for cont in range(50):
    #Sorteio
    idade = random.randint(18, 60)
    curso = random.choice(["Eng. Civil", "Eng. Mec","Eng. Química", "Eng. Prod."])
    semestre = random.randint(1,10)
    print(f"{idade} {curso} {semestre}")
    #Coleta de estatítiscas 
    #media de idades: é necessário somar as idades
    somaIdades += idade
    #curso do alunomais velho
    if idade > idadeMaisVelho:
        idadeMaisVelho = idade
        cursoMaisVelho = curso
    #total de alunos no 5o. semestre
    if semestre == 5:
        qtdAlunos5oSem +=1

mediaIdades = somaIdades // 50
print(f"Media de idades: {mediaIdades}")
print(f"Curso do aluno mais velho ({idadeMaisVelho} anos): {cursoMaisVelho}")                 
print(f"Total de alunos no 5o. sem: {qtdAlunos5oSem}")



