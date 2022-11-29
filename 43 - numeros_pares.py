#Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida, mostre na
#tela todos os números pares, e também a quantidade de números pares.

n = int(input("Quantos numeros você vai digitar? "))
vet: [int] = [0 for i in range (n)]
for i in range (n):
    vet[i] = int(input("Digite o número: "))
    total = 0

print(f"NUMEROS PARES: ")

for i in range (n):
    if vet[i]%2 == 0:
        print(f"{vet[i]}", end= " ")
        total = total + 1

print(f"\n\nQUANTIDADE DE PARES: {total}")