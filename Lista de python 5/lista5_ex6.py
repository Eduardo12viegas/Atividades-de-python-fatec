n = int(input("Digite a sua idade escoteiro: "))

while n < 6 or n > 116:
    print("Idade inválida, tente novamente")
    n = int(input("Digite a sua idade escoteiro: "))

if n < 10:
    print("Você é um lobinho")
elif n < 14:   
    print("Você é um escoteiro")
elif n < 18:   
    print("Você é um sênior")
elif n < 21:   
    print("Você é um pioneiro")
else:         
    print("Você é um líder")