compras = {
    "Sabonete": 2.50,
    "Shampoo": 15.00,
    "Condicionador": 16.50
}

for produto, preco in compras.items():
    print(f"O produto {produto.lower()} custa {preco} reais")
