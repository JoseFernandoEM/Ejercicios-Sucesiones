from fractions import Fraction

numero = int(input("Digite un numero: "))

for i in range(1, numero+1):
    a = (i)*(i)
    b = 3**i
    print(f"{a}/{b}")