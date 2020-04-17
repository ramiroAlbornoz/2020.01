numero = int(input("Altura del triángulo(tiene que ser entero positivo): "))
for i in range(1, numero+1, 2):
    for z in range(i, 0, -2):
        print(z, end=" ")
    print("")



