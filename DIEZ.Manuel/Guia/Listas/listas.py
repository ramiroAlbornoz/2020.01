print("Ejemplo1:  ")
complex_list = [["a", ["b", ["c", "x"]]]]
print(complex_list[0])
print(complex_list[0][1][1][0])
print("")

print("ejemplo2: ")
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio"]
meses.extend(["agosto", "septiembre", "octubre", "noviembre", "diciembre"])
for element in meses:
    print(element, end=" - ")
print("")

print("ejemplo3: ")

meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio"]
meses.extend(["agosto", "septiembre", "octubre", "noviembre", "diciembre"])
tupla = (meses)
for element in meses:
    print(element, end=" - ")

meses.remove("abril")

for element in meses:
    print(element, end=" - ")
print("")

print("")

print("ejemplo4:  ")

def show list(lista):
    