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

