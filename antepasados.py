n = int(input("Ingrese el número de generaciones (n): "))

resultado = 0

for n in range(1, n+1):
    resultado = 2**n + resultado

print(resultado)