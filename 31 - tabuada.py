#Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10, conforme exemplo.

x = int(input("Deseja tabuada para qual valor? "))
for i in range (0, 10 + 1):
    resultado = x * i
    print(f"{x} x {i} = {resultado}")