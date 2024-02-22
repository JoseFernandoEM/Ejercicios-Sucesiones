from fractions import Fraction

numero = int(input("Digite un numero: "))

for i in range(1, numero+1):
    a = (i-1)*(-1)**(i+1)
    b = i
    print(f"{a}/{b}")