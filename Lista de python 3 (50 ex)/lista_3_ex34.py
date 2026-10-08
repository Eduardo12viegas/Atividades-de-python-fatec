contador_pares = 0 
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    if numero % 2 == 0:
        contador_pares += 1

print(f"Quantidade de números pares: {contador_pares}")

