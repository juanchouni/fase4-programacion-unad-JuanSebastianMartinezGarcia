from excepciones import (
    ReservaInvalida,
    DuracionInvalida,
)

from logger_config import logger


class Reserva:

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        try:

            if self.duracion <= 0:
                raise DuracionInvalida(
                    "La duración debe ser mayor que cero."
                )

        except DuracionInvalida as e:
            logger.error(e)
            raise ReservaInvalida("No fue posible confirmar la reserva.") from e

        else:
            self.estado = "Confirmada"
            logger.info("Reserva confirmada correctamente.")

        finally:
            logger.info("Proceso de confirmación finalizado.")

    def cancelar(self):
        self.estado = "Cancelada"
        logger.info("Reserva cancelada.")

    def procesar(self):
        print("Cliente:", self.cliente.nombre)
        print("Servicio:", self.servicio.nombre)
        print("Estado:", self.estado)