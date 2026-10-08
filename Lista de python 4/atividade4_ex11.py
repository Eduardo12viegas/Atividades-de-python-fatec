print("você tem 5 tentativas para acertar o numero secreto!")
print("o numero secreto é um numero inteiro!")

import random
n = random.randint(1, 100)
tentativas = 1
x = 0

while tentativas <= 5:     
    x = int(input(f"Digite a sua {tentativas}ª tentativa: "))
    
    if x == n:
        print("Você acertou :D")
        break
    elif x < n:
        print("O número é maior do que isso")
    else:
        print("O número é menor do que isso")
    
    tentativas += 1

if x != n:   
    print("Você perdeu D:")
    print(f"O número secreto era {n}")