nota1 = int(input('Digite a sua nota do trabalho laborátorio: '))
nota2 = int(input('Digite a sua nota da avaliação bimestral: '))
nota3 = int(input('Digite a sua nota do exame final: '))

soma = nota1 * 2 + nota2 *3 + nota3 *5
media = soma / 10

print("")
print(f'A media foi de: {media}')
print("")

if media >= 8:
    print('A menção foi de A')
elif media >= 7:
    print(' menção foi de B')
elif media >= 6:
    print('A menção foi de C')
elif media >= 5:
    print('A menção foi de D')
else:
    print('A menção foi de E')