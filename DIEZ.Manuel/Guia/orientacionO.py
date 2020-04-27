class Dog:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.raza = ""
    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.raza
    def input(self):
        self.name = input("ingrese el nombre del perro: ")
        self.age = int(input("ingrese la edad del perro"))
        self.raza = input("ingrese la raza del perro")
if __name__ == "__main__":
    perro1 = Dog()
    perro2 = Dog()

    perro1.input()
    
    print("perro1 = " + perro1.__str__())
    print("perro2 = " + perro2.__str__())