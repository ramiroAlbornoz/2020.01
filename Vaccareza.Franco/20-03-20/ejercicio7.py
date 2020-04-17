horas_trabajo = float(input("Introducir horas de trabajo: "))
cobro = float(input("Introducir lo que cobra por hora: "))
pago = round(horas_trabajo * cobro, 3)
print("Tu paga es " + str(pago))