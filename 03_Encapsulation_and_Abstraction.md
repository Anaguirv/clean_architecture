# Encapsulation and Abstraction
Aunque ambos conceptos buscan simplificar la interacción con un objeto al “ocultar” detalles internos, su foco y alcance son distintos:

### 1. Naturaleza del concepto
- **Abstracción**
 
  - Se centra en qué hace un componente, no en cómo lo hace.

  - Define una interfaz o un conjunto de operaciones de alto nivel (ej. la clase Shape en Cosmic Python).

  - Es un modelo mental: resalta los atributos y comportamientos relevantes al dominio, dejando fuera todo lo superfluo.

- **Encapsulamiento**

    - Se ocupa de cómo se protegen y mantienen ocultos los datos y la implementación interna.

    - Impone una barrera entre el estado interno (atributos y métodos “privados”) y el exterior.

  - Garantiza invarianza: controla el acceso y las modificaciones al estado interno.

### 2. Objetivo principal
| Aspecto       | Abstracción                                 | Encapsulamiento                                                         |
| ------------- | ------------------------------------------- | ----------------------------------------------------------------------- |
| Propósito     | Simplificar la complejidad del dominio      | Proteger la integridad interna de un objeto                             |
| Exposición    | Sólo la interfaz relevante al usuario       | Sólo los métodos y atributos permitidos (públicos)                      |
| Cambio futuro | Cambiar implementación sin afectar interfaz | Cambiar detalles internos sin romper la lógica de validación/exposición |


### 3. Ejemplo práctico
```python
from abc import ABC, abstractmethod

class Account(ABC):
    """Abstracción: sólo define operaciones."""
    @abstractmethod
    def deposit(self, amount: float): ...
    @abstractmethod
    def withdraw(self, amount: float): ...


class BankAccount(Account):
    def __init__(self, owner: str, balance: float = 0.0):
        # Encapsulamiento: estado interno “privado”
        self._owner = owner
        self._balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Monto debe ser positivo")
        self._balance += amount

    def withdraw(self, amount: float):
        if amount > self._balance:
            raise ValueError("Fondos insuficientes")
        self._balance -= amount

    # Encapsulado: método interno no expuesto
    def _apply_fee(self):
        self._balance -= 5.0
```
- **Abstracción**: Account define qué operaciones existen (deposit, withdraw), sin detallar cómo se validan o modifican los datos.

- **Encapsulamiento**:

  - Atributos _balance y _owner quedan prote­gidos (convención de Python).

  - Método _apply_fee() es sólo para uso interno; su cambio no afecta al consumidor de BankAccount.

### 4. Relación y complementariedad
1. Primero abstraes el modelo de dominio (interfaz y responsabilidades).

2. Luego encapsulas la implementación concreta, garantizando invarianza y protegiendo la integridad del objeto.

> En términos de Cosmic Python, usarás abstracción para modelar tu dominio con interfaces limpias (por ejemplo, repositorios, servicios de dominio), y encapsulación para mantener tu lógica interna aislada, validando estados y evitando acoplamientos indeseados.

