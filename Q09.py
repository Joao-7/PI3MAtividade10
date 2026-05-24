n = int(input("Digite um número inteiro positivo: "))
print()

for l in range(n, 0, -1):
    for c in range(l):
        print("*", end="")
    print()
    