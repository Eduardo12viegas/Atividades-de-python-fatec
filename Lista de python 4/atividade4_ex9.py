print("piramide numerica")
n = int(input("digite um numero inteiro: "))

soma = ""
for i in range(1, n + 1):
    soma += str(i)

for i in range(n, 0, -1):
    print(soma[:i])