import tkinter as tk
from tkinter import messagebox

# Importación de las clases principales del sistema.
from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from simulaciones import ejecutar_simulaciones


# Función encargada de registrar una nueva reserva desde la interfaz gráfica.
def registrar_reserva():
    try:
        # Se crea un cliente con la información ingresada por el usuario.
        cliente = Cliente(
            entry_nombre.get(),
            entry_documento.get(),
            entry_correo.get(),
            entry_telefono.get()
        )

        # Se determina el tipo de servicio seleccionado.
        if servicio_var.get() == "Sala":
            servicio = ReservaSala("Sala Premium", 50000)
        elif servicio_var.get() == "Equipo":
            servicio = AlquilerEquipo("Portátil", 80000)
        else:
            servicio = AsesoriaEspecializada("Python", 120000)

        # Se crea la reserva y se confirma.
        reserva = Reserva(cliente, servicio, int(entry_duracion.get()))
        reserva.confirmar()

        # Mensaje mostrado cuando la reserva se registra correctamente.
        messagebox.showinfo(
            "Éxito",
            "Reserva registrada correctamente."
        )

    # Si ocurre un error, se muestra un mensaje al usuario.
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Función que ejecuta las simulaciones desarrolladas para el proyecto.
def ejecutar():
    try:
        ejecutar_simulaciones()

        # Mensaje indicando que las simulaciones finalizaron correctamente.
        messagebox.showinfo(
            "Finalizado",
            "Las simulaciones se ejecutaron correctamente.\nRevisa la terminal."
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Creación de la ventana principal de la aplicación.
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Reservas")
ventana.geometry("500x500")
ventana.resizable(False, False)

# Título principal.
tk.Label(
    ventana,
    text="Sistema de Gestión de Reservas",
    font=("Arial", 16, "bold")
).pack(pady=10)

# Campo para ingresar el nombre del cliente.
tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.pack()

# Campo para ingresar el documento.
tk.Label(ventana, text="Documento").pack()
entry_documento = tk.Entry(ventana, width=40)
entry_documento.pack()

# Campo para ingresar el correo electrónico.
tk.Label(ventana, text="Correo").pack()
entry_correo = tk.Entry(ventana, width=40)
entry_correo.pack()

# Campo para ingresar el teléfono.
tk.Label(ventana, text="Teléfono").pack()
entry_telefono = tk.Entry(ventana, width=40)
entry_telefono.pack()

# Campo para ingresar la duración del servicio.
tk.Label(ventana, text="Duración").pack()
entry_duracion = tk.Entry(ventana, width=40)
entry_duracion.pack()

# Variable que almacena el servicio seleccionado.
servicio_var = tk.StringVar(value="Sala")

# Opciones disponibles para seleccionar el servicio.
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

# Botón para registrar una nueva reserva.
tk.Button(
    ventana,
    text="Registrar Reserva",
    command=registrar_reserva,
    width=25
).pack(pady=10)

# Botón para ejecutar las simulaciones del sistema.
tk.Button(
    ventana,
    text="Ejecutar Simulaciones",
    command=ejecutar,
    width=25
).pack(pady=5)

# Botón para cerrar la aplicación.
tk.Button(
    ventana,
    text="Salir",
    command=ventana.destroy,
    width=25
).pack(pady=10)

# Inicia el ciclo principal de la interfaz gráfica.
ventana.mainloop()