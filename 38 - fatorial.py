n = int(input("Digite o valor de N: "))
fat = 1
for i in range(n, 0, -1):
    fat = fat * i

print(f"FATORIAL: {fat}")