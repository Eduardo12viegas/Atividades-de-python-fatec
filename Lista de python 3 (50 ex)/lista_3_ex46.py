n = input("Digite um número: ")
soma = 0
for i in n:
    soma += int(i)
print("A soma dos caracteres do número {} é {}.".format(n, soma))