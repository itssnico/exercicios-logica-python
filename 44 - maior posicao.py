#Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida, mostrar na tela
#o maior número do vetor (supor não haver empates). Mostrar também a posição do maior elemento,
#considerando a primeira posição como 0 (zero).

n = int(input("Quantos numeros voce vai digitar? "))

vet: [int] = [0 for i in range (n)]
maior = 0
posicao = int
for i in range (n):
    vet[i] = int(input("Digite um numero: "))

for i in range (n):
    if vet[i] > maior:
        maior = vet[i]
        posicao = i

print(f"\nMAIOR VALOR = {maior:.1f}")
print(f"POSICAO DO MAIOR VALOR = {posicao}")


