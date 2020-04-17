text = input("Ingrese una cadena: ")
print(text)

lista = []
for element in text:
    if element not in lista:
        lista.append(element)
        print(lista)
print(lista)


