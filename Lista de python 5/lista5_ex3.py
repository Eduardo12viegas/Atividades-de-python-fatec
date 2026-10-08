c = int(input("Digite o numero do cargo: "))

while c < 1 or c > 5:
    print("Cargo invalido, tente novamente")
    c = int(input("Digite o numero do cargo: "))

if c == 1:
    salario = 2.500
    beneficios = 300
    inposto = 8
elif c == 2:
    salario = 2.500
    beneficios = 450
    inposto = 10
elif c == 3:
    salario = 3.200
    beneficios = 600
    inposto = 12
elif c == 4:
    salario = 7.500
    beneficios = 1000
    inposto = 15
else:
    salario = 12.000
    beneficios = 2000
    inposto = 20

salario_bruto = salario + beneficios
salario_liquido = salario_bruto - (salario_bruto * inposto / 100)

print("Salario bruto: R$ {:.2f}".format(salario_bruto))
print("Salario liquido: R$ {:.2f}".format(salario_liquido))