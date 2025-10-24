from animales.especies import Gato, Perro, Loro, Aguila, Serpiente, Tiburon
from animales.mamifero import Mamifero
from animales.ave import Ave
from animales.reptil import Reptil
from animales.pez import Pez

animales = [
    Gato("Mamífero", "Gato con Botas", 2),
    Perro("Mamífero", "Firulais", 5),
    Loro("Ave", "Pepito", 3),
    Aguila("Ave", "Aquila Real", 7),
    Serpiente("Reptil", "Cobra", 4),
    Tiburon("Pez", "Tiburón Blanco", 8)
]

for a in animales:
    a.describir(); a.hablar(); a.comer(); a.dormir()
    if isinstance(a, Mamifero): a.amamantar()
    elif isinstance(a, Ave): a.volar()
    elif isinstance(a, Reptil): a.arrastrarse()
    elif isinstance(a, Pez): a.nadar()
    print("."*40)
