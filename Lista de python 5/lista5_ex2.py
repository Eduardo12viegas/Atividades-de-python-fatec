print ('data por extensso')
dia = input('digite o dia: ')
mes = int(input('digite o mês: '))
ano = input('digite o ano: ')

while mes <= 0 or mes > 12:
    print('Esse mês é invalido, digite novamente')
    mes = int(input('digite o mês: '))

if mes == 1:
    x = "janeiro"
elif mes == 2:
    x = "fevereiro"
elif mes == 3:
    x = "março"
elif mes == 4:
    x = "abril"
elif mes == 5:
    x = "maio"
elif mes == 6:
    x = "junho"
elif mes == 7:
    x = "julho"
elif mes == 8:
    x = "agosto"
elif mes == 9:
    x = "setembro"
elif mes == 10:
    x = "outubro"
elif mes == 11:
    x = "novembro"
elif mes == 12:
    x = "dezembro"

print(f'{dia} de {x} de {ano}')




