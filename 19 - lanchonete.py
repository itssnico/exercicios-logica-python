#Uma lanchonete possui vários produtos. Cada produto possui um código
#e um preço. Você deve fazer um programa para ler o código e a
#quantidade comprada de um produto (suponha um código válido), e daí
#informar qual o valor a ser pago, com duas casas decimais, conforme
#tabela de produtos ao lado.

cod = int(input("Código do produto: "))
qnt = int(input("Quantidade comprada: "))

if cod == 1:
    total = qnt * 5.00
    print(f"Valor a pagar: R$ {total:.2f}")
elif cod == 2:
    total = qnt * 3.50
    print(f"Valor a pagar: {total:.2f}")
elif cod == 3:
    total = qnt * 4.80
    print(f"Valor a pagar: {total:.2f}")
elif cod == 4:
    total = qnt * 8.90
    print(f"Valor a pagar: {total:.2f}")
else:
    total = qnt* 7.32
    print(f"Valor a pagar: {total:.2f}")