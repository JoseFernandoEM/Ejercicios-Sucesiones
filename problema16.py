from fractions import Fraction

numero = int(input("Digite un numero: "))

for i in range(1, numero+1):
    a = 3*(2**(i-1))
    print(a)