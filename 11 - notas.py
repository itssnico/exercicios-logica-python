#Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de
#uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal) no
#ano juntamente com um texto explicativo. Caso a nota final do aluno seja inferior a 60.00, mostrar a
#mensagem "REPROVADO", conforme exemplos.

primeira = float(input("Digite a primeira nota: " ))
segunda = float(input("Digite a segunda nota: "))
print("-"*30)
soma = primeira + segunda
if soma >= 60:
    print(f"NOTA FINAL: {soma:.1f}")
else:
    print("REPROVADO!!!")
