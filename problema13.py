from fractions import Fraction

numero = int(input("Digite un numero: "))

for i in range(1, numero+1):
    fraccion1 = Fraction(1, i)
    fraccion2 = Fraction(1, i+1)
    
    print(f"{fraccion1} - {fraccion2}")