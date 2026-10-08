n = int(input('Digite quantos numeros a fatorar: '))

for i in range(1, n+1):
    x = int(input(f'digite o {i}º numero: '))
    fatorial = 1
    for j in range(1, x+1):
        fatorial *= j
    print(f'O fatorial de {x} é {fatorial}')