#Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades. Os nomes
#devem ser armazenados em um vetor, e as idades em um outro vetor. Depois, mostrar na tela o nome
#da pessoa mais velha.

n = int(input("Quantas pessoas voce vai digitar? "))

nomes: [str] = [0 for x in range(n)]
idades: [int] = [0 for x in range(n)]

for i in range(n):
	print(f"Dados da {i+1}a pessoa:")
	nomes[i] = str(input("Nome: "))
	idades[i] = int(input("Idade: "))

maioridade = idades[0]
posicaomaior = 0

for i in range(n):
	if idades[i] > maioridade:
		maioridade = idades[i]
		posicaomaior = i

print(f"PESSOA MAIS VELHA: {nomes[posicaomaior]}")