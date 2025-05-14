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