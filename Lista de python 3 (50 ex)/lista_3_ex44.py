n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
x = 0

for i in range(1, n1 + 1):
    if n1 % i == 0 and n2 % i == 0:
        x = i
print("O maior divisor comum entre {} e {} é {}".format(n1, n2, x))
        
