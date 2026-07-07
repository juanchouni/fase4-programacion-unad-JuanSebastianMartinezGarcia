from persona import Persona
from excepciones import (
    ClienteInvalido,
    DocumentoInvalido,
    CorreoInvalido,
    TelefonoInvalido
)

# Clase que representa a un cliente del sistema.
# Hereda los atributos básicos de la clase Persona.
class Cliente(Persona):

    # Constructor de la clase Cliente.
    # Valida que los datos ingresados sean correctos antes de crear el objeto.
    def __init__(self, nombre, documento, correo, telefono):
        super().__init__(nombre, documento)

        # Verifica que el nombre no esté vacío.
        if not nombre.strip():
            raise ClienteInvalido("El nombre no puede estar vacío.")

        # Verifica que el documento contenga únicamente números.
        if not documento.isdigit():
            raise DocumentoInvalido("El documento solo debe contener números.")

        # Valida el formato básico del correo electrónico.
        if "@" not in correo or "." not in correo:
            raise CorreoInvalido("Correo electrónico inválido.")

        # Verifica que el teléfono contenga únicamente números.
        if not telefono.isdigit():
            raise TelefonoInvalido("El teléfono solo debe contener números.")

        self._correo = correo
        self._telefono = telefono

    # Retorna el correo electrónico del cliente.
    @property
    def correo(self):
        return self._correo

    # Retorna el número de teléfono del cliente.
    @property
    def telefono(self):
        return self._telefono

    # Muestra la información del cliente.
    # Implementa el método abstracto heredado de Persona.
    def mostrar_info(self):
        return (
            f"Cliente: {self.nombre}\n"
            f"Documento: {self.documento}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )