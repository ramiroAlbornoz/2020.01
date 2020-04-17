inversion = float(input(" inversion ($): "))
interes = float(input(" Interés porcentual anual (%): "))
ano = int(input(" Ano: "))
print(" Capital final: " + str(round(inversion * (interes / 100 + 1) ** ano, 2)))