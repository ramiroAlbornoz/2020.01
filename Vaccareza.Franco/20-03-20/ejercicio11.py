inversion = float(input(" Inversion: "))
interes = float(input(" Interés porcentual anual: "))
ano = int(input(" Años: "))
print("Capital final: " + str(round(inversion * (interes / 100 + 1) ** ano, 2)))