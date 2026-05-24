valores = []
print("---- Digite 20 valores ----")

for i in range(1, 21):
    valores.append(float(input(f"Valor {i}: ")))

print("Média dos valores: ", sum(valores) / 20)