#Um comerciante deseja fazer o levantamento do lucro das mercadorias que ele comercializa. Para isto,
#mandou digitar um conjunto de N mercadorias, cada uma contendo nome, preço de compra e preço de
#venda das mesmas. Fazer um programa que leia tais dados e determine e escreva quantas mercadorias
#proporcionaram:
# lucro < 10%
# 10% ≤ lucro ≤ 20%
# lucro > 20%
#Determine e escreva também o valor total de compra e de venda de todas as mercadorias, assim como
#o lucro total.

n = int(input("Serão digitados quantos produtos? "))
nome: [str] = [0 for x in range (n)]
compra: [float] = [0 for x in range (n)]
venda: [float] = [0 for x in range (n)]
porcentagem: [float] = [0 for x in range (n)]

for i in range (n):
    print(f"Produto {i+1}:")
    nome[i] = input("Nome: ")
    compra[i] = float(input("Preco de compra: "))
    venda [i] = float(input("Preco de venda: "))

for i in range (n):
    porcentagem[i] = (((venda[i] - compra[i]) / compra[i]) * 100)

abaixo = 0
entre = 0
acima = 0

for i in range(n):
    if porcentagem[i] < 10.0:
        abaixo = abaixo + 1
    elif porcentagem[i] < 20.0:
        entre = entre + 1
    else:
        acima = acima + 1

totalCompra = 0
totalVenda = 0
for i in range (n):
    totalCompra = totalCompra + compra[i]
    totalVenda = totalVenda + venda[i]

total = totalVenda - totalCompra
print("\nRELATÓRIO: ")
print(f"Lucro abaixo de 10%: {abaixo}")
print(f"Lucro entre 10% e 20%: {entre}")
print(f"Lucro acima de 20%: {acima}")
print(f"Valor total de compra: {totalCompra:.2f}")
print(f"Valor total de venda: {totalVenda:.2f}")
print(f"Lucro total: {total:.2f}")
