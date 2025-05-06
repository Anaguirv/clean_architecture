from abc import ABC, abstractmethod

# 1. Abstracción
class CanalNotificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass


# 2. Implementación concreta: Email
class ServicioEmail(CanalNotificacion):
    def __init__(self):
        print("→ Se creó un objeto ServicioEmail")

    def enviar(self, mensaje):
        print("→ Ejecutando ServicioEmail.enviar()")
        print(f"[EMAIL] {mensaje}")


# 3. Implementación concreta: SMS
class ServicioSMS(CanalNotificacion):
    def __init__(self):
        print("→ Se creó un objeto ServicioSMS")

    def enviar(self, mensaje):
        print("→ Ejecutando ServicioSMS.enviar()")
        print(f"[SMS] {mensaje}")

class ServicioWhatsApp(CanalNotificacion):
    def __init__(self):
        print("→ Se creo un objeto ServicioWhatsApp")

    def enviar(self, mensaje):
        print("→ Ejecutando ServicioWhatsApp.enviar()")
        print(f"[WhatsApp] {mensaje}")

# 4. Clase de alto nivel
class Notificador:
    def __init__(self, canal: CanalNotificacion):
        print("→ Se creó un objeto Notificador")
        self.canal = canal

    def notificar(self, mensaje):
        print("→ Ejecutando Notificador.notificar()")
        self.canal.enviar(mensaje)


# 5. Bloque principal
if __name__ == "__main__":
    print("== INICIO DE LA EJECUCIÓN ==")

    # Paso 1: Crear un canal de notificación
    canal_email= ServicioEmail()
    canal_sms = ServicioSMS()
    canal_whatsapp = ServicioWhatsApp()

    # Paso 2: Crear el objeto notificador
    notificador1 = Notificador(canal_email)
    notificador2 = Notificador(canal_sms)
    notificador3 = Notificador(canal_whatsapp)

    # Paso 3: Enviar una notificación
    notificador1.notificar("¡Bienvenido al sistema!")
    notificador2.notificar("Código de verificación: 123456")
    notificador3.notificar("Tienes una nueva oferta")

    print("== FIN DE LA EJECUCIÓN ==")
