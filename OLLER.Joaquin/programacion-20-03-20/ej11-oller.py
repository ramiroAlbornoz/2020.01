cantidad = float(input("Cuanto quiere invertir? "))
interes = float(input("Interes porcentual anual:  "))
años = int(input("Cuantos años desea invertir? "))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))