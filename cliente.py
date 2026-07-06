from persona import Persona
from excepciones import (
    ClienteInvalido,
    DocumentoInvalido,
    CorreoInvalido,
    TelefonoInvalido
)


class Cliente(Persona):

    def __init__(self, nombre, documento, correo, telefono):
        super().__init__(nombre, documento)

        if not nombre.strip():
            raise ClienteInvalido("El nombre no puede estar vacío.")

        if not documento.isdigit():
            raise DocumentoInvalido("El documento solo debe contener números.")

        if "@" not in correo or "." not in correo:
            raise CorreoInvalido("Correo electrónico inválido.")

        if not telefono.isdigit():
            raise TelefonoInvalido("El teléfono solo debe contener números.")

        self._correo = correo
        self._telefono = telefono

    @property
    def correo(self):
        return self._correo

    @property
    def telefono(self):
        return self._telefono

    def mostrar_info(self):
        return (
            f"Cliente: {self.nombre}\n"
            f"Documento: {self.documento}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )