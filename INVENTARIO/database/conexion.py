import sqlite3
import os


# ============================================================
# UBICACIÓN DEL PROYECTO
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


# ============================================================
# CARPETA DATABASE
# ============================================================

CARPETA_DATABASE = os.path.join(
    BASE_DIR,
    "database"
)


# ============================================================
# ARCHIVO DE BASE DE DATOS
# ============================================================

DB_PATH = os.path.join(
    CARPETA_DATABASE,
    "inventario.db"
)


# ============================================================
# CONEXIÓN A LA BASE DE DATOS
# ============================================================

def conectar_bd():

    os.makedirs(
        CARPETA_DATABASE,
        exist_ok=True
    )

    conexion = sqlite3.connect(DB_PATH)

    conexion.execute(
        "PRAGMA foreign_keys = ON"
    )

    return conexion


# ============================================================
# CREAR TABLAS
# ============================================================

def crear_tablas():

    conexion = conectar_bd()

    cursor = conexion.cursor()


    # ========================================================
    # CATEGORÍAS
    # ========================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (

            id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL UNIQUE,

            descripcion TEXT,

            activo INTEGER NOT NULL DEFAULT 1
        )
    """)


    # ========================================================
    # MARCAS
    # ========================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS marcas (

            id_marca INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL UNIQUE,

            activo INTEGER NOT NULL DEFAULT 1
        )
    """)


    # ========================================================
    # TIPOS DE FRAGANCIA
    # ========================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tipos_fragancia (

            id_tipo INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL UNIQUE,

            descripcion TEXT,

            activo INTEGER NOT NULL DEFAULT 1
        )
    """)


    # ========================================================
    # GÉNEROS
    # ========================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS generos (

            id_genero INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL UNIQUE,

            activo INTEGER NOT NULL DEFAULT 1
        )
    """)


    # ========================================================
    # PRESENTACIONES
    # ========================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS presentaciones (

            id_presentacion INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL UNIQUE,

            activo INTEGER NOT NULL DEFAULT 1
        )
    """)


    # ========================================================
    # PRODUCTOS
    # ========================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (

            id_producto INTEGER PRIMARY KEY AUTOINCREMENT,

            codigo TEXT UNIQUE,

            codigo_barras TEXT UNIQUE,

            nombre TEXT NOT NULL,

            id_categoria INTEGER,

            id_marca INTEGER,

            id_tipo INTEGER,

            id_genero INTEGER,

            id_presentacion INTEGER,

            unidad_medida TEXT,

            descripcion TEXT,

            imagen TEXT,

            precio_compra REAL NOT NULL DEFAULT 0,

            precio_venta REAL NOT NULL DEFAULT 0,

            iva REAL NOT NULL DEFAULT 0,

            activo INTEGER NOT NULL DEFAULT 1,

            fecha_creacion DATETIME
                DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (
                id_categoria
            )
            REFERENCES categorias (
                id_categoria
            ),

            FOREIGN KEY (
                id_marca
            )
            REFERENCES marcas (
                id_marca
            ),

            FOREIGN KEY (
                id_tipo
            )
            REFERENCES tipos_fragancia (
                id_tipo
            ),

            FOREIGN KEY (
                id_genero
            )
            REFERENCES generos (
                id_genero
            ),

            FOREIGN KEY (
                id_presentacion
            )
            REFERENCES presentaciones (
                id_presentacion
            )
        )
    """)


    # ========================================================
    # INVENTARIO
    # ========================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventario (

            id_inventario INTEGER PRIMARY KEY AUTOINCREMENT,

            id_producto INTEGER NOT NULL UNIQUE,

            stock_actual REAL NOT NULL DEFAULT 0,

            stock_minimo REAL NOT NULL DEFAULT 0,

            stock_maximo REAL NOT NULL DEFAULT 0,

            ubicacion TEXT,

            FOREIGN KEY (
                id_producto
            )
            REFERENCES productos (
                id_producto
            )
            ON DELETE CASCADE
        )
    """)


    # ========================================================
    # MOVIMIENTOS
    # ========================================================

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimientos_inventario (

            id_movimiento INTEGER PRIMARY KEY AUTOINCREMENT,

            id_producto INTEGER NOT NULL,

            tipo_movimiento TEXT NOT NULL,

            cantidad REAL NOT NULL,

            stock_anterior REAL NOT NULL,

            stock_nuevo REAL NOT NULL,

            motivo TEXT,

            usuario TEXT,

            fecha DATETIME
                DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (
                id_producto
            )
            REFERENCES productos (
                id_producto
            )
        )
    """)
        # ========================================================
    # ACTUALIZAR TABLA PRODUCTOS
    # ========================================================

    # Obtener las columnas que actualmente tiene productos
    cursor.execute("""
        PRAGMA table_info(productos)
    """)

    columnas_productos = [
        fila[1]
        for fila in cursor.fetchall()
    ]


    # Agregar tipo de fragancia
    if "id_tipo" not in columnas_productos:

        cursor.execute("""
            ALTER TABLE productos
            ADD COLUMN id_tipo INTEGER
        """)


    # Agregar género
    if "id_genero" not in columnas_productos:

        cursor.execute("""
            ALTER TABLE productos
            ADD COLUMN id_genero INTEGER
        """)


    # Agregar presentación
    if "id_presentacion" not in columnas_productos:

        cursor.execute("""
            ALTER TABLE productos
            ADD COLUMN id_presentacion INTEGER
        """)


    # ========================================================
    # DATOS INICIALES
    # ========================================================

    # TIPOS DE FRAGANCIA

    tipos = [
        ("Perfume", "Alta concentración de esencia"),
        ("Eau de Parfum", "Concentración intermedia-alta"),
        ("Eau de Toilette", "Concentración intermedia"),
        ("Eau de Cologne", "Concentración ligera")
    ]

    for nombre, descripcion in tipos:

        cursor.execute(
            """
            INSERT OR IGNORE INTO tipos_fragancia
            (nombre, descripcion)
            VALUES (?, ?)
            """,
            (nombre, descripcion)
        )


    # ========================================================
    # GÉNEROS
    # ========================================================

    generos = [
        "Hombre",
        "Mujer",
        "Unisex"
    ]

    for nombre in generos:

        cursor.execute(
            """
            INSERT OR IGNORE INTO generos
            (nombre)
            VALUES (?)
            """,
            (nombre,)
        )


    # ========================================================
    # PRESENTACIONES
    # ========================================================

    presentaciones = [
        "30 ml",
        "50 ml",
        "75 ml",
        "100 ml",
        "125 ml",
        "150 ml",
        "200 ml"
    ]

    for nombre in presentaciones:

        cursor.execute(
            """
            INSERT OR IGNORE INTO presentaciones
            (nombre)
            VALUES (?)
            """,
            (nombre,)
        )


    # ========================================================
    # GUARDAR
    # ========================================================

    conexion.commit()

    conexion.close()


# ============================================================
# PRUEBA DIRECTA
# ============================================================

if __name__ == "__main__":

    crear_tablas()

    print(
        "Base de datos actualizada correctamente."
    )