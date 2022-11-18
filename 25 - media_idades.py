#Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um
#indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular
#e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez,
#mostrar a mensagem "IMPOSSIVEL CALCULAR".


print("Digite as idades: ")
id = int(input())
soma = 0
total = 0
media = 0
if id < 0:
    print("IMPOSSIVEL CALCULAR")
else:
    while id > 0:
        soma = 0
        total = 0
        while id >= 0:
            soma = soma + 1
            total = total + id
            id = int(input())

        media = total / soma

        print(f"MEDIA = {media:.2f}")

