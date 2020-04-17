inversion = float(input(" Inversión inicial: "))
interes = 0.04
balance1 = inversion * (1 + interes)
print(" Balance primer año: " + str(round(balance1, 2)))
balance2 = balance1 * (1 + interes)
print(" Balance segundo año: " + str(round(balance2, 2)))
balance3 = balance2 * (1 + interes)
print(" Balance tercer año: " + str(round(balance3, 2)))