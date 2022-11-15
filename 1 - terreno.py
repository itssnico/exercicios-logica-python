#Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma
#casa decimal, bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida,
#o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos com
#duas casas decimais, conforme exemplo.

comp = float(input("Digite o comprimento do terreno: "))
larg = float(input("Digite a largura do terreno: "))
valor = float(input("Digite o valor do metro quadrado: "))
print("__________________________________________________")
area = larg * comp
preco = valor * area
print(f"Area do terreno = {area:.2f}") #quando printar um numero float usar esse tipo de formatação
print(f"Valor do terreno: {preco:.2f}")