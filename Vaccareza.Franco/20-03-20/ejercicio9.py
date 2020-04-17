peso = input(" Peso (en kg): ")
estatura = input(" Estatura (en metros): ")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))