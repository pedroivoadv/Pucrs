#Exemplo 6: uso de continue

for cont in range(20):
    if cont %2 == 1:
        continue
    print(cont)
print("Continuação de programa")