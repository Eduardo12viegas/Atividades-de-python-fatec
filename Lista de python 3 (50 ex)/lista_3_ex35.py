contador = 0 
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    if numero > 0:
        contador += 1

print(f"Quantidade de números positivos: {contador}")
