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
    rectangle = Rectangle(5, 3)
    circle = Circle(2)

    print_metrics(rectangle)
    print_metrics(circle)
