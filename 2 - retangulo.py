#Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor
#da área, perímetro e diagonal deste retângulo, com quatro casas decimais, conforme exemplos.

import math

base = float(input("Digite a base do retangulo: "))
altura = float(input("Digite a altura do retangulo: "))
area = base * altura
perimeto = 2 * (base+altura)
diagonal = math.sqrt(base*base + altura*altura)
print("-"*20)
print(f"Area: {area:.4f}")
print(f"Perimeto: {perimeto:.4f}")
print(f"Diagonal: {diagonal:.4f}")