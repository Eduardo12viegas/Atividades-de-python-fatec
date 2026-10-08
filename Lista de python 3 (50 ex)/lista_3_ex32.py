contador = 0
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    if numero < contador:
        contador = numero 

print(f"O menor número digitado foi: {contador}")  
