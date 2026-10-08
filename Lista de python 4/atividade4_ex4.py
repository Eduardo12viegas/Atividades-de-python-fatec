q = 1
soma = 0
pares = 0
impares = 0

print("digite 10 numeros inteiros e o algoritimo dira quantos são pares, impares, e a soma dos pares :D")
for i in range (1, 11):
    n = int(input(f'digite o {q}º numero: '))
    if n % 2 == 0:
        soma += n
        pares += 1
        q += 1
    else:
        impares += 1
        q += 1

print(f"o numero de pares foi de {pares}")
print(f"o numero de impares foi de {impares}")
print(f"a soma dos pares foi de {soma}")