archivo = open('archivos.py', 'r')
while True:
    linea = archivo.readline()
    if not linea:
        break
    print(linea, end='')
archivo.close()