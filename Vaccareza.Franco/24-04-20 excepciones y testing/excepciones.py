class EdadError(Exception):
    pass
​
while True:
    try:
        edad = int(input("Escribe tu edad: "))
        if edad < 1 or edad > 122:
            raise EdadError
        break
    except ValueError:
        print("¡Debes ingresar un número!")
    except EdadError:
        print("Ingrese un valor entre 1 y 122")
    finally:
        print("Esto siempre se ejecuta")
​
if edad >= 18:
    print("Eres un adulto.")
else:
    print("Aún no eres un adulto.")