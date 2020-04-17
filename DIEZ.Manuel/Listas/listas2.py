meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio"]
meses.extend(["agosto", "setiembre", "octubre", "noviembre", "diciembre"])
tupla = (meses)
for element in meses:
    print(element, end=" - ")
print("")
for element in tupla:
    print(element, end=" - ")
print("")

print("ejemplo2: ")

def show_list(lista):
    for element in lista:
        print(element, end=" - ")
    print("")
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio"]
meses.extend(["agosto", "setiembre", "octubre", "noviembre", "diciembre"])
show_list(meses)
meses.remove("abril")
show_list(meses)
text = "Esto es una prueba"
text_list = text.split()
print(text_list)
print("")


print("ejemplo3:  ")

mylist = [5, 3, 2, 4, 1]
print(len(mylist))#Len: Escribe la cantidad de elementos.
print(min(mylist))#Min: escribe el elemento de menor valor
print(max(mylist))#Max: escribe el elemento de mayor valor
print(sum(mylist))#Sum: Suma una lista con un valor que asignes
print("")

print("ejemplo4:  ")
def show_list(lista):
    for element in lista:
        print(element, end = " - ")
    print(" ")
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio"]
meses.extend(["agosto", "setiembre", "octubre", "noviembre", "diciembre"])
show_list(meses)
posicion = meses.index("abril")
print(posicion)