numeros = []

print("---- Digite 5 números ----")

for i in range(1,6):
    numeros.append(int(input(f"Número {i}: ")))

print()
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
print("Média:", sum(numeros) / 5)
    
