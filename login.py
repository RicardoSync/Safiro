import customtkinter
from PIL import Image
import mysql.connector
import hashlib
from tkinter import messagebox
from creacion_usuarios_vista import windows_usuarios
from panel_directivo import panel_de_control
import json


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


# Función para encriptar contraseñas con hash SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Conexión a la base de datos
def conectar_db():

    config = cargar_configuracion()

    return  mysql.connector.connect(
            host=config['host'],
            database=config['database'],
            user=config['user'],
            password=config['password']
        )

# Función para verificar credenciales en la base de datos
def verificar_usuario(usuario, password, tipo_usuario):
    conexion = conectar_db()
    cursor = conexion.cursor(dictionary=True)
    
    # Consulta SQL para obtener el usuario
    query = """
    SELECT Usuarios.usuario, Usuarios.password, Roles.nombre AS rol
    FROM Usuarios
    JOIN Roles ON Usuarios.rol_id = Roles.id
    WHERE Usuarios.usuario = %s
    """
    
    cursor.execute(query, (usuario,))
    resultado = cursor.fetchone()
    
    if resultado:
        hashed_password = resultado["password"]
        rol = resultado["rol"]
        
        # Verificamos la contraseña y el tipo de usuario
        if hash_password(password) == hashed_password and rol == tipo_usuario:
            print(f"Acceso concedido para {usuario} como {tipo_usuario}")

            if tipo_usuario == "Directivo":
                panel_de_control(login)  # Asegúrate de pasar `login` y `usuario_panel`
            else:
                pass

            return True
        else:
            messagebox.showerror("Inicio Incorrecto", "El usuario o tipo de usuario es incorrecto")
            return False
    else:
        messagebox.showerror("Usuario!", "Usuario no encontrado")
        return False

# Imágenes
my_image = customtkinter.CTkImage(light_image=Image.open("icons/logo.png"),
                                  dark_image=Image.open("icons/logo.png"),
                                  size=(120, 130))

# Definimos los tipos de usuario
tipo_usuario = ['Directivo', 'Docente', 'Alumno', 'Secretaria']

# Función para obtener datos desde la interfaz
def get_datos():
    usuario = user_entry.get()
    password = password_entry.get()
    tipo = tipo_usuarop.get()
    
    # Verificar las credenciales en la base de datos
    if verificar_usuario(usuario, password, tipo):
        # Aquí podrías redirigir a la interfaz correspondiente según el rol
        pass

# Configuración de la interfaz gráfica
login = customtkinter.CTk()
login.title("Safiro Login")
login.geometry("500x600")
login.resizable(False, False)
customtkinter.set_appearance_mode("dark")

# Componentes de la interfaz
label_imagen = customtkinter.CTkLabel(login, text="", image=my_image)
label_spacio = customtkinter.CTkLabel(login, text="")

user_label = customtkinter.CTkLabel(login, text="Usuario", fg_color="transparent", font=("Arial", 20))
user_entry = customtkinter.CTkEntry(login, width=250)
label_spacio2 = customtkinter.CTkLabel(login, text="")

password_label = customtkinter.CTkLabel(login, text="Password", fg_color="transparent", font=("Arial", 20))
password_entry = customtkinter.CTkEntry(login, width=250, show="*")

label_spacio3 = customtkinter.CTkLabel(login, text="")

tipo_usuarop_label = customtkinter.CTkLabel(login, text="Tipo Usuario", fg_color="transparent", font=("Arial", 20))
tipo_usuarop = customtkinter.CTkComboBox(login, width=250, values=tipo_usuario)
label_spacio4 = customtkinter.CTkLabel(login, text="")

login_button = customtkinter.CTkButton(login, text="Login", width=250, fg_color="royal blue", font=("Arial", 20),
                                       text_color="white", border_color="gray", command=get_datos)

label_spacio5 = customtkinter.CTkLabel(login, text="")

richard = customtkinter.CTkLabel(login, text="© Richard Escobedo", fg_color="transparent", font=("Monospace", 10))
# Mostrar componentes
label_imagen.pack()
label_spacio.pack()
user_label.pack()
user_entry.pack()
label_spacio2.pack()
password_label.pack()
password_entry.pack()
label_spacio3.pack()
tipo_usuarop_label.pack()
tipo_usuarop.pack()
label_spacio4.pack()
login_button.pack()
label_spacio5.pack()
richard.pack()
login.mainloop()
