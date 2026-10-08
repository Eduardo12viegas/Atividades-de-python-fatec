n = float(input('digite o primeiro número: '))
n2 = float(input('digite o segundo número: '))
n3 = float(input('digite o terceiro número: '))

if n < n2 and n < n3:
    
    print(f'o número {n} é o menor')
elif n2 < n3:
    print(f'o número {n2} é o menor')
else:
    print(f'o número {n3} é o menor')

