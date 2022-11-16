#Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
#O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
#e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido
#ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o
#valor restante conforme exemplo.


uni = float(input("Preço unitário do produto: "))
qnt = int(input("Quantidade comprada: "))
rec = float(input("Dinheiro recebido: "))
total = uni * qnt
if total<rec:
    troco = rec - total
    print(f"TROCO = R${troco:.2f}")
else:
    falta = total - rec
    print(f"DINHEIRO INSUFICIENTE, FALTAM R${falta:.2f}")