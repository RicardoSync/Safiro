import mysql.connector
import hashlib
from tkinter import messagebox

# Función para encriptar contraseñas con hash SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Conexión a la base de datos
def conectar_db():
    return mysql.connector.connect(
        host="localhost",        # Cambia esto si usas un host diferente
        user="ciso",       # Cambia a tu usuario de MySQL
        password="ciso",  # Cambia a tu contraseña de MySQL
        database="gestion_escolar"
    )

# Función para crear un nuevo usuario
def crear_usuario(usuario, password, rol_nombre):
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Obtener el ID del rol basado en el nombre del rol
    cursor.execute("SELECT id FROM Roles WHERE nombre = %s", (rol_nombre,))
    rol = cursor.fetchone()
    
    if rol:
        rol_id = rol[0]

        # Insertar nuevo usuario con el hash de la contraseña
        insert_query = """
        INSERT INTO Usuarios (usuario, password, rol_id) 
        VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (usuario, hash_password(password), rol_id))
        conexion.commit()
        messagebox.showinfo("Creacion exitosa", f"Usuario '{usuario}' creado exitosamente con el rol '{rol_nombre}'.")
    else:
        messagebox.showerror("Error!", f"El rol '{rol_nombre}' no existe. Por favor, verifica el nombre del rol.")

    cursor.close()
    conexion.close()
