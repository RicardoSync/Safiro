import customtkinter 
from PIL import Image
from backend_creacion_docentes import insertar_docente

materias_secundaria = [
    "Español",
    "Matemáticas",
    "Ciencias",
    "Historia",
    "Geografía",
    "Química",
    "Física",
    "Biología",
    "Lengua Extranjera (Inglés u otro idioma)",
    "Educación Cívica y Ética",
    "Arte",
    "Educación Física",
    "Tecnología",
    "Música",
    "Ciencias Sociales",
    "Literatura",
    "Matemáticas Avanzadas",
    "Filosofía",
    "Educación para la Salud",
    "Técnicas de Estudio"
]

def registrar_docente_vista():
    formulario_docente = customtkinter.CTk()
    formulario_docente.title("Creacion de Docente")
    formulario_docente.geometry("700x500")
    formulario_docente.resizable(False, False)
    customtkinter.set_appearance_mode("dark")
    logo_icono = customtkinter.CTkImage(light_image=Image.open("icons/logo.png"),
                                        dark_image=Image.open("icons/logo.png"),
                                        size=(80,80))

    logo_tec = customtkinter.CTkImage(light_image=Image.open("icons/tec.png"),
                                      dark_image=Image.open("icons/tec.png"),
                                      size=(80,80))

    banner = customtkinter.CTkFrame(master=formulario_docente, corner_radius=0, fg_color="#4E88FC",
                                              border_width=2, border_color="white")


    card_nombre = customtkinter.CTkFrame(master=formulario_docente, corner_radius=0, fg_color="#4E51FC",
                                              border_width=2, border_color="white")
    
    def get_datos():
        nombre = entry_nombre.get()
        email = entry_email.get()
        telefono = entry_telefono.get()
        direccion = entry_direccion.get()
        especialidad = entry_especialidad.get()


        insertar_docente(nombre, email, telefono, direccion, especialidad)

    #Imagenes que vamos a usar
    logo = customtkinter.CTkLabel(master=banner, text="", image=logo_icono)
    tec = customtkinter.CTkLabel(master=banner, text="", image=logo_tec)



    #Widges que vamos a usar
    titulo_label = customtkinter.CTkLabel(banner, text="INGRESAR LOS DATOS DEL DOCENTE",
                                          font=("Arial", 23, "bold"))

    label_nombre = customtkinter.CTkLabel(master=card_nombre, text="Nombre Docente", font=("Arial", 15, "bold"))
    entry_nombre = customtkinter.CTkEntry(master=card_nombre, width=150)
    label_email = customtkinter.CTkLabel(master=card_nombre, text="Correo Gmail", font=("Arial", 15, "bold"))
    entry_email = customtkinter.CTkEntry(master=card_nombre, width=150)
    label_telefono = customtkinter.CTkLabel(master=card_nombre, text="No Celular", font=("Arial", 15, "bold"))
    entry_telefono = customtkinter.CTkEntry(master=card_nombre, width=150)
    label_direccion = customtkinter.CTkLabel(master=card_nombre, text="Direccion", font=("Arial", 15, "bold"))
    entry_direccion = customtkinter.CTkEntry(master=card_nombre, width=150)
    label_especialidad = customtkinter.CTkLabel(master=card_nombre, text="Especialidad", font=("Arial", 15, "bold"))
    entry_especialidad = customtkinter.CTkComboBox(master=card_nombre, values=materias_secundaria, width=150)

    boton_guardar = customtkinter.CTkButton(card_nombre, text="Guardar", width=150, fg_color="#0156FF", font=("Arial", 15),
                                        text_color="white", border_color="#ffffff", border_width=2, command=get_datos)

    boton_cancelar = customtkinter.CTkButton(card_nombre, text="Cancelar", width=150, fg_color="#0156FF", font=("Arial", 15),
                                        text_color="white", border_color="#ffffff", border_width=2 ,command=formulario_docente.destroy)


    #Posicion de los widgets
    banner.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.2)
    logo.grid(column=0, row=0, padx=10, pady=10)
    tec.grid(column=2, row=0, padx=10, pady=10)
    titulo_label.grid(column=1, row=0, padx=10, pady=10)

    card_nombre.place(relx=0.0, rely=0.2, relwidth=1.0, relheight=0.8)
    label_nombre.grid(column=0, row=0, padx=10, pady=10)
    entry_nombre.grid(column=1, row=0, padx=10, pady=10)

    label_email.grid(column=2, row=0, padx=10, pady=10)
    entry_email.grid(column=3, row=0, padx=10, pady=10)
    
    label_telefono.grid(column=0, row=1, padx=10, pady=10)
    entry_telefono.grid(column=1, row=1, padx=10, pady=10)

    label_direccion.grid(column=2, row=1, padx=10, pady=10)
    entry_direccion.grid(column=3, row=1, padx=10, pady=10)

    label_especialidad.grid(column=0, row=2, padx=10, pady=10)
    entry_especialidad.grid(column=1, row=2, padx=10, pady=10)

    boton_guardar.grid(column=1, row=3, padx=10, pady=10)
    boton_cancelar.grid(column=2, row=3, padx=10, pady=10)
    formulario_docente.mainloop()


registrar_docente_vista()