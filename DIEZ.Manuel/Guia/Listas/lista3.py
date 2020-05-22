text = input ("Ingrese una cadena: ")
print (text)
lista  = []
for element in text:
    if element not in lista:
       lista.append(element)
print(lista)
print("")

print("ejemplo2:  ")
def isSorted(elements):
    cantidad = len(elements)
    for i in range(cantidad - 1):
        if elements[i] > elements[i + 1]:
            return False
    return True
numbers = [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]
print(isSorted(numbers))
