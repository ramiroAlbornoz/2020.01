letra = input("Introduce una letra: ")
frase = input("Introduce una frase: ")
cantidad = 0

for i in frase:
    if i == letra:
        cantidad += 1

print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, cantidad, frase))




