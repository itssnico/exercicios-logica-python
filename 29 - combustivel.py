#Um posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes.
#Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma:
#1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a
#4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o
#código informado for o número 4, devendo então mostrar a mensagem "MUITO OBRIGADO", bem
#como as quantidades de cada combustível.


alcool = 0
gasolina = 0
diesel = 0
escolha = int(input("Informe um código(1, 2, 3) pu 4 para parar: "))
if escolha == 1:
    alcool = alcool + 1
elif escolha == 2:
    gasolina = gasolina + 1
elif escolha == 3:
    diesel = diesel + 1

while escolha != 4:
    escolha = int(input("Informe um código(1, 2, 3) pu 4 para parar: "))
    if escolha == 1:
        alcool = alcool + 1
    elif escolha == 2:
        gasolina = gasolina + 1
    elif escolha == 3:
        diesel = diesel + 1

print(f"MUITO OBRIGADO! ")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
