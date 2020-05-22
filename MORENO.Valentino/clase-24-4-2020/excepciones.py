class EdadError(Exception):
    pass

while True:
    try:
        edad = int(input("Escribe tu edad: "))
        if edad > 122:
            raise ValueError
        break
    except ValueError:
        print("Debes agregar un numero!")
    except EdadError:
        print("Ingrese un numero entr 1 y 122")
    finally:
        print("Esto siempre se ejecuta")
        
if edad >= 18:
    print("Eres un adulto.")
else:
    print("Aun no eres un adulto")