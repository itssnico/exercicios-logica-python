#Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
#O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
#e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve
#mostrar o valor do troco a ser devolvido ao cliente.


prod = float(input("Preço unitário do produto: "))
qnt = int(input("Quantidade comprada: "))
recebido = float(input("Dinheiro recebido: "))
total = prod * qnt
troco = recebido - total
print(f"TROCO = {troco:.2f}")