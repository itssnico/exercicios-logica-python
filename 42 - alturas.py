#Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois, mostrar na
#tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos,
#bem como os nomes dessas pessoas caso houver.

n = int(input("Quantas idades serão digitas? "))
total = float

nome: [] = [0 for i in range (n)]
idade: [int] = [0 for i in range(n)]
altura: [float] = [0 for i in range(n)]

for i in range (n):
    print(f"Dados da {i+1}a pessoa:")
    nome[i] = input("Nome: ")
    idade[i] = int(input("Idade: "))
    altura[i] = float(input("Altura: "))

    total = 0
    menor = 0

media = total / n

print(f"Altura media: {media:.2f}")

for i in range (n):
    total = total + altura[i]
    if  idade[i] < 16:
        menor = menor + 1
totalMenor = (menor / n ) * 100

print(f"Pessoas com menos de 16 anos: {totalMenor:.1f}%")

for i in range (n):
    if idade[i] < 16:
        print(nome[i])