preço = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o desconto em porcentagem: '))
preço_com_desconto = preço - (preço * desconto / 100)

print(f'o preço do produto antes era de R${preço:.2f} 1e com o desconto de {desconto}% o preço agora é de R${preço_com_desconto:.2f}')