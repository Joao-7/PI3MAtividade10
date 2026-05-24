num = input("Número: ")
digito = input("Dígito (0 - 9): ")

qtn_digitos = 0

for d in num:
    if d == digito:
        qtn_digitos += 1
        
print()
print(f"O digito {digito} aparece {qtn_digitos} vezes.")