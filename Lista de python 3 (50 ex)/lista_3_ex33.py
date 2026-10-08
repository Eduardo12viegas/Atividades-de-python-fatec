contador = 0

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    contador += numero
media = contador / 5
print(f"A média dos números digitados é: {media}")
    
