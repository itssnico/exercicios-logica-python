#Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida:
#- Imprimir todos os elementos do vetor
#- Mostrar na tela a soma e a média dos elementos do vetor

n = int(input("Quantos números você vai digitar? "))

vet: [int] = [0 for x in range(n)]

for i in range (n):
    vet[i] = int(input("Digite um número: "))

soma = 0
for i in range (n):
    soma =  soma + vet[i]

media= soma/n
print("\VALORES = ", end= " ")

for i in range(n):
    print(f"{ vet[i]:.2f}  ", end="")

print(f"\nSOMA = {soma:.2f}")
print(f"MEDIA = {media:.2f}")

