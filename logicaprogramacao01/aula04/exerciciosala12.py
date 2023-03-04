#Classificação: identificação do grau de hipertensão, se houver? Determinação da situação em função da pressão arterial

sist = int(input("Sistólica: "))
diast = int(input("Diastólica: "))

if diast >= 120  or sist >= 180:
    print("Crise  hipertensiva")
elif (diast >= 90 and diast < 120) or (sist >= 140 and sist < 180):
    print("Hipertensão estágio 2")
elif (diast >=80 and diast <90) or (sist >= 130 and sist < 140):
    print("Hipertensão estágio 1") 
elif diast < 80 and sist < 130 and sist >= 120:
    print("Elevada")
elif sist < 120 and diast < 80:
    print("Normal")
