n = int(input('Digite um número inteiro positivo: '))
x = 0
for i in range(1, n + 1):
        if n % i == 0:
            x += 1
print("O número {} tem {} divisores.".format(n, x))
if n == x:
    print("O número {} é perfeito.".format(n))
else:
    print("O número {} não é perfeito.".format(n))
