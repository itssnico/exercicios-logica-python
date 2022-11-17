alcool = 0
gasolina = 0
diesel = 0
escolha = int(input("Informe um código(1, 2, 3) pu 4 para parar: "))
if escolha == 1:
    alcool = alcool + 1
elif escolha == 2:
    gasolina = gasolina + 1
else:
    diesel = diesel + 1

while escolha != 4:
    escolha = int(input("Informe um código(1, 2, 3) pu 4 para parar: "))
    if escolha == 1:
        alcool = alcool + 1
    elif escolha == 2:
        gasolina = gasolina + 1
    else:
        diesel = diesel + 1

print(f"MUITO OBRIGADO! ")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
