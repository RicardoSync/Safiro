import mysql.connector
from mysql.connector import Error
import json
from tkinter import messagebox

def cargar_configuracion():
    """
    Carga la configuración de la base de datos desde un archivo JSON.
    
    Retorna:
    dict: Diccionario con la configuración de la base de datos.
    """
    try:
        with open('config.json', 'r') as archivo:
            configuracion = json.load(archivo)
            return configuracion
    except FileNotFoundError:
        print("El archivo de configuración no se encontró.")
        return None
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return None

def insertar_docente(nombre, email, telefono, direccion, especialidad):
    """
    Inserta un nuevo docente en la tabla Docentes.

    Parámetros:
    nombre (str): Nombre del docente.
    email (str): Correo electrónico del docente.
    telefono (str): Teléfono del docente.
    direccion (str): Dirección del docente.
    especialidad (str): Especialidad del docente.
    """
    config = cargar_configuracion()
    if config is None:
        return

    try:
        # Establecer conexión con la base de datos usando la configuración del archivo JSON
        connection = mysql.connector.connect(
            host=config['host'],
            database=config['database'],
            user=config['user'],
            password=config['password']
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Consulta SQL para insertar un nuevo docente
            sql_insert_query = """
                INSERT INTO Docentes (nombre, email, telefono, direccion, especialidad)
                VALUES (%s, %s, %s, %s, %s)
            """
            # Valores a insertar
            valores = (nombre, email, telefono, direccion, especialidad)
            # Ejecutar la consulta
            cursor.execute(sql_insert_query, valores)
            # Confirmar los cambios
            connection.commit()
            messagebox.showinfo("Exito!", f"Docente {nombre} insertado correctamente.")
    
    except Error as e:
        messagebox.showerror("Error Denisse", f"Error al insertar el docente: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

