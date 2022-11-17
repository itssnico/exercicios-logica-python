#Leia os valores das coordenadas X e Y de um ponto no plano
#cartesiano. A seguir, determine qual o quadrante ao qual pertence o
#ponto (Q1, Q2, Q3 ou Q4). Se o ponto estiver na origem, escreva a
#mensagem “Origem”. Se o ponto estiver sobre um dos eixos escreva
#“Eixo X” ou “Eixo Y”, conforme for a situação.

x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
if x == 0 and y == 0:
	print("Origem")
elif x == 0:
	print("Eixo Y")
elif y == 0:
	print("Eixo X")
elif x > 0 and y > 0:
	print("Q1")
elif x < 0 and y > 0:
	print("Q2")
elif x < 0 and y < 0:
	print("Q3")
else:
	print("Q4")