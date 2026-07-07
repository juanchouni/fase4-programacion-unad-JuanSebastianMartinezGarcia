"""
Módulo de excepciones personalizadas.

Este archivo contiene todas las excepciones utilizadas por el sistema
de gestión de reservas Software FJ para controlar y reportar errores
durante la ejecución del programa.
"""


class ClienteInvalido(Exception):
    """Se lanza cuando un cliente tiene datos inválidos."""
    pass


class DocumentoInvalido(Exception):
    """Se lanza cuando el documento no es válido."""
    pass


class CorreoInvalido(Exception):
    """Se lanza cuando el correo tiene un formato incorrecto."""
    pass


class TelefonoInvalido(Exception):
    """Se lanza cuando el teléfono no es válido."""
    pass


class ServicioNoDisponible(Exception):
    """Se lanza cuando el servicio solicitado no existe."""
    pass


class ReservaInvalida(Exception):
    """Se lanza cuando una reserva presenta errores."""
    pass


class DuracionInvalida(Exception):
    """Se lanza cuando la duración de una reserva es incorrecta."""
    pass