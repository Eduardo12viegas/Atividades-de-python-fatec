print("Sistema de notas")

qtd_alunos = int(input("Digite a quantidade de alunos: "))

aprovados = 0
reprovados = 0

for i in range(1, qtd_alunos + 1):
    print(f"\nAluno {i}:")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    media = (nota1 + nota2) / 2
    print(f"Média do aluno {i}: {media:.2f}")
    
    if media >= 6:  
        print("Situação: Aprovado")
        aprovados += 1
    else:
        print("Situação: Reprovado")
        reprovados += 1

print("\nResumo final:")
print(f"Total de alunos aprovados: {aprovados}")
print(f"Total de alunos reprovados: {reprovados}")
