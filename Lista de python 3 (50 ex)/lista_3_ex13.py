n = float(input('digite o primeiro número: '))
n2 = float(input('digite o segundo número: '))

if n == n2:
    print(f'os números {n} e {n2} são iguais')
elif n > n2:
    print(f'o número {n} é maior que o número {n2}')
else:
    print(f'o número {n} é menor que o número {n2}')