c = float(input("¿Cantidad a invertir? "))
i = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
print("capital final " + str(round(c * (i / 100 + 1) ** años, 2)))