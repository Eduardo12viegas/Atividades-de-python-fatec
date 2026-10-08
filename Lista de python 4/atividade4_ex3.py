print('caixa eletronico, digite os valores dos produtos, digite "0" para encerrar')

quantidade = 1
soma = 0
corte = 1
atual = 0
while corte != 0: 
    atual = float(input(f'digite valor do {quantidade}º produto: '))
    if atual != 0:
        print(f'adicionado o {quantidade} produto, valor = {atual}')
        soma += atual
        print(f'total atual é de: {soma}')
        quantidade += 1
    else:
        if soma >= 100:
            print("aplicando desconto de 10%")
            soma -= soma / 10
        print(f"o valor total foi de {soma}")
        print('já vai pagando D:<')
