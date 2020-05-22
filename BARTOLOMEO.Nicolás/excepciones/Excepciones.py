while True:
    try:
        edad = int(input("Escribe tu edad: "))
        break
    except ValueError:
        print("¡Debes ingresar un número!")

if edad >= 18:
    print("Eres un adulto.")
else:
    print("Aún no eres un adulto.")