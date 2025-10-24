# Superclase
class Animal:
    def __init__(self, especie, nombre, edad):
        self.especie, self.nombre, self.edad = especie, nombre, edad

    def describir(self): print(f"Soy {self.nombre}, un {self.especie} de {self.edad} años.")
    def hablar(self): print("Sonido genérico de animal...")
    def comer(self): print(f"{self.nombre} está comiendo.")
    def dormir(self): print(f"{self.nombre} está durmiendo.")

# Subclases principales
class Mamifero(Animal):
    def amamantar(self): print(f"{self.nombre} amamanta a sus crías.")
class Ave(Animal):
    def volar(self): print(f"{self.nombre} vuela alto.")
class Reptil(Animal):
    def arrastrarse(self): print(f"{self.nombre} se arrastra.")
class Pez(Animal):
    def nadar(self): print(f"{self.nombre} nada en el agua.")

# Especies específicas
class Gato(Mamifero):
    def hablar(self): print("Miau, me gusta la leche.")
class Perro(Mamifero):
    def hablar(self): print("Guau, soy el mejor amigo del humano.")
class Loro(Ave):
    def hablar(self): print("¡Hola! Soy un loro parlanchín.")
class Aguila(Ave):
    def hablar(self): print("Screeech! (grito de águila).")
class Serpiente(Reptil):
    def hablar(self): print("Sssss... soy una serpiente.")
class Tiburon(Pez):
    def hablar(self): print("Soy un tiburón y domino el océano.")

# Lista de animales
animales = [
    Gato("Mamífero", "Gato con Botas", 2),
    Perro("Mamífero", "Firulais", 5),
    Loro("Ave", "Pepito", 3),
    Aguila("Ave", "Aquila Real", 7),
    Serpiente("Reptil", "Cobra", 4),
    Tiburon("Pez", "Tiburón Blanco", 8)
]

# Ejecución general
for a in animales:
    a.describir(); a.hablar(); a.comer(); a.dormir()
    if isinstance(a, Mamifero): a.amamantar()
    elif isinstance(a, Ave): a.volar()
    elif isinstance(a, Reptil): a.arrastrarse()
    elif isinstance(a, Pez): a.nadar()
    print("."*40)
