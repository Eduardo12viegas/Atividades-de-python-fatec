soma = 0
n = int(input("Digite um número inteiro: "))
for i in range(1, n+1):
    if i % 2 != 0:
        soma += i
        print(i, end=" + ")
print(f"\b\b = {soma}")
