import tkinter as tk
from tkinter import font

# Crear ventana
ventana = tk.Tk()
ventana.title("Programa para subir repositorio")
ventana.geometry("450x250")
ventana.configure(bg="#1e1e2f")  # Fondo oscuro

# Crear tipografía gótica personalizada
try:
    fuente_gotica = font.Font(family="Old English Text MT", size=24, weight="bold")
except tk.TclError:
    # Si la fuente gótica no está disponible, usar una similar
    fuente_gotica = font.Font(family="Times", size=24, weight="bold")

# Crear etiqueta con estilo gótico
etiqueta = tk.Label(
    ventana,
    text="Este programa es de Jovany y Axel",
    font=fuente_gotica,
    fg="#ff6f61",   # Color llamativo
    bg="#1e1e2f"
)
etiqueta.pack(pady=50)  # Más espacio vertical para centrar

ventana.mainloop()