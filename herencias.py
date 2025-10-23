class animal:
    def __init__(self,especie,nombre):
        self.especie = especie 
        self.nombre = nombre
    def describir(self):
        print(f"es de la especie de los {self.especie} y es un {self.nombre}")    
        

class mamiferos(animal):
    def __init__(self,especie,nombre,edad):
        self.especie = especie 
        self.nombre = nombre
        self.edad = edad


class gato(mamiferos):
    def informacion(self):
        print(f"soy de especie {self.especie} me llamo{self.nombre} y tengo {self.edad} años ")

    def hablar(self):
        print("me gusta la leche")

class aves(animal):
    def __init__(self,especie,nombre,edad):
        self.especie = especie 
        self.nombre = nombre
        self.edad = edad




    
cat = gato("mamifero","gato con botas", "2")
cat.informacion()
cat.hablar()