import customtkinter
from PIL import Image
from backend_creacion_usuarios import crear_usuario

usuario_logo = customtkinter.CTkImage(light_image=Image.open("icons/usuario.png"),
                                      dark_image=Image.open("icons/usuario.png"),
                                      size=(120,130))

tipo_usuario = ['Directivo', 'Docente', 'Alumno', 'Secretaria']


def get_datos():
    usuario = usuario_entry.get()
    password = password_entry.get()
    rol_nombre = tipo_entry.get()
    crear_usuario(usuario, password, rol_nombre)


def windows_usuarios(login):
    login.destroy()
    windows_usuario = customtkinter.CTk()
    windows_usuario.title("Creacion de Usuarios")
    windows_usuario.geometry("750x300")
    windows_usuario.resizable(False, False)
    customtkinter.set_default_color_theme("dark-blue")  # Temas: "blue" (estándar), "green", "dark-blue"

    global usuario_entry, password_entry, tipo_entry

    imagen = customtkinter.CTkLabel(windows_usuario, text="", image=usuario_logo)
    usuario_label = customtkinter.CTkLabel(windows_usuario, text="Usuario", font=("Arial", 15), fg_color="transparent")
    usuario_entry = customtkinter.CTkEntry(windows_usuario, width=200)

    password_label = customtkinter.CTkLabel(windows_usuario, text="Clave", font=("Arial", 15), fg_color="transparent")
    password_entry = customtkinter.CTkEntry(windows_usuario, width=200, show="#")

    tipo_label = customtkinter.CTkLabel(windows_usuario, text="Tipo de Usuario", font=("Arial", 15), fg_color="transparent")
    tipo_entry = customtkinter.CTkComboBox(windows_usuario, width=200, values=tipo_usuario)

    guardar_button = customtkinter.CTkButton(windows_usuario, text="Guardar", height=20, fg_color="royal blue", font=("Arial", 20),
                                        text_color="white", border_color="gray", command=get_datos)

    imagen.grid(column=0, row=0, padx=10, pady=10)
    usuario_label.grid(column=0, row=1, padx=10, pady=10)
    usuario_entry.grid(column=1, row=1, padx=10, pady=10)

    password_label.grid(column=0, row=2, padx=10, pady=10)
    password_entry.grid(column=1, row=2, padx=10, pady=10)

    guardar_button.grid(column=2, row=2, padx=10, pady=10)

    tipo_label.grid(column=2, row=1, padx=10, pady=10)
    tipo_entry.grid(column=3, row=1, padx=10, pady=10)


    windows_usuario.mainloop()
