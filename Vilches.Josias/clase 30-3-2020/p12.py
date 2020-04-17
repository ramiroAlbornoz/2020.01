fras = input("Introduce una frase: \n")
let = input("Introduce una letra: \n")
cantidad = 0
for i in fras:
    if i == let:
        cantidad += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (let, cantidad, fras))