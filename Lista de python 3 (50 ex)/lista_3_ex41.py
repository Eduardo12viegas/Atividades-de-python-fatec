n = int(input('Digite um número inteiro positivo: '))
fatorial = 1
if n < 0:
    print("Não existe fatorial de número negativo.")
else:
    for i in range(1, n + 1):
        fatorial *= i
        print ("Calculando: {}! = {}".format(i, fatorial))
    print("O fatorial de {} é {}".format(n, fatorial))
