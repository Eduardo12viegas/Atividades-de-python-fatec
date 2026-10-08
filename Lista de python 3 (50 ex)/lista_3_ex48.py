senha = 123
n = int(input("Digite a senha: "))
while n != senha:
    print("Senha incorreta. Tente novamente.")
    n = int(input("Digite a senha: "))     
print("Senha correta. Acesso permitido.")
