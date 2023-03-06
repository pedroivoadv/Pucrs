
a = int(input("Informe o valor inicial do intervalo: "))
while a<0 : 
    print("o valor inicial do intervalo deve ser um valor natural")
    a = int(input("Informe novamente o valor inicial do intervalo: "))

b = int(input("Informe o valor final do intervalo: "))
while b<0:
    print("o valor final do intervalo deve ser um valor natural")
    b = int(input("Informe novamente valor final do intervalo: "))

if a > b: # não precisa de validação pq já vai estar certo os valores por causa do while
    aux = a
    a = b
    b = aux
if a%2==0 : a = a + 1
soma = 0
print("Valores impares do intervalo:")
while a<=b:
    print(a)  
    soma = soma + a
    a = a + 2
print("Soma dos impares do internvalo: ", soma)