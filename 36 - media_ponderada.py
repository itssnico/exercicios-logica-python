#Leia um valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de
#teste consiste de 3 valores reais, para os quais você deverá calcular e mostrar a média ponderada, sendo
#que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5. Vale lembrar
#que a média ponderada é a soma de todos os valores multiplicados pelo seu respectivo peso, dividida
#pela soma dos pesos.
n = int(input("Quantos casos você vai digitar? "))
for i in range (n):
    print("Digite três numeros: ")
    primeiro = float(input())
    segundo = float(input())
    terceiro = float(input())
    total = 0
    media = 0

    primeiro = primeiro * 2
    segundo = segundo * 3
    terceiro = terceiro * 5
    total = primeiro + segundo + terceiro
    media = total / 10
    print(f"MEDIA = {media:.1f}")