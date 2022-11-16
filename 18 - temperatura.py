#Deseja-se converter uma medida de temperatura da escala Celsius para Fahrenheit ou vice-versa. Para
#isso, você deve construir um programa que leia a letra "C" ou "F" indicando em qual escala vai ser
#informada uma temperatura. Em seguida o programa deve mostrar a temperatura na outra escala com

esc = input("Você vai digitar a temperatura em qual escala (C/F)? ")
if esc == "c":
    cel = float(input("Digite a temperatura em Celsius: "))
    feir = cel * 9/5 + 32
    print(f"Temperatura em Fahreinheit: {feir:.2f}")
else:
    feir = float(input("Digite a temperatura em Fahrenheit: "))
    cel = 5/9 * (feir - 32)
    print(f"Temperatura em Celsius: {cel:.2f}")