#Programa para verificar se uma senha digitada é “forte”

import string

print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)
senha = input("Senha: ")

maiuscula = False
digito = False
pontuação = False

if len(senha) < 8:
    print("Erro: senha muito curta")
else:
    for letra in senha:
        if letra in string.ascii_uppercase:
            maiuscula = True
        if letra in string.digits:
            digito = True
        if letra in string.punctuation:
            pontuação = True
    if maiuscula == False or digito == False or pontuação == False:
        if maiuscula == False:
            print("Erro: senha não tem maiúsculas")
        if digito == False:
            print("Erro: senha não tem dígitos")
        if pontuação == False:
            print("Erro: senha não tem caractere de pontuação")
    else:
        print("senha válida!")
    

    


