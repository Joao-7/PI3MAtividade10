produtos = []

for i in range(1,8):
    consumo = float(input(f"Consumo de matéria prima no produto {i} (em Kg): "))
    produtos.append(consumo)
    
consumo_total = sum(produtos)
maior_consumo = max(produtos)
id_maior = produtos.index(maior_consumo) + 1
    
print("----------------")
print(f"Consumo total: {consumo_total} Kg")
print(f"Produto que mais consome matéria prima: Produto {id_maior} - {maior_consumo} Kg")
