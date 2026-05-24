diviseis = []
print("---- Digite 8 números inteiros ----")

for i in range(1,9):
    num = int(input(f"Número {i}: "))
    
    if num % 4 == 0:
        diviseis.append(num)

print()
print("Números divisíveis por 4:")
print(*diviseis, sep=", ")   