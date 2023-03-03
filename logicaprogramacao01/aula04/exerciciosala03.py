#Aprovação de aluno por nota e frequência com exame aula 2

p1 = float(input("P1: "))
p2 = float(input("P2: "))
p3 = float(input("P3: "))
freq = float(input("Freq: "))

g1 = (p1+p2+p3)/3

print(f"Media G1: {g1}")

if freq < 75: 
    print(f"Reprovado por faltas: {freq}")
else: 
    if g1 >=7: 
        print(f"Aprovado por media: {g1}")
    else:
        if g1 < 4:
            print(f"Reprovado por média: {g1}")
        else:
            # Em exame (g2)
            g2 = float(input("G2: "))
            final = (g1 + g2)/2
            if final >=5:
                print(f"Aprovado em G2: {final}")
            else:
                print(f"Reprovado em G2: {final}")
  