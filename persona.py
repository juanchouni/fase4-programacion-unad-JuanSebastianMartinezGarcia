from abc import ABC, abstractmethod

# Clase abstracta que representa a una persona dentro del sistema.
# Esta clase sirve como base para otras clases, como Cliente.
class Persona(ABC):

    # Constructor de la clase Persona.
    # Inicializa el nombre y el documento de la persona.
    def __init__(self, nombre, documento):
        self._nombre = nombre
        self._documento = documento

    # Obtiene el nombre de la persona.
    @property
    def nombre(self):
        return self._nombre

    # Obtiene el documento de la persona.
    @property
    def documento(self):
        return self._documento

    # Permite modificar el nombre de la persona.
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Permite modificar el documento de la persona.
    @documento.setter
    def documento(self, documento):
        self._documento = documento

    # Método abstracto que debe ser implementado por las clases hijas.
    @abstractmethod
    def mostrar_info(self):
        pass