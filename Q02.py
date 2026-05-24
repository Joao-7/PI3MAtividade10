n = int(input("Digite um número: "))
print()
print(f"Múltiplos de {n} de 1 até 10:")

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")