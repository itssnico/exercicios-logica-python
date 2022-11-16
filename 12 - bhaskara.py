#Fazer um programa para ler os três coeficientes de uma equação do segundo grau. Usando a fórmula
#de Baskara, calcular e mostrar os valores das raízes x1 e x2 da equação com quatro casas decimais,
#conforme exemplo. Se a equação não possuir raízes reais, mostrar uma mensagem.


import math

a = float(input("Digite o A: "))
b = float(input("Digite o B: " ))
c = float(input("Digite o C: "))

delta = (b * b) - (4*a*c)
if delta <0:
    print("Esta equação nao possui raizes reais")
else:
    x1 = ((-b) + math.sqrt(delta)) / (2 * a)
    x2 = ((-b) - math.sqrt(delta)) / (2 * a)
    print(f"X1 = {x1:.4f}")
    print(f"X2 = {x2:.4f}")