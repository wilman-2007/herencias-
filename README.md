# Proyecto de Herencia en Python - Clases de Animales

Este proyecto demuestra el uso de **herencia**, **polimorfismo** y **clases** en Python mediante un sistema jerárquico de animales.  
Cada animal pertenece a una **superclase** (`Animal`) y a una **subclase** más específica (como `Mamifero`, `Ave`, `Reptil`, o `Pez`).

---

## Estructura del Código

### Superclase: `Animal`
Define las propiedades y comportamientos comunes a todos los animales:

```python
class Animal:
    def __init__(self, especie, nombre, edad):
        self.especie, self.nombre, self.edad = especie, nombre, edad

    def describir(self): print(f"Soy {self.nombre}, un {self.especie} de {self.edad} años.")
    def hablar(self): print("Sonido genérico de animal...")
    def comer(self): print(f"{self.nombre} está comiendo.")
    def dormir(self): print(f"{self.nombre} está durmiendo.")
```

---

### Subclases principales
Cada una hereda de `Animal` y añade comportamientos propios:

| Subclase  | Método adicional         | Ejemplo de acción |
|------------|---------------------------|--------------------|
| `Mamifero` | `amamantar()`            | “amamanta a sus crías” |
| `Ave`      | `volar()`                | “vuela alto” |
| `Reptil`   | `arrastrarse()`          | “se arrastra” |
| `Pez`      | `nadar()`                | “nada en el agua” |

---

### 🐾 Especies específicas
Implementan **polimorfismo** sobre el método `hablar()`:

| Clase | Hereda de | Mensaje personalizado |
|--------|------------|------------------------|
| `Gato` | Mamífero | “Miau, me gusta la leche.” |
| `Perro` | Mamífero | “Guau, soy el mejor amigo del humano.” |
| `Loro` | Ave | “¡Hola! Soy un loro parlanchín.” |
| `Aguila` | Ave | “Screeech! (grito de águila).” |
| `Serpiente` | Reptil | “Sssss... soy una serpiente.” |
| `Tiburon` | Pez | “Soy un tiburón y domino el océano.” |

---

## 🚀 Ejecución del Programa

Se crean varias instancias de animales y se recorre una lista para mostrar su comportamiento:

```python
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
```

---

## 💡 Conceptos Destacados

- **Herencia:** permite que las subclases reutilicen y amplíen el comportamiento de `Animal`.
- **Polimorfismo:** cada especie redefine el método `hablar()` a su manera.
- **Encapsulación:** los atributos (`especie`, `nombre`, `edad`) están contenidos dentro de cada objeto.
- **Abstracción:** el usuario interactúa con los métodos sin preocuparse por la implementación interna.

---

## 🧪 Ejemplo de salida

```
Soy Gato con Botas, un Mamífero de 2 años.
Miau, me gusta la leche.
Gato con Botas está comiendo.
Gato con Botas está durmiendo.
Gato con Botas amamanta a sus crías.
........................................
Soy Firulais, un Mamífero de 5 años.
Guau, soy el mejor amigo del humano.
...
```

---

## 🛠️ Cómo ejecutar

1. Guarda el archivo como `animales.py`
2. Abre tu terminal o consola (en PC o PyDroid)
3. Ejecuta el siguiente comando:

```bash
python animales.py
```

---

## 📄 Autor

**Wilman Porto Cárcamo**  
Proyecto educativo para practicar **Programación Orientada a Objetos (POO)** en **Python**.
