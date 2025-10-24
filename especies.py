from .mamifero import Mamifero
from .ave import Ave
from .reptil import Reptil
from .pez import Pez

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
