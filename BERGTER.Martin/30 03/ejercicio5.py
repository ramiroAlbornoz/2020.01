inicial=float(input("inversion inicial: "))
interes=float(input("interes anual: "))
tiempo=int(input("ingrese cantidad de años: "))
for i in range(tiempo):
    print("año ",i+1)
    ganado=(inicial*interes)
    print("dinero ganado ", ganado)
    inicial+=ganado