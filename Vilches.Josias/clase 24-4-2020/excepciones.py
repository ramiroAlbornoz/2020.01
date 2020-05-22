class EdadError(Exception):
    pass

while True:
    try: 
        edad = int(input("Escribe tu edad: "))
        if edad < 1 or edad > 122:
            raise EdadError
        break
    except ValueError:
        print("Debes ingresar un numero bobina!")
    except EdadError:
        print("Bobinaa tenes que ingresar un valor entre 1 y 122!!!!!!!!!!!!!!")
    finally:
        print("Esto siempre se ejecuta champion")

if edad >= 18:
    print("Sos todo un adulto COLEGA")
else:
    print("Aun no eres un adulto colega")
