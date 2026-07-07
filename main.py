import tkinter as tk
from tkinter import messagebox

from simulaciones import ejecutar_simulaciones

def ejecutar():
    try:
        ejecutar_simulaciones()
        messagebox.showinfo(
            "Finalizado",
            "Las simulaciones se ejecutaron correctamente.\nRevisa la terminal para ver los resultados."
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Sistema de Gestión de Reservas - Software FJ")
ventana.geometry("500x300")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana,
    text="Sistema de Gestión de Reservas",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=20)

descripcion = tk.Label(
    ventana,
    text="Fase 4 - Programación Orientada a Objetos",
    font=("Arial", 11)
)
descripcion.pack()

boton = tk.Button(
    ventana,
    text="Ejecutar Simulaciones",
    width=25,
    height=2,
    command=ejecutar
)
boton.pack(pady=30)

salir = tk.Button(
    ventana,
    text="Salir",
    width=25,
    command=ventana.destroy
)
salir.pack()

ventana.mainloop()