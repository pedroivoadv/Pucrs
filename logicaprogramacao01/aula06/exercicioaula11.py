#A conjectura de goldbach

quant = int(input("Informe a quantidade de valores pares: "))
while quant <= 0:
    print("Valor deve ser positivo")
    quant = int(input("Informe novamente a quantidade de valores pares: ")) 

num = 4
pares = 1
while pares<= quant: 
    print("Número: ", num)
    parte1 = num // 2
    parte2 = parte1

    while parte2 <= parte1:
        contParte1 = 0
        d = 1
        while d<= parte1: #ver se é primo
            if parte1 % d == 0: contParte1 = contParte1 + 1
            d = d + 1
        
        if contParte1 == 2: #se o primeiro não é primo nem adianta testar segundo
            d = 1
            contParte2 = 0
            while d<=parte2: #teste se for primo
                if parte2 % d ==0 : contParte2 = contParte2 + 1
                d = d + 1
            if contParte2 == 2: #encontrou dos divisores
                print("Primo1 : ", parte1, "Primo2: ", parte2)
                pares = pares + 1
                break
        
        parte1 = parte1 + 1
        parte2 = parte2 - 1

    num = num + 2
