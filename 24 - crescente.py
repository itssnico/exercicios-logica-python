x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))


while x != y:
    if x > y:
        print("DECRESCENTE!")
    else:
        print("CRESCENTE!")

    print("Digite dois numeros:")
    x = int(input())
    y = int(input())


