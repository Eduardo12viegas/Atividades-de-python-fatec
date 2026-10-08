senha = '007'
tentativas = 3
x = '0'

while tentativas > 0:
    x = input('Digite sua senha: ')
    if x == senha:
        print('Senha correta!')
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print('Senha incorreta!')
            print(f'você ainda tem {tentativas}º tentativas')
        else:
            print('vaza daqui seu bobão, tentativas esgotadas')

