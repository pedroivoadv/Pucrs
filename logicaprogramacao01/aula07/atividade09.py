#gerador o triângulo de pascal

def pascal(linhas):
    for linha in range(linhas):
        for coluna in range(linha+1):
    valor = binomial2(linha,coluna)
    print(f"{valor} ",end="")
print()
