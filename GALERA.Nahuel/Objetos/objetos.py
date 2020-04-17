class Dog:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        self.raza = "Labrador"

    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.raza


if __name__ == "__main__":
    perro1 = Dog("Firulais", 5)
    perro2 = Dog("Spike", 1)
    

    print("perro1 = "+ perro1.__str__())
    print("perro2 = "+ perro2.__str__())