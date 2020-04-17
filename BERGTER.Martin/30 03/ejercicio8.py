n = int(input("Introduce la altura del triángulo: "))
for i in range(1, n+1, 2):
    for a in range(i, 0, -2):
        print(a, end=" ")
    print("")