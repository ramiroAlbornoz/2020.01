contra=input("cree contraseña: ")
respuesta=contra + "asdfghjk"
while not(contra == respuesta):
    respuesta=input("ingrese contraseña: ")
print("contraseña ingresada")