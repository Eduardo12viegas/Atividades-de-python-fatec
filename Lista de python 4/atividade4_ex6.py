x = int(input("digite o numero que você quer saber a tabuada: "))

for i in range(1, 11):
    if x < 11:
        print(f'olha lá! ele não sabe a tabuada do {x}! kkkkkkkkk')
    print(f'{x} X {i} = {x * i}')