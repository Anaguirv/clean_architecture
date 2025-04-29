# 01. Encapsulation and Abstractions

## Encapsulamiento
Uno de los pilares de la POO, se utiliza para ocultar los detalles de implementación y exponer únicamente los métodos que el usuario necesita.

```
class Circle:
    
    def __init__(self, radio: float):
        self.radio = radio

    def __get_pi(self):
        return 3.1416
    
    def area(self):
        return self.__get_pi() * self.radio ** 2
    
if __name__ == '__main__':
    circle = Circle(10)
    print(circle.area())

    print(circle._Circle__get_pi())
```
Python simula un método privado agregando un doble guion bajo en el nombre, como por ejemplo  **__get_pi(self)** y esto hace que no este disponible para ser invocado por el usuario, aunque en realidad como python solo simula la protección y privacidad, se puede acceder igualmente a el indicando el nombre de clase y metodo al cual se quiere acceder, como se realiza en **print(circle._Circle__get_pi())**. 

## Abstracción

