#Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas. Fazer um programa
#que calcule e escreva a maior e a menor altura do grupo, a média de altura das mulheres, e o número
#de homens.

n: int; qtdhomens: int; qtdmulheres: int
menoraltura: float; maioraltura: float; alturafemMedia: float; alturafemtotal: float

n = int(input("Quantas pessoas serao digitadas? "))

alturas: [float] = [0 for x in range(n)]
generos: [str] = [0 for x in range(n)]

for i in range(n):
	alturas[i] = float(input(f"Altura da {i+1}a pessoa: "))
	generos[i] = str(input(f"Genero da {i+1}a pessoa: "))

menoraltura = alturas[0]
maioraltura = alturas[0]

for i in range(n):
	if alturas[i] > maioraltura:
		maioraltura = alturas[i]
	if alturas[i] < menoraltura:
		menoraltura = alturas[i]

qtdhomens = 0
qtdmulheres = 0
alturafemtotal = 0

for i in range(n):
	if generos[i]=='m':
		qtdhomens = qtdhomens + 1
	else:
		qtdmulheres = qtdmulheres + 1
		alturafemtotal = alturafemtotal + alturas[i]

alturafemMedia = alturafemtotal / qtdmulheres

print(f"Menor altura = {menoraltura:.2f}")
print(f"Maior altura = {maioraltura:.2f}")
print(f"Media das alturas das mulheres = {alturafemMedia:.2f}")
print(f"Numero de homens = {qtdhomens}")