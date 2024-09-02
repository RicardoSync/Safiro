import customtkinter 
from PIL import Image
import datetime


def panel_de_control(login):
    login.destroy()
    panel_de_control = customtkinter.CTk()
    panel_de_control.title("Panel de Control Safiro")
    panel_de_control.geometry("900x500")
    panel_de_control.resizable(False, False)
    customtkinter.set_appearance_mode("dark")

    #Definoms las variables dentro del entorno
    fecha_actual = datetime.date.today()


    #Definimos las imagenes que vamos a estar usando
    logo_tec = customtkinter.CTkImage(light_image=Image.open("icons/tec.png"),
      dark_image=Image.open("icons/tec.png"),
      size=(100, 100))



    #Definimos las FRAMES que vamos a usar
    barra_navegacion = customtkinter.CTkFrame(panel_de_control, fg_color="transparent",
                                              border_color="#ffffff", border_width=2)

    banner = customtkinter.CTkFrame(panel_de_control, fg_color="transparent",
                                              border_color="#ffffff", border_width=2)


    pestanas = customtkinter.CTkTabview(panel_de_control)
    pestanas.add("Premisas") #Vamos a poner a las materias y los padres
    pestanas.add("Alumnos") #Vamos a poner a los alumnos, padres y asistencias
    pestanas.add("Oficina") #Vamos a poner a los reportes, calificaciones
    pestanas.add("Ajustes") #Vamos a poner los ajustes que se vayan requeriendo



    #Definomos los widgets que vams a usar
    logo_tec_icono = customtkinter.CTkLabel(barra_navegacion, text="", image=logo_tec)

    titulo_panel = customtkinter.CTkLabel(banner, text="Panel De Control Safiro", font=("Monospace", 20, "bold"))

    #Botones para la barra de navegacion

    #Botones para la pestana de "Premisas"
    materias_button = customtkinter.CTkButton(master=pestanas.tab("Premisas"), text="Agregar Materias",
      corner_radius=32)
    maestros_button = customtkinter.CTkButton(master=pestanas.tab("Premisas"), text="Agregar Docentes",
      corner_radius=32)
    opciones = customtkinter.CTkButton(master=pestanas.tab("Premisas"), text="###=###",
      corner_radius=32)


    #Botones para los alumnos
    padres_familia = customtkinter.CTkButton(master=pestanas.tab("Alumnos"), text="Agregar Padre",
      corner_radius=32)
    agregar_alumno = customtkinter.CTkButton(master=pestanas.tab("Alumnos"), text="Agregar Alumnos",
      corner_radius=32)




    #Definimos las posiciones de los widgets
    barra_navegacion.place(
    relx=0.0,
    rely=0.0,
    relwidth=0.2,
    relheight=1.0
    )
    logo_tec_icono.pack(padx=10, pady=10)


    banner.place(
    relx=0.2,
    rely=0.0,
    relwidth=0.8,
    relheight=0.2
    )
    titulo_panel.pack(padx=10, pady=10)

    pestanas.place(
    relx=0.3,
    rely=0.2,
    relwidth=0.6,
    relheight=0.7
    )
    materias_button.grid(column=0, row=0, padx=10, pady=10)
    maestros_button.grid(column=1, row=0, padx=10, pady=10)
    opciones.grid(column=2, row=0, padx=10, pady=10)

    padres_familia.grid(column=0, row=0, padx=10, pady=10)
    agregar_alumno.grid(column=1, row=0, padx=10, pady=10)
    panel_de_control.mainloop()
