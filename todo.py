import mysql.connector
import customtkinter as ctk
import tkinter as tk

# Función para obtener datos de la base de datos
def obtener_datos():
    conn = mysql.connector.connect(
        host="localhost",
        user="ciso",
        password="ciso",
        database="gestion_escolar"
    )
    cursor = conn.cursor()
    query = "SELECT * FROM Alumnos"
    cursor.execute(query)
    alumnos = cursor.fetchall()
    cursor.close()
    conn.close()
    return alumnos

# Función para crear y mostrar los frames
def mostrar_alumnos(alumnos):
    root = tk.Tk()
    root.title("Lista de Alumnos")
    
    for index, alumno in enumerate(alumnos):
        frame = ctk.CTkFrame(root, corner_radius=10)
        frame.pack(pady=5, padx=10, fill="x")
        
        # Crear etiquetas para los campos del alumno
        etiquetas = [
            f"ID: {alumno[0]}",
            f"Nombre: {alumno[1]}",
            f"Fecha de Nacimiento: {alumno[2]}",
            f"Dirección: {alumno[3]}",
            f"Teléfono: {alumno[4]}",
            f"Email: {alumno[5]}",
            f"Año Escolar: {alumno[6]}"
        ]
        
        for etiqueta in etiquetas:
            label = ctk.CTkLabel(frame, text=etiqueta)
            label.pack(pady=2)

    root.mainloop()

# Obtener los datos de los alumnos
alumnos = obtener_datos()

# Mostrar los datos en los frames
mostrar_alumnos(alumnos)
