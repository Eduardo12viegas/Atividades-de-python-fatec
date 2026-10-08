import random
n = random.randint(1, 50)
tentativas = 1
x = 0

print('tente adivinhar o numero secreto!')
while x != n:
    x = int(input(f"digite {tentativas}º numero: "))
    if x < n:
        print("não, não, o numero secreto é bem maior do que isso")
        tentativas += 1
    else:
        if x > n:
            print("se é loco, num compenssa, o numero secreto é menor do que isso")
            tentativas += 1

print ("você acertou :D")
print (f"o numero de tentativas foi de {tentativas}")

if tentativas == 1:
    print ("mas de primeira? deve ta de hack D:<")
else:
    if tentativas < 5:
        print ("Em menos de 5 tentativas? você é muito bom!")
    else:
        if tentativas <= 10:
            print("você pode fazer melhor!")
        else:
            if tentativas > 20:
                print("mais de 20 tentativas? se ta de sacanagem né kkkk")
            else:
                print("mais de 10 tentativas? se é ruim mesmo em kkkkkk")