from abc import ABC, abstractmethod


class Persona(ABC):

    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_info(self):
        pass