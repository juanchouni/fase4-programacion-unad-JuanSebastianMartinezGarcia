from abc import ABC, abstractmethod

# Clase abstracta que representa un servicio ofrecido por el sistema.
# Define los atributos y métodos que deberán implementar las clases hijas.
class Servicio(ABC):

    # Constructor de la clase Servicio.
    # Inicializa el nombre y el precio base del servicio.
    def __init__(self, nombre, precio_base):
        self._nombre = nombre
        self._precio_base = precio_base

    # Retorna el nombre del servicio.
    @property
    def nombre(self):
        return self._nombre

    # Retorna el precio base del servicio.
    @property
    def precio_base(self):
        return self._precio_base

    # Método abstracto para calcular el costo del servicio.
    # Cada clase derivada implementa su propia forma de cálculo.
    @abstractmethod
    def calcular_costo(self):
        pass

    # Método abstracto para describir el servicio.
    @abstractmethod
    def describir(self):
        pass


# Clase que representa el servicio de reserva de salas.
class ReservaSala(Servicio):

    # Calcula el costo de la reserva según la cantidad de horas.
    def calcular_costo(self, horas=1):
        return self.precio_base * horas

    # Retorna una descripción del servicio.
    def describir(self):
        return f"Reserva de sala - ${self.precio_base}/hora"


# Clase que representa el servicio de alquiler de equipos.
class AlquilerEquipo(Servicio):

    # Calcula el costo del alquiler según la cantidad de días.
    def calcular_costo(self, dias=1):
        return self.precio_base * dias

    # Retorna una descripción del servicio.
    def describir(self):
        return f"Alquiler de equipo - ${self.precio_base}/día"


# Clase que representa el servicio de asesorías especializadas.
class AsesoriaEspecializada(Servicio):

    # Calcula el costo de la asesoría aplicando un descuento opcional.
    def calcular_costo(self, horas=1, descuento=0):
        total = self.precio_base * horas
        return total - (total * descuento)

    # Retorna una descripción del servicio.
    def describir(self):
        return f"Asesoría especializada - ${self.precio_base}/hora"