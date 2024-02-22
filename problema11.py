numero = int(input("Digite un numero: "))

for i in range(1, numero+1):
    posicion = (i-1)*(-1)**i
    print(posicion)