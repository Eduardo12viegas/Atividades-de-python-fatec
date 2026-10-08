n = int(input('Digite um número inteiro positivo: '))
fibonacci = 0
for i in range(1, n + 1):
    if i == 1 or i == 2:
        fibonacci = 1
    else:
        fibonacci = fibonacci + fibonacci
    print("Calculando: {} = {}".format(i, fibonacci))
print("A sequencia de fibonacci até {} da o total de {}".format(n, fibonacci))

