#Fazer um programa para ler a quantidade de glicose
#no sangue de uma pessoa e depois mostrar na tela a
#classificação desta glicose de acordo com a tabela de
#referência ao lado.
glic = float(input("Digite a medida da glicose: "))
if glic <= 100:
    print("Classificação: normal")
elif glic <= 140:
    print("Classificação: elevado")
else:
    print("Classificação: diabetes")

