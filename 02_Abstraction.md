# Abstracción


La **abstracción** es otro pilar de la Programación Orientada a Objetos. Su objetivo es ocultar la complejidad de la implementación y presentar únicamente una interfaz sencilla y relevante al usuario o a otras partes del sistema.  

- **¿Qué es?**  
  - Separar el “qué” (la interfaz y comportamiento esperado) del “cómo” (la implementación interna).  
  - Permitir a quien consume la clase o módulo trabajar con conceptos de alto nivel, sin preocuparse por detalles internos.

- **¿Por qué usarla?**  
  - Facilita la comprensión y el mantenimiento del código.  
  - Permite cambiar la implementación interna sin afectar al código que depende de la interfaz.  
  - Refuerza el diseño orientado al dominio, enfocándose en los conceptos relevantes del negocio.

## Ejemplo en Python usando `abc`

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Interfaz abstracta para distintas figuras geométricas."""

    @abstractmethod
    def area(self) -> float:
        """Calcular el área de la figura."""
        ...

    @abstractmethod
    def perimeter(self) -> float:
        """Calcular el perímetro de la figura."""
        ...


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.1416 * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.1416 * self.radius


def print_metrics(shape: Shape):
    """Función de alto nivel que solo conoce la interfaz Shape."""
    print(f"Área: {shape.area():.2f}")
    print(f"Perímetro: {shape.perimeter():.2f}")


if __name__ == "__main__":
    r = Rectangle(5, 3)
    c = Circle(2)

    print_metrics(r)
    print_metrics(c)
