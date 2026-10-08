print("Descubra o imposto de renda do seu salário") 
salario = float(input("Digite o valor do seu salário bruto: "))

if salario <= 2.112:
    print("Isento de imposto de renda")
elif salario > 2.112 and salario <= 2.826:
    aliquota = 7.5
    parcela_deduzir = 158.40
elif salario > 2.826 and salario <= 3.751:
    aliquota = 15
    parcela_deduzir = 370.40
elif salario > 3.751 and salario <= 4.664:
    aliquota = 22.5
    parcela_deduzir = 651.73
else:
    aliquota = 27.5
    parcela_deduzir = 884.96

imposto = salario * (aliquota / 100) - parcela_deduzir

if imposto < 0:
    print("Isento de imposto de renda")
else:
    print(f"O imposto de renda devido é: R$ {imposto:.2f}")