from excepciones import CorreoInvalido

try:
    raise CorreoInvalido("Correo incorrecto.")
except CorreoInvalido as e:
    print(f"Error capturado: {e}")