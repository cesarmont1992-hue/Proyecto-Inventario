import tkinter as tk
from tkinter import messagebox


# ============================================================
# CONFIGURACIÓN DE LA VENTANA
# ============================================================

ventana = tk.Tk()

ventana.title("Sistema de Inventario")

ventana.geometry("1000x650")

ventana.minsize(900, 600)

ventana.configure(bg="#F5F1EA")


# ============================================================
# CENTRAR VENTANA
# ============================================================

ventana.update_idletasks()

ancho = ventana.winfo_width()
alto = ventana.winfo_height()

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

pos_x = (ancho_pantalla - ancho) // 2
pos_y = (alto_pantalla - alto) // 2

ventana.geometry(
    f"{ancho}x{alto}+{pos_x}+{pos_y}"
)


# ============================================================
# MENÚ LATERAL
# ============================================================

menu = tk.Frame(
    ventana,
    bg="#241F1A",
    width=230
)

menu.pack(
    side="left",
    fill="y"
)

menu.pack_propagate(False)


# ============================================================
# TÍTULO
# ============================================================

titulo = tk.Label(
    menu,
    text="INVENTARIO",
    bg="#241F1A",
    fg="white",
    font=("Arial", 20, "bold")
)

titulo.pack(
    pady=(40, 10)
)


subtitulo = tk.Label(
    menu,
    text="Sistema de Gestión",
    bg="#241F1A",
    fg="#D8C7AE",
    font=("Arial", 10)
)

subtitulo.pack(
    pady=(0, 40)
)


# ============================================================
# ÁREA PRINCIPAL
# ============================================================

contenido = tk.Frame(
    ventana,
    bg="#F5F1EA"
)

contenido.pack(
    side="left",
    fill="both",
    expand=True
)


# ============================================================
# PANTALLA DE INICIO
# ============================================================

titulo_inicio = tk.Label(
    contenido,
    text="Sistema de Inventario",
    bg="#F5F1EA",
    fg="#241F1A",
    font=("Arial", 28, "bold")
)

titulo_inicio.pack(
    pady=(100, 10)
)


descripcion = tk.Label(
    contenido,
    text="Control de productos y existencias",
    bg="#F5F1EA",
    fg="#555555",
    font=("Arial", 13)
)

descripcion.pack()


# ============================================================
# BOTÓN INVENTARIO
# ============================================================

def abrir_inventario():

    messagebox.showinfo(
        "Inventario",
        "Aquí construiremos el módulo de inventario."
    )


boton_inventario = tk.Button(
    menu,
    text="📦  Inventario",
    command=abrir_inventario,
    bg="#3A3028",
    fg="white",
    activebackground="#4A3D32",
    activeforeground="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2",
    height=2
)

boton_inventario.pack(
    fill="x",
    padx=15,
    pady=5
)


# ============================================================
# BOTÓN CONFIGURACIÓN
# ============================================================

def abrir_configuracion():

    messagebox.showinfo(
        "Configuración",
        "Aquí construiremos la configuración del sistema."
    )


boton_configuracion = tk.Button(
    menu,
    text="⚙️  Configuración",
    command=abrir_configuracion,
    bg="#3A3028",
    fg="white",
    activebackground="#4A3D32",
    activeforeground="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2",
    height=2
)

boton_configuracion.pack(
    fill="x",
    padx=15,
    pady=5
)


# ============================================================
# BOTÓN SALIR
# ============================================================

def salir():

    respuesta = messagebox.askyesno(
        "Salir",
        "¿Deseas salir del sistema?"
    )

    if respuesta:
        ventana.destroy()


boton_salir = tk.Button(
    menu,
    text="🚪  Salir",
    command=salir,
    bg="#8C3B3B",
    fg="white",
    activebackground="#A94A4A",
    activeforeground="white",
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2",
    height=2
)

boton_salir.pack(
    side="bottom",
    fill="x",
    padx=15,
    pady=20
)


# ============================================================
# EJECUTAR PROGRAMA
# ============================================================

ventana.mainloop()