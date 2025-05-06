# Dependency Inversion Principle (DIP)
Uno de los principios SOLID, su idea principal es:
> Los módulos de alto nivel no deben depender de los módulos de bajo nivel. Ambos deben depender de abstracciones.

- **Módulo de alto nivel**: Contiene la lógica del negocio (reglas de dominio).

- **Módulo de bajo nivel**: Se ocupa de detalles técnicos (acceso a bases de datos, redes, etc).

- **Problema**: Si el alto nivel depende del abna nivel, el dominio queda acoplado a los detalles técnicos.

- **Solución**: Invertir la dependencia haciendo que ambos dependan de una **interfaz (abstracción)**.


## Ejemplo - Escenario: Enviar notificaciones
Queremos que una clase Notificador envíe mensajes a los usuarios. Podría enviarlos por correo electrónico, SMS, WhatsApp, etc. ¿Cómo diseñamos esto para que sea flexible y desacoplado?

### Sin DIP (acoplamiento fuerte)

```py
class EmailService:
    def enviar_email(self, mensaje):
        print(f"Enviando email: {mensaje}")


class Notificador:
    def __init__(self):
        self.email_service = EmailService()

    def notificar(self, mensaje):
        self.email_service.enviar_email(mensaje)


notificador = Notificador()
notificador.notificar("Tu pedido fue enviado")
```
- Notificador depende directamente de EmailService.

- No puedes cambiar a SMS o WhatsApp sin modificar Notificador.

### Aplicando DIP
Primero definimos una interfaz para cualquier tipo de servicio de notificación:
```py
from abc import ABC, abstractmethod

# Abstracción: puerto de salida
class CanalNotificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass
```
Ahora podemos crear múltiples implementaciones:

```py
class ServicioEmail(CanalNotificacion):
    def enviar(self, mensaje):
        print(f"[EMAIL] {mensaje}")

class ServicioSMS(CanalNotificacion):
    def enviar(self, mensaje):
        print(f"[SMS] {mensaje}")

class ServicioWhatsApp(CanalNotificacion):
    def enviar(self, mensaje):
        print(f"[WhatsApp] {mensaje}")

```
Y nuestro Notificador sólo depende de la abstracción, no de la implementación concreta:
```py
class Notificador:
    def __init__(self, canal: CanalNotificacion):
        self.canal = canal

    def notificar(self, mensaje):
        self.canal.enviar(mensaje)

```

### Probamos el sistema:
```py
if __name__ == "__main__":
    canal_sms = ServicioSMS()
    canal_email = ServicioEmail()
    canal_whatsapp = ServicioWhatsApp()

    notificador1 = Notificador(canal_email)
    notificador2 = Notificador(canal_sms)
    notificador3 = Notificador(canal_whatsapp)

    notificador1.notificar("Bienvenido a la app")
    notificador2.notificar("Código de verificación: 123456")
    notificador3.notificar("Tienes una nueva oferta")
```

## ¿Qué logramos con DIP?
- Notificador no depende de detalles técnicos (como Email, SMS, etc.).

- Podemos agregar o cambiar canales sin tocar la lógica de negocio.

- Podemos testear usando una clase CanalNotificacionFalso (fake o mock).