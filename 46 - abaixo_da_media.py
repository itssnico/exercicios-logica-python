#Fazer um programa para ler um número inteiro N e depois um vetor de N números reais. Em seguida,
#mostrar na tela a média aritmética de todos elementos com três casas decimais. Depois mostrar todos
#os elementos do vetor que estejam abaixo da média, com uma casa decimal cada.

n = int(input("Quantos elementos vai ter o vetor? "))
vet: [int] = [0 for i in range (n)]

for i in range (n):
    vet[i] = float(input("Digite um numero: "))

media = 0
total = 0
for i in range(n):
    total = total + vet[i]

media = total / n

print(f"MEDIA DO VETOR: {media:.3f}")
print("ELEMENTOS ABAIXO DA MEDIA: ")
for i in range (n):
    if vet[i] < media:
        print(vet[i])