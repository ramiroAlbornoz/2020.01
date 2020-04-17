ne = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while ne % i != 0:
    i += 1
if i == ne:
    print(str(ne) + " es primo")
else:
    print(str(ne) + " no es primo")