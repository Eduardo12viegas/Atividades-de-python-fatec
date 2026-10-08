soma = 0
n = 0
x = int(input("Digite um número inteiro, digite 0 para encerrar: "))
while x != 0:
    n += 1
    soma += x
    x = int(input("Digite um número inteiro, digite 0 para encerrar: "))
print(f"Você digitou {n} números inteiros.")
print(f"A soma de todos os números digitados é {soma}.")
