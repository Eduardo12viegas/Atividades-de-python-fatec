n1 = int(input("Digite um número: "))
op = input("Digite a operação (+, -, *, /): ")
n2 = int(input("Digite outro número: "))
if op == "+":
    resultado = n1 + n2
elif op == "-":
    resultado = n1 - n2
elif op == "*":
    resultado = n1 * n2
elif op == "/":
    resultado = n1 / n2
print("O resultado da operação {} {} {} é {}.".format(n1, op, n2, resultado))