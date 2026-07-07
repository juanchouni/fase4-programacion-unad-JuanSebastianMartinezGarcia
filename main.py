import tkinter as tk
from tkinter import messagebox

from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from simulaciones import ejecutar_simulaciones


def registrar_reserva():
    try:
        cliente = Cliente(
            entry_nombre.get(),
            entry_documento.get(),
            entry_correo.get(),
            entry_telefono.get()
        )

        if servicio_var.get() == "Sala":
            servicio = ReservaSala("Sala Premium", 50000)
        elif servicio_var.get() == "Equipo":
            servicio = AlquilerEquipo("Portátil", 80000)
        else:
            servicio = AsesoriaEspecializada("Python", 120000)

        reserva = Reserva(cliente, servicio, int(entry_duracion.get()))
        reserva.confirmar()

        messagebox.showinfo(
            "Éxito",
            "Reserva registrada correctamente."
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


def ejecutar():
    try:
        ejecutar_simulaciones()
        messagebox.showinfo(
            "Finalizado",
            "Las simulaciones se ejecutaron correctamente.\nRevisa la terminal."
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))


ventana = tk.Tk()
ventana.title("Sistema de Gestión de Reservas")
ventana.geometry("500x500")
ventana.resizable(False, False)

tk.Label(
    ventana,
    text="Sistema de Gestión de Reservas",
    font=("Arial", 16, "bold")
).pack(pady=10)

tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.pack()

tk.Label(ventana, text="Documento").pack()
entry_documento = tk.Entry(ventana, width=40)
entry_documento.pack()

tk.Label(ventana, text="Correo").pack()
entry_correo = tk.Entry(ventana, width=40)
entry_correo.pack()

tk.Label(ventana, text="Teléfono").pack()
entry_telefono = tk.Entry(ventana, width=40)
entry_telefono.pack()

tk.Label(ventana, text="Duración").pack()
entry_duracion = tk.Entry(ventana, width=40)
entry_duracion.pack()

servicio_var = tk.StringVar(value="Sala")

tk.Label(ventana, text="Seleccione un servicio").pack(pady=5)

tk.Radiobutton(
    ventana,
    text="Reserva de Sala",
    variable=servicio_var,
    value="Sala"
).pack()

tk.Radiobutton(
    ventana,
    text="Alquiler de Equipo",
    variable=servicio_var,
    value="Equipo"
).pack()

tk.Radiobutton(
    ventana,
    text="Asesoría Especializada",
    variable=servicio_var,
    value="Asesoria"
).pack()

tk.Button(
    ventana,
    text="Registrar Reserva",
    command=registrar_reserva,
    width=25
).pack(pady=10)

tk.Button(
    ventana,
    text="Ejecutar Simulaciones",
    command=ejecutar,
    width=25
).pack(pady=5)

tk.Button(
    ventana,
    text="Salir",
    command=ventana.destroy,
    width=25
).pack(pady=10)

ventana.mainloop()