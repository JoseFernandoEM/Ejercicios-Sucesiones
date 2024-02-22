from fractions import Fraction

numero = int(input("Digite un numero: "))

for i in range(1, numero+1):
    denominador = (i+1)*(i+1)
    posicion = Fraction(i, denominador)
    print(posicion)