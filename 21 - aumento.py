#Uma empresa vai conceder um aumento percentual de
#salário aos seus funcionários dependendo de quanto
#cada pessoa ganha, conforme tabela ao lado. Fazer um
#programa para ler o salário de uma pessoa, daí mostrar
#qual o novo salário desta pessoa depois do aumento,
#quanto foi o aumento e qual foi a porcentagem de aumento.

salario = float(input("Digite o salario da pessoa: "))
if salario <= 1000:
    porcentagem = 20
    aumento = salario * porcentagem /100
    novo = salario + aumento
elif salario <= 3000:
    porcentagem = 15
    aumento = salario * porcentagem / 100
    novo = salario + aumento
elif salario <= 8000:
    porcentagem = 10
    aumento = salario * porcentagem / 100
    novo = salario + aumento
else:
    porcentagem = 5
    aumento = salario * porcentagem / 100
    novo = salario + aumento

print(f"Novo salário = R$ {novo:.2f}")
print(f"Aumento = R${aumento:.2f}")
print(f"Porcentagem = {porcentagem}%")