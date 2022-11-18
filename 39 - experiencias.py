#Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para
#organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano,
#quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este
#laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas
#informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia
#utilizada e a quantidade de cobaias utilizadas em cada experimento. Faça um programa que leia um
#valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um
#inteiro que representa a quantidade de cobaias utilizadas e uma letra ('C', 'R' ou 'S'), indicando o tipo
#de cobaia (R:Rato S:Sapo C:Coelho). Apresente o total de cobaias utilizadas, o total de cada tipo de
#cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o
#percentual deve ser apresentado com dois dígitos após o ponto.


tipo = int; qnt = int;
c = 0
r = 0
s = 0
total = 0
n = int(input("Quantos casos de teste serao digitados? "))

for i in range(n):
    qnt = int(input("Quantide de cobaias: "))
    tipo = input("Tipo de cobaia: ")
    total = total +qnt
    if tipo == "c":
        c = c + qnt
    elif tipo == "r":
        r = r + qnt
    elif tipo == "s":
        s = s + qnt
pcoelhos = (float(c) / total) * 100.0
pratos = (float(r) / total) * 100.0
psapos = (float(s) / total) * 100.0
print("")
print("RELATÓRIO FINAL: ")
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos {r}")
print(f"Total de sapos: {s}")
pcoelhos = (float(c) / total) * 100.0
pratos = (float(r) / total) * 100.0
psapos = (float(s) / total) * 100.0
