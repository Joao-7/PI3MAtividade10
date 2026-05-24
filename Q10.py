meses = []
print("---- Digite o valor das vendas em cada mês ----")

for i in range(1, 7):
    valor = float(input(f"Mês {i}: "))
    meses.append(valor)
    
total_vendas = sum(meses)
media_vendas = total_vendas / 6

acima_media = 0

for valor in meses:
    if valor > media_vendas:
        acima_media += 1

print("--------------")
print(f"Total de vendas: R$ {total_vendas:.2f}")
print(f"Média das vendas: R$ {media_vendas:.2f}")
print("Quantidade de meses com vendas acima da média:", acima_media)