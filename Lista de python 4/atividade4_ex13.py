print("Sistema de Saque")
print("Digite valores para sacar. Digite 0 para encerrar.")

while True:
    valor = int(input("Digite o valor do saque: "))
    
    if valor == 0:
        print("Encerrando o sistema. Obrigado!")
        break
    
    print(f"Decomposição do saque de R${valor}:")
    
    
    notas = [100, 50, 20, 10, 5, 2, 1]
    
    for nota in notas:
        qtd = valor // nota   
        valor = valor % nota  
        if qtd > 0:
            print(f"{qtd} nota(s) de R${nota}")
    
    print("-" * 30)  
