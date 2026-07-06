from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, nombre, documento):
        self._nombre = nombre
        self._documento = documento

    @property
    def nombre(self):
        return self._nombre

    @property
    def documento(self):
        return self._documento

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @documento.setter
    def documento(self, documento):
        self._documento = documento

    @abstractmethod
    def mostrar_info(self):
        pass