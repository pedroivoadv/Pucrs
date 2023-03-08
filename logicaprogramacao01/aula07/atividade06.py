# aula 4 exemplo de pitagoras

import math

def distancia(x1,y1,x2,y2):
    deltax = x1-x2
    deltay = y1-y2
    dist = math.sqrt(deltax**2 + deltay**2)
    return dist

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
d = distancia(x1,y1,x2,y2)
print(f"Distância entre({x1}, {y1}) e ({x2}, {y2}): {d:.5f}")
