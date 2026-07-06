from abc import ABC, abstractmethod


class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        self._nombre = nombre
        self._precio_base = precio_base

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def describir(self):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, horas=1):
        return self.precio_base * horas

    def describir(self):
        return f"Reserva de sala - ${self.precio_base}/hora"


class AlquilerEquipo(Servicio):

    def calcular_costo(self, dias=1):
        return self.precio_base * dias

    def describir(self):
        return f"Alquiler de equipo - ${self.precio_base}/día"


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas=1, descuento=0):
        total = self.precio_base * horas
        return total - (total * descuento)

    def describir(self):
        return f"Asesoría especializada - ${self.precio_base}/hora"