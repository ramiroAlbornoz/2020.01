
inversion = float(input("¿Cuánto quiere invertir? "))
intereses = float(input("¿Cuánto es su interes anual? "))
años = int(input("¿Años?"))
print("Su capital final es: " + str(round(inversion * (intereses / 100 + 1) ** años, 2)))




