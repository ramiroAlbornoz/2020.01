horas = float(input("¿Cuántas horas ha trabajado? "))
paga = float(input("¿Cuánto cobra por hora? "))

total = round(horas * paga, 3)
print("Tenés que cobrar $", str(total))



