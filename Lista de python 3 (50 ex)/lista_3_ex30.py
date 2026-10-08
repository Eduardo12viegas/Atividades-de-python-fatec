n = int(input("Digite um número inteiro: "))

soma = 0
for i in range (1, n + 1):
    soma += i
    print(soma)

print(f"A soma dos números de 1 a {n} é: {soma}")
