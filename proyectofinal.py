import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk # Necesita instalar pillow: pip install pillow
import os

# -------------------------
# FUNCIONES (pantallas vacías por ahora)
# -------------------------
def abrir_registro_productos():
    reg = tk.Toplevel()
    reg.title("Registro de Productos")
    reg.geometry("450x450")
    reg.resizable(False, False)

    # Colores
    COLOR_FONDO = "#1E1E1E"
    COLOR_TEXTO = "white"
    COLOR_ENTRADA = "#2D2D2D"
    COLOR_BOTON = "#28A745"

    reg.configure(bg=COLOR_FONDO)

    # Frame principal
    frame = tk.Frame(reg, bg=COLOR_FONDO)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título
    titulo = tk.Label(
        frame,
        text="REGISTRO DE PRODUCTOS",
        font=("Segoe UI", 16, "bold"),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO
    )
    titulo.pack(pady=(0, 20))

    # ID
    lbl_id = tk.Label(
        frame,
        text="ID del Producto",
        font=("Segoe UI", 11),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO
    )
    lbl_id.pack(anchor="w")

    txt_id = tk.Entry(
        frame,
        font=("Segoe UI", 11),
        bg=COLOR_ENTRADA,
        fg="white",
        insertbackground="white"
    )
    txt_id.pack(fill="x", pady=(0, 10))

    # Descripción
    lbl_desc = tk.Label(
        frame,
        text="Descripción",
        font=("Segoe UI", 11),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO
    )
    lbl_desc.pack(anchor="w")

    txt_desc = tk.Entry(
        frame,
        font=("Segoe UI", 11),
        bg=COLOR_ENTRADA,
        fg="white",
        insertbackground="white"
    )
    txt_desc.pack(fill="x", pady=(0, 10))

    # Precio
    lbl_precio = tk.Label(
        frame,
        text="Precio",
        font=("Segoe UI", 11),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO
    )
    lbl_precio.pack(anchor="w")

    txt_precio = tk.Entry(
        frame,
        font=("Segoe UI", 11),
        bg=COLOR_ENTRADA,
        fg="white",
        insertbackground="white"
    )
    txt_precio.pack(fill="x", pady=(0, 10))

    # Categoría
    lbl_categoria = tk.Label(
        frame,
        text="Categoría",
        font=("Segoe UI", 11),
        bg=COLOR_FONDO,
        fg=COLOR_TEXTO
    )
    lbl_categoria.pack(anchor="w")

    txt_categoria = tk.Entry(
        frame,
        font=("Segoe UI", 11),
        bg=COLOR_ENTRADA,
        fg="white",
        insertbackground="white"
    )
    txt_categoria.pack(fill="x", pady=(0, 20))

    # Función guardar
    def guardar_producto():

        id_prod = txt_id.get().strip()
        descripcion = txt_desc.get().strip()
        precio = txt_precio.get().strip()
        categoria = txt_categoria.get().strip()

        if not all([id_prod, descripcion, precio, categoria]):
            messagebox.showwarning(
                "Campos Vacíos",
                "Por favor complete todos los campos."
            )
            return

        try:
            float(precio)
        except ValueError:
            messagebox.showerror(
                "Error",
                "El precio debe ser un número."
            )
            return

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        archivo = os.path.join(BASE_DIR, "productos.txt")

        with open(archivo, "a", encoding="utf-8") as f:
            f.write(
                f"{id_prod}|{descripcion}|{precio}|{categoria}\n"
            )

        messagebox.showinfo(
            "Guardado",
            "Producto registrado correctamente."
        )

        txt_id.delete(0, tk.END)
        txt_desc.delete(0, tk.END)
        txt_precio.delete(0, tk.END)
        txt_categoria.delete(0, tk.END)

        txt_id.focus()

    # Botón
    btn_guardar = tk.Button(
        frame,
        text="💾 Guardar Producto",
        command=guardar_producto,
        bg=COLOR_BOTON,
        fg="white",
        font=("Segoe UI", 11, "bold"),
        padx=10,
        pady=8,
        cursor="hand2",
        relief="flat"
    )

    btn_guardar.pack(fill="x")
       
def abrir_registro_ventas():
   messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes():
   messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
   messagebox.showinfo("Acerca de", "Punto de Venta de RopanProyecto EscolarnVersión 1.0")


# -------------------------
# VENTANA PRINCIPAL
# -------------------------
# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - Ropa")
ventana.geometry("550x700")
ventana.resizable(False, False)

# Colores
COLOR_FONDO = "#1E1E1E"
COLOR_PANEL = "#252526"
COLOR_TEXTO = "#FFFFFF"

ventana.configure(bg=COLOR_FONDO)

# -------------------------
# ENCABEZADO
# -------------------------
frame_encabezado = tk.Frame(
    ventana,
    bg=COLOR_PANEL
)
frame_encabezado.pack(fill="x")

lbl_titulo = tk.Label(
    frame_encabezado,
    text="PUNTO DE VENTA",
    font=("Segoe UI", 22, "bold"),
    bg=COLOR_PANEL,
    fg="white"
)

lbl_titulo.pack(pady=(20, 5))

lbl_subtitulo = tk.Label(
    frame_encabezado,
    text="Sistema de Administración de Ropa",
    font=("Segoe UI", 11),
    bg=COLOR_PANEL,
    fg="#CCCCCC"
)

lbl_subtitulo.pack(pady=(0, 15))

# -------------------------
# LOGO
# -------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    imagen = Image.open(
        os.path.join(BASE_DIR, "logo.png")
    )

    imagen = imagen.resize((220, 220))

    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(
        ventana,
        image=img_logo,
        bg=COLOR_FONDO
    )

    lbl_logo.pack(pady=20)

except:

    lbl_sin_logo = tk.Label(
        ventana,
        text="LOGO DEL SISTEMA",
        font=("Segoe UI", 14, "bold"),
        bg=COLOR_FONDO,
        fg="white"
    )

    lbl_sin_logo.pack(pady=40)

# -------------------------
# CONTENEDOR DE BOTONES
# -------------------------
frame_botones = tk.Frame(
    ventana,
    bg=COLOR_FONDO
)

frame_botones.pack(pady=10)

# Botón Registro Productos
btn_reg_prod = tk.Button(
    frame_botones,
    text="📦 Registro de Productos",
    command=abrir_registro_productos,
    bg="#0078D7",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    cursor="hand2",
    width=25,
    pady=10
)

btn_reg_prod.pack(pady=8)

# Botón Ventas
btn_reg_ventas = tk.Button(
    frame_botones,
    text="💰 Registro de Ventas",
    command=abrir_registro_ventas,
    bg="#28A745",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    cursor="hand2",
    width=25,
    pady=10
)

btn_reg_ventas.pack(pady=8)

# Botón Reportes
btn_reportes = tk.Button(
    frame_botones,
    text="📊 Reportes",
    command=abrir_reportes,
    bg="#FFC107",
    fg="black",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    cursor="hand2",
    width=25,
    pady=10
)

btn_reportes.pack(pady=8)

# Botón Acerca de
btn_acerca = tk.Button(
    frame_botones,
    text="ℹ️ Acerca de",
    command=abrir_acerca_de,
    bg="#6C757D",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    cursor="hand2",
    width=25,
    pady=10
)

btn_acerca.pack(pady=8)

# -------------------------
# PIE DE PÁGINA
# -------------------------
lbl_version = tk.Label(
    ventana,
    text="Versión 1.0 | MQ Académico",
    font=("Segoe UI", 9),
    bg=COLOR_FONDO,
    fg="#AAAAAA"
)

lbl_version.pack(side="bottom", pady=15)

# -------------------------
# INICIAR APP
# -------------------------
ventana.mainloop()