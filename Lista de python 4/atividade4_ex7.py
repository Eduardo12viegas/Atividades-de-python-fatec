x = int(input('digite o a largura do retangulo: '))
y = int(input('digite o a altura do retangulo: '))

linha1 = ("*" * x)
print('')
print(linha1)
for i in range(1, y - 1):
    linha2 = ("*" + (" " * (x - 2)) + "*")
    print(linha2)
print(linha1)
print('')

if x < 2 or y < 2:
    print('olha lá! ele não sabe fazer um retangulo! kkkkkkkkk')
    
if x / 2 == y:
    print('é um quadrado!')