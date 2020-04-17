n = int(input("Introduce un número entero que sea mas grande que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(n , " es primo")
else:
    print(n , " no es primo")