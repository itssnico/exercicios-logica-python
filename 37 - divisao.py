#Escreva um algoritmo que leia dois números e imprima o resultado da divisão do primeiro pelo
#segundo. Caso não for possível, mostre a mensagem “DIVISAO IMPOSSIVEL”.

n = int(input("Quantos casos você vai digitar? "))
for i in range (n):
    x = int(input("Entre com o numerador: "))
    y = int(input("Entre com o denominador: "))
    resultado = 0
    if y == 0:
        print("DIVISÃO IMPOSSIVEL")
    else:
        resultado = x / y
        print(f"DIVISÃO: {resultado:.2f}")