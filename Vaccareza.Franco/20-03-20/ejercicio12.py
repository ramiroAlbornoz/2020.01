p_payaso = 112
p_muñeca = 75
n_payasos = int(input(" Número de payasos a enviar: "))
n_muñecas = int(input(" Número de muñecas a enviar: "))
p_total = p_payaso * n_payasos + p_muñeca * n_muñecas
print(" Peso total encomienda (g): " + str(p_total))