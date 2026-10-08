for i in range(1, 7):
    nota1 = int(input(f"digite a primeira nota do {i}° aluno: "))
    nota2 = int(input(f"digite a segunda nota nota do {i}°: "))
    media = (nota1 + nota2) / 2
    if media < 3:
        print(f"o {i}° aluno foi reprovado")
    elif media < 7:
           print(f"o {i}° aluno esta sob exame")
    else:
           print(f"o {i}° aluno foi aprovado")