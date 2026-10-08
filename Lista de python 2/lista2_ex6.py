#Pergunta quantas notas o usuário possui e calcula a média delas. 
print("Quantas notas você deseja inserir?")
quantidade_notas = int(input())
notas = []

for i in range(quantidade_notas):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f'A média das notas é: {media:.2f}')
