#simula um caixa eletrônico

saldo = 1000
print("Bem-vindo ao caixa eletrônico!")
op = input("Digite a operação desejada (sacar, depositar, consultar): ")
if op == "sacar":
    valor = float(input("Digite o valor a ser sacado: "))
    if valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        print("Saque realizado com sucesso. Saldo atual: R$ {:.2f}".format(saldo))
elif op == "depositar":
    valor = float(input("Digite o valor a ser depositado: "))
    saldo += valor
    print("Depósito realizado com sucesso. Saldo atual: R$ {:.2f}".format(saldo))
elif op == "consultar":
    print("Seu saldo atual é R$ {:.2f}".format(saldo))