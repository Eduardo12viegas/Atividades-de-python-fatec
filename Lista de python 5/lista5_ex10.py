print("Calculador de médias")
somaM = 0
quantidadeM = 0
somaF = 0
quantidadeF = 0

for i in range(1, 5):
    idade = int(input(f"Digite a idade do {i}º aluno: "))

  
    sexo = input(f"Digite o gênero (M/F) do {i}º aluno: ").upper()
    while sexo not in ["M", "F"]:
        print("Gênero inválido. Digite apenas M ou F.")
        sexo = input(f"Digite o gênero (M/F) do {i}º aluno: ").upper()

    if sexo == "M":
        somaM += idade
        quantidadeM += 1
    else:  # aqui só sobra "F"
        somaF += idade
        quantidadeF += 1

print("")
if quantidadeM > 0:
    print(f"O número de alunos masculinos é {quantidadeM}")
    print(f"A média de idade dos alunos masculinos é {somaM / quantidadeM:.2f}")
else:
    print("Nenhum aluno masculino informado")

print("")
if quantidadeF > 0:
    print(f"O número de alunas femininas é {quantidadeF}")
    print(f"A média de idade das alunas femininas é {somaF / quantidadeF:.2f}")
else:
    print("Nenhuma aluna feminina informada")