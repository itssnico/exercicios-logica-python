#Leia um valor inteiro N. Este valor será a quantidade de números inteiros que serão lidos em seguida.
#Para cada valor lido, mostre uma mensagem dizendo se este valor lido é PAR ou IMPAR, e também
#se é POSITIVO ou NEGATIVO. No caso do valor ser igual a zero (0), seu programa deverá imprimir
#apenas NULO.

n = int(input("Quantos numeros você vai digitar? "))

for i in range (n):
    x = int(input("Digite um numero: "))
    if x == 0:
        print("NULO")
    elif x%2 == 0 and x>0:
        print("PAR POSITIVO")
    elif x%2 == 0 and x < 0:
        print("PAR NEGATIVO")
    elif x == 0 and x > 0:
        print("IMPAR POSITIVO")
    else:
        print("IMPAR NEGATIVO")
