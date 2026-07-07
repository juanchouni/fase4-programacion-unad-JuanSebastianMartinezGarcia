from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva

# Función encargada de ejecutar diferentes casos de prueba del sistema.
# Cada simulación verifica el funcionamiento de una característica específica.
def ejecutar_simulaciones():

    # Simulación 1: Creación correcta de un cliente.
    print("\n========== SIMULACIÓN 1 ==========")
    try:
        cliente = Cliente("Juan", "12345", "juan@gmail.com", "3001234567")
        print("Cliente creado correctamente.")
    except Exception as e:
        print(e)

    # Simulación 2: Validación de un nombre vacío.
    print("\n========== SIMULACIÓN 2 ==========")
    try:
        Cliente("", "12345", "juan@gmail.com", "3001234567")
    except Exception as e:
        print(e)

    # Simulación 3: Validación de un documento inválido.
    print("\n========== SIMULACIÓN 3 ==========")
    try:
        Cliente("Juan", "ABC123", "juan@gmail.com", "3001234567")
    except Exception as e:
        print(e)

    # Simulación 4: Validación de un correo electrónico incorrecto.
    print("\n========== SIMULACIÓN 4 ==========")
    try:
        Cliente("Juan", "12345", "correo_malo", "3001234567")
    except Exception as e:
        print(e)

    # Simulación 5: Cálculo del costo de una reserva de sala.
    print("\n========== SIMULACIÓN 5 ==========")
    try:
        sala = ReservaSala("Sala Premium", 50000)
        print("Costo:", sala.calcular_costo(4))
    except Exception as e:
        print(e)

    # Simulación 6: Cálculo del costo de alquiler de un equipo.
    print("\n========== SIMULACIÓN 6 ==========")
    try:
        equipo = AlquilerEquipo("Portátil", 80000)
        print("Costo:", equipo.calcular_costo(2))
    except Exception as e:
        print(e)

    # Simulación 7: Cálculo del costo de una asesoría con descuento.
    print("\n========== SIMULACIÓN 7 ==========")
    try:
        asesoria = AsesoriaEspecializada("Python", 120000)
        print("Costo:", asesoria.calcular_costo(2, 0.15))
    except Exception as e:
        print(e)

    # Simulación 8: Confirmación correcta de una reserva.
    print("\n========== SIMULACIÓN 8 ==========")
    try:
        cliente = Cliente("Laura", "98765", "laura@gmail.com", "3101234567")
        servicio = ReservaSala("Sala A", 60000)
        reserva = Reserva(cliente, servicio, 3)
        reserva.confirmar()
        reserva.procesar()
    except Exception as e:
        print(e)

    # Simulación 9: Intento de confirmar una reserva con duración inválida.
    print("\n========== SIMULACIÓN 9 ==========")
    try:
        cliente = Cliente("Carlos", "55555", "carlos@gmail.com", "3201112233")
        servicio = ReservaSala("Sala B", 70000)
        reserva = Reserva(cliente, servicio, -5)
        reserva.confirmar()
    except Exception as e:
        print(e)

    # Simulación 10: Confirmación y posterior cancelación de una reserva.
    print("\n========== SIMULACIÓN 10 ==========")
    try:
        cliente = Cliente("Ana", "99999", "ana@gmail.com", "3015556677")
        servicio = ReservaSala("Sala VIP", 90000)
        reserva = Reserva(cliente, servicio, 2)
        reserva.confirmar()
        reserva.cancelar()
        reserva.procesar()
    except Exception as e:
        print(e)