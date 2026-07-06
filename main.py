from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada

sala = ReservaSala("Sala Premium", 50000)
equipo = AlquilerEquipo("Portátil", 80000)
asesoria = AsesoriaEspecializada("Python", 120000)

print(sala.describir())
print(sala.calcular_costo(3))

print(equipo.describir())
print(equipo.calcular_costo(2))

print(asesoria.describir())
print(asesoria.calcular_costo(2, 0.10))