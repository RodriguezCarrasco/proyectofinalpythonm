import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk # Necesita instalar pillow: pip install pillow
import os

# -------------------------
# FUNCIONES (pantallas vacías por ahora)
# -------------------------
def abrir_registro_productos():
   messagebox.showinfo("Registro de Productos", "Aquí irá el módulo de registro de productos.")

def abrir_registro_ventas():
   messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes():
   messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
   messagebox.showinfo("Acerca de", "Punto de Venta de RopanProyecto EscolarnVersión 1.0")


# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - Ropa")
ventana.geometry("500x600")
ventana.resizable(False, False)
ventana.configure(bg="black")

# -------------------------
# LOGO
# -------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Abrir imagen
    imagen = Image.open(os.path.join(BASE_DIR, "logo.png"))

    # Cambiar tamaño
    imagen = imagen.resize((250, 250))

    # Convertir imagen para Tkinter
    img_logo = ImageTk.PhotoImage(imagen)

    # Mostrar logo
    lbl_logo = tk.Label(ventana, image=img_logo, bg="black")
    lbl_logo.pack(pady=20)

except Exception as e:
    print("Error cargando logo:", e)

    lbl_sin_logo = tk.Label(
        ventana,
        text="No se encontró el logo",
        font=("Arial", 14),
        bg="black",
        fg="white"
    )
    lbl_sin_logo.pack(pady=40)
# -------------------------
# BOTONES PRINCIPALES
# -------------------------
estilo = ttk.Style()
estilo.configure("TButton", font=("Arial", 12), padding=10)

btn_reg_prod = ttk.Button(ventana, text="Registro de Productos", command=abrir_registro_productos)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = ttk.Button(ventana, text="Registro de Ventas", command=abrir_registro_ventas)
btn_reg_ventas.pack(pady=10)

btn_reportes = ttk.Button(ventana, text="Reportes", command=abrir_reportes)
btn_reportes.pack(pady=10)

btn_acerca = ttk.Button(ventana, text="Acerca de", command=abrir_acerca_de)
btn_acerca.pack(pady=10)


# -------------------------
# INICIO DE LA APP
# -------------------------
ventana.mainloop()