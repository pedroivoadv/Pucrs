# Programa para mostrar as iniciais de um nome com o(s) sobrenomes, digitados em uma única string

nome = input("Digite um nome completo: ")
inicio = True

for letra in nome:
    if inicio:
        print(f"{letra}. ", end="")
        inicio = False
    elif letra == " ":
        inicio = True
