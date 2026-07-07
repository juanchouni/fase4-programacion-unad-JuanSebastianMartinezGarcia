from excepciones import (
    ReservaInvalida,
    DuracionInvalida,
)

from logger_config import logger

# Clase encargada de gestionar las reservas realizadas por los clientes.
class Reserva:

    # Constructor de la clase Reserva.
    # Inicializa el cliente, el servicio, la duración y el estado inicial.
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    # Confirma la reserva validando que la duración sea mayor que cero.
    # Además, registra los eventos mediante el sistema de logging.
    def confirmar(self):
        try:

            # Verifica que la duración ingresada sea válida.
            if self.duracion <= 0:
                raise DuracionInvalida(
                    "La duración debe ser mayor que cero."
                )

        # Captura la excepción específica y la registra en el archivo de logs.
        except DuracionInvalida as e:
            logger.error(e)
            raise ReservaInvalida("No fue posible confirmar la reserva.") from e

        # Si no ocurre ninguna excepción, la reserva se confirma correctamente.
        else:
            self.estado = "Confirmada"
            logger.info("Reserva confirmada correctamente.")

        # Este bloque siempre se ejecuta, independientemente del resultado.
        finally:
            logger.info("Proceso de confirmación finalizado.")

    # Cancela la reserva y actualiza su estado.
    def cancelar(self):
        self.estado = "Cancelada"
        logger.info("Reserva cancelada.")

    # Muestra la información básica de la reserva.
    def procesar(self):
        print("Cliente:", self.cliente.nombre)
        print("Servicio:", self.servicio.nombre)
        print("Estado:", self.estado)