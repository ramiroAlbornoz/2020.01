class Dog:
    def __init__(self, name="", age=0, raza=""):
        self.name = name
        self.age = age
        self.raza = raza

    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.raza

    def input(self):
        self.name = input ("Ingrese el nombre del perro ")
        self.age = int(input ("Ingrese la edad del perro "))
        self.raza = input ("Ingrese la raza del perro ")
if __name__ == "__main__":
    perro1 = Dog()
    perro2 = Dog("Firulais", 5, "Pitbull")
    print(perro2)
    print(perro1)

