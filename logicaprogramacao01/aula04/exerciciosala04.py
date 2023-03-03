#aula 2 exemplo 5: Coonceito em função da nota

nota = int(input("Nota: "))

if nota >= 90:
    print("Conceito A")
else:
    if nota >= 80:
        print("Conceito B")
    else:
        if nota >= 70:
            print("Conceito C")
        else: 
            if nota >= 60:
                print("Conceito D")
            else:
                print("Conceito F")
