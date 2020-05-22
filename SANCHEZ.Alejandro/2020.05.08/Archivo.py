# Creamos una clase de prueba
class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido=apellido
    def __str__(self):
        return "%s,%s" %(self.apellido,self.nombre)
# Creamos la lista con los objetos
nombres = ["Héctor","Fernandez"],["Mario","Fernandez"],["Marta","Fernandez"]
personas = []
for n in nombres:
    p = Persona(n[0], n[1])
    personas.append(p)
#Escribimos la lista en el fichero con pickle
import pickle
f = open('personas.pck','wb')
pickle.dump(personas, f)
f.close()
# Leemos la lista del fichero con pickle
f = open('personas.pck','rb')
personas = pickle.load(f)
f.close()
for p in personas:
    print(p)