class Animal:
    def __init__(self, especie, nombre, edad):
        self.especie, self.nombre, self.edad = especie, nombre, edad

    def describir(self): print(f"Soy {self.nombre}, un {self.especie} de {self.edad} años.")
    def hablar(self): print("Sonido genérico de animal...")
    def comer(self): print(f"{self.nombre} está comiendo.")
    def dormir(self): print(f"{self.nombre} está durmiendo.")
