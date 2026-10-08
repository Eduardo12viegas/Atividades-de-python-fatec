print("Pega um número inteiro e mostra todos os primos até ele")
n = int(input("Digite um número inteiro: "))

for i in range(2, n + 1):  
    primo = True
    for s in range(2, i):
        if i % s == 0:     
            primo = False
            break
    if primo:
        print(i)
