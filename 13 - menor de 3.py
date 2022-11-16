#Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três
#números lidos. Em caso de empate, mostrar apenas uma vez

primeiro = int(input("Primeiro valor: "))
segundo = int(input("Segundo valor: "))
terceiro = int(input("Terceiro valor: "))
if primeiro < segundo and primeiro < terceiro:
    print(f"MENOR = {primeiro}")
elif segundo < terceiro:
    print(f"MENOR = {segundo}")
else:
    print(f"MENOR = {terceiro}")
