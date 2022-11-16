#Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de
#telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para
#ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago.


min = float(input("Digite a quantidade de minuts: "))
base = 50.00
if min <= 100:
    print(f"Valor a pagar R${base:.2f}")
else:
    novo = base+ ((min - 100) * 2)
    print(f"Valor a pagar R${novo:.2f}")