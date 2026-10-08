n = int(input("Digite um número inteiro: "))

if n < 2:
    print("Esse número não é primo.")
elif n == 2:
    print("Esse número é primo.")
elif n % 2 == 0:
    print("Esse número não é primo.")
else:
    primo = True
    # só precisa testar os ímpares até a raiz quadrada
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            primo = False
            break
    if primo:
        print("Esse número é primo.")
    else:
        print("Esse número não é primo.")
