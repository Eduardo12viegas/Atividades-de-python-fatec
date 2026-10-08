q = int(input('digite quantas notas quer calcular'))
c = 0
for i in range(1, q + 1):
    n = float(input(f'digite a {i}ª nota: '))
    if n < 0:
        print('nota inválida')
    else:
        print(f'nota {i} é {n}')
        c += n
print(f'a soma das notas é {c}')
print(f'a média das notas é {c / q}')