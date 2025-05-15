# Modelo del Dóminio

Concepto utilizado para constuir un modelo de objeto que este muy nutrido de la logica de negocio haciendo uso del TDD.

## ¿Qué es el Dominio?
En terminos simples:
> Es la parte del software que representa el conocimiento central del negocio que se esta modelando, es decir, la lógica y reglas fundamentales del sistema, **lo que hace que el software tenga sentido y funcione para su propósito real**.

En Cosmic Python, los autores utilizan como ejemplo un sistema para almacenes de productos y envios (inventory and shipping system).

En ese sistema, el **dominio** incluye cosas como:
- Los productos que se pueden enviar.
- Los lotes (batches) de inventario.
- Los pedidos de clinetes.
- La lógica que decide qué lote se debe usar para asignar un producto a un pedido.

**¡Eso es Domino!** Las reglas del negocio, no los detalles técnicos.

## ¿Qué no es Dominio?
No forma parte del domino:
- Cómo se guardan los datos (Base de datos, SQL, ORM, etc).
- Cómo se comunican los componentes(API, HTTP, mensajería).
- Cómo se presentan los datos (HTML, CLI, GUI).

## ¿Por qué es importante?
Separar el dominio de los detalles técnicos nos da:
- **Claridad**: El corazon del sistema esta en un lugar limpio y entendible.

- **Testeabilidad**: Podemos probar reglas del negocio sin conectar a DB ni servidores.
  
- **Flexibilidad**: Podemos cambiar el almacenamiento o interfaz grafica sin afectar el modelo central.

## En resumen
| Concepto         | Dominio                                                          |
| ---------------- | ---------------------------------------------------------------- |
| ¿Qué es?         | Lógica de negocio principal, reglas y conocimiento del sistema   |
| ¿Dónde vive?     | En una capa aislada del código (por ejemplo, `domain/`)          |
| ¿Para qué sirve? | Para mantener la lógica central clara, testeable y desacoplada   |
| ¿Ejemplo?        | Cómo asignar pedidos a lotes, cómo calcular disponibilidad, etc. |


# Domain Driven Desing (DDD)
Muchas vences al desarrollar un nuevo sistema comenzamos por el diseño de la base de datos, el problema en pensar en los dato primero es que ahi se genera en acoplamiento, ya que, todo lo que hacemos para diseñar el modelo de datos es técnico y en lugar de pensar en el comportamiento del sistema, pensamos en los requerimientos de almacenamiento, con esto hacemos que todo se acople a la infraestructura.

> "Al cliente no le interesa el modelo de datos, de lo contrario solo utilizarian un excel" - Cosmic Python

DDD nos invita a pensar en el comportamiento y no en los datos.

## ¿Qué es el Domain-Driven Desing?
Es una filosofia de diseño de software creada por Eric Evans en su libro *"Domain Driven Desgin: Tackling Complexity in heart of sofware"*

Su objetivo principal es:
> **Poner el dominio del negocio en el centro del diseño del software**, facilitando que los desarrolladores y expertos del negocio hablen el mismo idioma y trabajen juntos.
>
## Principios fundamentales del DDD
1. **Modelar el Dominio junto al experto**:
El software debe representar fielmente como funciona el negocio. Por eso, los desarrolladores deben trabajar codo a codo con los expertos del dominio (ej. cajeros, cocineros, gerentes de restaurant) para entender los procesos reales.
    > "El código debe contar la misma historia que te cuenta el experto del negocio."

2. **Lenguaje ubicuo**: Todo el equipo debe usar el **mismo vocabulario** cuando se refiere a elementos del sistema.

    Ejemplo en un sistema de restaurante:
    - **Correcto**: Un pedido contiene platillos  y puede ser servido o cancelado.
    - **Incorrecto**: El objeto OrderDataModel tiene un campo status_flag con valor 4.
  
    El lenguaje debe estar **reflejado en el código**, en nombres de clases, métodos y módulos. 
    
3. **Modelo rico**: Las clases del dominio deben tener comportamiento, no solo datos 

    **Mala práctica (modelo anémico)**:
    ```py
    class Pedido:
        def __init__(self, estado):
            self.estado = estado
    ```
    **Mejor**:
    ```py
    class Pedido:
        def confirmar(self):
            self.estado = "confirmado"
    ```
    **No solo representes *qué* es algo, define *qué puede hacer* ese algo**

**4. Separacion de responsabilidades**:
DDD prompon diferenciar claramente las capas del sistema, para que cada una tenga un propósito único. Una forma de organizarlo es con la arquitectura limpia.

```scss
[ Interfaces / Infraestructura ] ← base de datos, APIs
        ↓
[ Aplicación ] ← orquestación de casos de uso
        ↓
[ Dominio ] ← lógica de negocio pura (modelo rico)

```
**5. Desacoplamiento de la insfraestructura**:
> "Si diseñamos primero la base de datos, todo queda aclopado a la base de datos "

DDD recomienda **modelar primero el dominio**, y después usar patrones como **puertos y adaptadores** o **repositorios** para conectarlo a la infraestructura.

## Componentes comunes de un sistema DDD
| Componente                             | Rol                                                                  |
| -------------------------------------- | -------------------------------------------------------------------- |
| Entidad (`Entity`)                     | Tiene identidad propia y ciclo de vida. Ej: `Pedido`                 |
| Objeto de Valor (`Value Object`)       | No tiene identidad, solo datos. Ej: `Dinero`, `Dirección`            |
| Agregado (`Aggregate`)                 | Raíz de un grupo de entidades. Ej: `Pedido` controla sus `Platillos` |
| Repositorio (`Repository`)             | Guarda y recupera agregados desde la infraestructura                 |
| Servicio de Dominio (`Domain Service`) | Lógica que no encaja en una entidad. Ej: asignar pedidos             |

## Cómo se une esto a TDD 
DDD y TDD van de la mano:
- Primero se define el **comportamiento del dominio**.
- Luego los implementas con clases y métodos.
- Despues se escriben test que ejerciten  esos comportamientos  sin preocuparse aún por DBs o interfaces graficas.

## En resumen
- **DDD no es una arquitectura, sino una forma de pensar**.
- Su meta es que el software modele fielmente **cómo funciona el negocio**.
- Nos permite desarrollar sistemas más limpios, mantenibles y centrados en el valor real. 

## Ejemplo práctico aplicando DDD al dominio de un restaurante
Veras:
1. Entidades (Platillo, Pedido).
2. Objetos de valor (Money, OrderLine).
3. Repositorio (interfaz y una implementación en memoria).
4. Flujo de uso.

### 1. Objetos de valor
```py
# domain/value_objects.py
from dataclasses import dataclass

@dataclass(frozen=True)
class Money:
    amount: float
    currency: str = "MXN"

    def __add__(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("No se pueden sumar distintas divisas")
        return Money(self.amount + other.amount, self.currency)

    def __repr__(self):
        return f"{self.amount:.2f} {self.currency}"
```
### 2. Entidades
```
# domain/entities.py
from uuid import uuid4
from typing import List
from .value_objects import Money, OrderLine

class Platillo:
    def __init__(self, platillo_id: str, nombre: str, precio: Money):
        self.platillo_id = platillo_id
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f"<Platillo {self.platillo_id}: {self.nombre} — {self.precio}>"

```
```py
# domain/entities.py (continuación)
from datetime import datetime

class Pedido:
    def __init__(self, pedido_id: str = None):
        self.pedido_id = pedido_id or str(uuid4())
        self._lineas: List[OrderLine] = []
        self._estado: str = "pendiente"
        self._timestamp = datetime.now()

    def agregar_linea(self, line: OrderLine):
        if line.cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self._lineas.append(line)

    def total(self, menu: dict) -> Money:
        total = Money(0.0)
        for line in self._lineas:
            platillo = menu[line.platillo_id]
            total += Money(platillo.precio.amount * line.cantidad, platillo.precio.currency)
        return total

    def confirmar(self):
        if not self._lineas:
            raise ValueError("No hay platillos en el pedido")
        self._estado = "en preparación"

    @property
    def estado(self):
        return self._estado

    @property
    def lineas(self):
        return list(self._lineas)

```

### 3. Repositorio de pedidos
```py
# domain/repos.py
from abc import ABC, abstractmethod
from .entities import Pedido
from typing import Optional

class PedidoRepository(ABC):
    @abstractmethod
    def save(self, pedido: Pedido) -> None:
        """Guardar o actualizar un pedido."""
        pass

    @abstractmethod
    def get(self, pedido_id: str) -> Optional[Pedido]:
        """Recuperar un pedido por su ID."""
        pass

```
```py
# infrastructure/in_memory_repo.py
from domain.repos import PedidoRepository
from domain.entities import Pedido
from typing import Dict, Optional

class InMemoryPedidoRepository(PedidoRepository):
    def __init__(self):
        self._storage: Dict[str, Pedido] = {}

    def save(self, pedido: Pedido) -> None:
        print(f"→ Repositorio: guardando pedido {pedido.pedido_id}")
        self._storage[pedido.pedido_id] = pedido

    def get(self, pedido_id: str) -> Optional[Pedido]:
        print(f"→ Repositorio: recuperando pedido {pedido_id}")
        return self._storage.get(pedido_id)

```
### 4. Flujo de la aplicación
```py
# app.py
from domain.value_objects import Money, OrderLine
from domain.entities import Platillo, Pedido
from infrastructure.in_memory_repo import InMemoryPedidoRepository

if __name__ == "__main__":
    # 1. Definimos el menú (simulado)
    menu = {
        "p1": Platillo("p1", "Tacos al pastor", Money(75.0)),
        "p2": Platillo("p2", "Agua de horchata", Money(25.0)),
    }

    # 2. Creamos repositorio e instanciamos un pedido
    repo = InMemoryPedidoRepository()
    pedido = Pedido()
    print(f"→ Nuevo pedido con ID: {pedido.pedido_id}")

    # 3. Cajero agrega líneas al pedido
    pedido.agregar_linea(OrderLine("p1", 2))
    pedido.agregar_linea(OrderLine("p2", 1))
    print("→ Lineas del pedido:", pedido.lineas)

    # 4. Confirmar y guardar
    pedido.confirmar()
    print("→ Estado tras confirmar:", pedido.estado)
    repo.save(pedido)

    # 5. Recuperar y calcular total
    fetched = repo.get(pedido.pedido_id)
    if fetched:
        total = fetched.total(menu)
        print(f"→ Total del pedido ({fetched.pedido_id}): {total}")

```
### ¿Qué hemos visto?
- **Entidades**: Pedido y Platillo con identidad y comportamiento.

- **Objetos de Valor**: Money y OrderLine encapsulan datos inmutables.

- **Repositorio**: PedidoRepository como abstracción; InMemoryPedidoRepository como adaptador de infraestructura.

- **Flujo**: la capa de aplicación (app.py) orquesta caso de uso “tomar pedido” sin conocer detalles de almacenamiento.

> Con esto tenemos un esqueleto DDD listo para extender con más entidades, servicios de dominio y adaptadores (por ejemplo, persistencia en base de datos, mensajería a cocina, etc.).