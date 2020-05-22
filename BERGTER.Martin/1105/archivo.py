import pickle


# Creamos una clase de prueba
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return "%s, %s" % (self.apellido, self.nombre)


# Creamos la lista con los objetos
nombres = ["Hector", "Mario", "Marta"]
apellidos = ["Fernandez", "Guzman", "Kicillof"]
personas = []

for i in range(len(nombres)):
    p = Persona(nombres[i], apellidos[i])
    personas.append(p)

# Escribimos la lista en el fichero con pickle
with open('personas.pck', 'wb') as f:
    pickle.dump(personas, f)

# Leemos la lista del fichero con pickle
with open('personas.pck', 'rb') as f:
    personas = pickle.load(f)

for p in personas:
    print(p)