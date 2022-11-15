primeiro = int(input("Primeiro valor: "))
segundo = int(input("Segundo valor: "))
terceiro = int(input("Terceiro valor: "))
if primeiro < segundo & primeiro < terceiro:
    print(f"MENOR = {primeiro}")
elif segundo < terceiro:
    print(f"MENOR = {segundo}")
else:
    print(f"MENOR = {terceiro}")
