class Simple():
    def __init__(self,value=0):
        self.value=value
    
    @property
    #getter
    def value(self):
        return self._value



    @value.setter
    #setter
    def value(self,value):
        if value<0:
            print("No u")
        self._value=value

if __name__ == '__main__':
    objeto = Simple(0)
    objeto.value = -3
    print(objeto.__dict__)