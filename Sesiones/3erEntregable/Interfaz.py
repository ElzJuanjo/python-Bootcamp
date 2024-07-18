from Desarrollador import Desarrollador
from Proyecto import Proyecto
import tkinter as tk
import sv_ttk
from tkinter import messagebox, ttk

class Aplicacion:
    def __init__(self):
        self.developer = Desarrollador()
        self.project = Proyecto()
        
        self.ventana = tk.Tk()
        self.ventana.title("Tercer Entregable - Juan José Jaramillo Vera")
        try:
            self.ventana.iconbitmap("Tkinter/Imagenes/LogoIcono.ico")
        except:
            print("Aviso :: No se pudo cargar el icono.")            
        self.ventana.resizable(False,False)
        
        # LADO IZQUIERDO EN LA VENTANA, CONTIENE LO DE DEVELOPERS
        self.frameDevelopers = tk.Frame(self.ventana)
        self.frameDevelopers.grid(row=0, column=0, padx=10, pady=10)
        self.frameTituloDevelopers = tk.Frame(self.frameDevelopers)
        self.frameTituloDevelopers.grid(row=0, column=0)
        self.labelDevelopers = tk.Label(self.frameTituloDevelopers, text="DEVELOPERS")
        self.labelDevelopers.config(font=("Arial",15,"bold"), foreground="#d35631")
        self.labelDevelopers.grid(row=0, column=0)
        try:
            imagenDeveloper = tk.PhotoImage(file="Tkinter/Imagenes/Developer.png")
            labelImagenDeveloper = tk.Label(self.frameTituloDevelopers, image=imagenDeveloper)
            labelImagenDeveloper.grid(row=0, column=1)
        except:
            print("Aviso :: No se pudo cargar la imagen de developer.")           
        self.frameDatosDeveloper = tk.Frame(self.frameDevelopers)
        self.frameDatosDeveloper.grid(row=1, column=0)
        self.datosDeveloper()
        self.frameBotonesDevDatos = tk.Frame(self.frameDevelopers)
        self.frameBotonesDevDatos.grid(row=2, column=0)
        self.botonesDevDatos()
        self.frameTablaDev = tk.Frame(self.frameDevelopers)
        self.frameTablaDev.grid(row=3, column=0)
        self.tablaDev()
        self.actualizarTablaDev()
        self.frameInferiorDev = tk.Frame(self.frameDevelopers)
        self.frameInferiorDev.grid(row=4,column=0)
        self.inferiorDev()
        
        # LINEA EN MEDIO ENTRE AMBOS LADOS
        separador = ttk.Separator(self.ventana, orient="vertical")
        separador.grid(row=0, column=1, sticky="ns")
        
        # LADO DERECHO EN LA VENTANA, CONTIENE LO DE PROJECTS
        self.frameProjects = tk.Frame(self.ventana)
        self.frameProjects.grid(row=0, column=2, padx=10, pady=10)
        self.frameTituloProjects = tk.Frame(self.frameProjects)
        self.frameTituloProjects.grid(row=0, column=0)
        self.labelProjects = tk.Label(self.frameTituloProjects, text="PROJECTS")
        self.labelProjects.config(font=("Arial",15,"bold"), foreground="#d35631")
        self.labelProjects.grid(row=0, column=0)
        try:
            imagenProject = tk.PhotoImage(file="Tkinter/Imagenes/Project.png")
            labelImagenProject = tk.Label(self.frameTituloProjects, image=imagenProject)
            labelImagenProject.grid(row=0, column=1, padx=10, pady=24)
        except:
            print("Aviso :: No se pudo cargar la imagen de project.")  
        self.frameDatosProject = tk.Frame(self.frameProjects)
        self.frameDatosProject.grid(row=1, column=0)    
        self.datosProject()
        self.frameBotonesProjectDatos = tk.Frame(self.frameProjects)
        self.frameBotonesProjectDatos.grid(row=2, column=0)
        self.botonesProjectDatos()
        self.frameTablaProject = tk.Frame(self.frameProjects)
        self.frameTablaProject.grid(row=3, column=0)
        self.tablaProject()
        self.actualizarTablaProject()
        self.frameInferiorProject = tk.Frame(self.frameProjects)
        self.frameInferiorProject.grid(row=4,column=0)
        self.inferiorProject()
        
        # CARGADO DE LA VENTANA
        sv_ttk.use_dark_theme()
        self.barraDeMenu()
        self.centrarVentana()
        self.ventana.mainloop()
        
    # EJECUTAR EN MEDIO DE LA PANTALLA
    def centrarVentana(self):
        self.ventana.update_idletasks()
        anchoVentana = self.ventana.winfo_width()
        altoVentana = self.ventana.winfo_height()

        anchoPantalla = self.ventana.winfo_screenwidth()
        altoPantalla = self.ventana.winfo_screenheight()

        x = (anchoPantalla - anchoVentana) // 2
        y = (altoPantalla - altoVentana) // 2

        self.ventana.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")
     
    # OPCIONES EN LA PARTE SUPERIOR DE LA VENTANA        
    def barraDeMenu(self):
        menuNavegacion = tk.Menu()   
        subMenuInicio = tk.Menu(tearoff=0)
        subMenuConsultas = tk.Menu(tearoff=0)
        subMenuAjustes = tk.Menu (tearoff=0)
        subMenuAyuda = tk.Menu(tearoff=0)
        menuNavegacion.add_cascade(label='Inicio',menu=subMenuInicio)
        menuNavegacion.add_cascade(label='Consultas',menu=subMenuConsultas)
        menuNavegacion.add_cascade(label='Ajustes',menu=subMenuAjustes)
        menuNavegacion.add_cascade(label='Ayuda',menu=subMenuAyuda)
        self.ventana.config(menu=menuNavegacion) 
        
    # CUADROS PARA INGRESAR LA INFO DEL DEVELOPER
    def datosDeveloper(self):
        self.labelDevNombre = tk.Label(self.frameDatosDeveloper, text="Nombre:")
        self.labelDevNombre.config(font=("Arial",12,"bold"))
        self.labelDevNombre.grid(row=0, column=0)
        
        self.varDevNombre = tk.StringVar()
        self.cuadroDevNombre = tk.Entry (self.frameDatosDeveloper, textvariable=self.varDevNombre)
        self.cuadroDevNombre.config(bd=5, relief="ridge", background="#606060", font=("Arial", 12))
        self.cuadroDevNombre.grid(row=0, column=1, padx=5, pady=5)
        
        self.labelHabilidad = tk.Label(self.frameDatosDeveloper, text="Habilidad:")
        self.labelHabilidad.config(font=("Arial",12,"bold"))
        self.labelHabilidad.grid(row=1, column=0)
        
        self.varHabilidad = tk.StringVar()
        self.cuadroHabilidad = tk.Entry (self.frameDatosDeveloper, textvariable=self.varHabilidad)
        self.cuadroHabilidad.config(bd=5, relief="ridge", background="#606060", font=("Arial", 12))
        self.cuadroHabilidad.grid(row=1, column=1, padx=5, pady=5)

    # CUADROS PARA INGRESAR LA INFO DEL PROJECT
    def datosProject(self):
        self.labelProjectNombre = tk.Label(self.frameDatosProject, text="Nombre:")
        self.labelProjectNombre.config(font=("Arial",12,"bold"))
        self.labelProjectNombre.grid(row=0, column=0)
        
        self.varProjectNombre = tk.StringVar()
        self.cuadroProjectNombre = tk.Entry (self.frameDatosProject, textvariable=self.varProjectNombre)
        self.cuadroProjectNombre.config(bd=5, relief="ridge", background="#606060", font=("Arial", 12))
        self.cuadroProjectNombre.grid(row=0, column=1, padx=5, pady=5)
        
        self.labelDevID = tk.Label(self.frameDatosProject, text="Dev_ID:")
        self.labelDevID.config(font=("Arial",12,"bold"))
        self.labelDevID.grid(row=1, column=0)
        
        self.varDevID = tk.IntVar()
        self.cuadroDevID = tk.Entry (self.frameDatosProject, textvariable=self.varDevID)
        self.cuadroDevID.config(bd=5, relief="ridge", background="#606060", font=("Arial", 12))
        self.cuadroDevID.grid(row=1, column=1, padx=5, pady=5)
        
    # BOTONES NUEVO, GUARDAR Y CANCELAR EN DEVELOPERS
    def botonesDevDatos(self):
        self.botonDevNuevo = tk.Button(self.frameBotonesDevDatos, text="Nuevo", command=self.funcionNuevoDev)
        self.botonDevNuevo.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonDevNuevo.grid(row=0, column=0,padx=10)
        
        self.botonDevGuardar = tk.Button(self.frameBotonesDevDatos, text="Guardar", command=self.funcionGuardarDev)
        self.botonDevGuardar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonDevGuardar.grid(row=0, column=1,padx=10)
        
        self.botonDevCancelar = tk.Button(self.frameBotonesDevDatos, text="Cancelar", command=self.funcionCancelarDev)
        self.botonDevCancelar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonDevCancelar.grid(row=0, column=2,padx=10)
        
    # BOTONES NUEVO, GUARDAR Y CANCELAR EN PROJECTS
    def botonesProjectDatos(self):
        self.botonProjectNuevo = tk.Button(self.frameBotonesProjectDatos, text="Nuevo", command=self.funcionNuevoProject)
        self.botonProjectNuevo.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonProjectNuevo.grid(row=0, column=0,padx=10)
        
        self.botonProjectGuardar = tk.Button(self.frameBotonesProjectDatos, text="Guardar", command=self.funcionGuardarProject)
        self.botonProjectGuardar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonProjectGuardar.grid(row=0, column=1,padx=10)
        
        self.botonProjectCancelar = tk.Button(self.frameBotonesProjectDatos, text="Cancelar", command=self.funcionCancelarProject)
        self.botonProjectCancelar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonProjectCancelar.grid(row=0, column=2,padx=10)
        
    # FUNCIONES AL DAR CLIC EN NUEVO, GUARDAR Y CANCELAR EN DEVELOPERS    
    
    def funcionNuevoDev(self):
        self.varDevNombre.set('')
        self.varHabilidad.set('')  
        self.cuadroDevNombre.config(state='normal')
        self.cuadroHabilidad.config(state='normal')
        self.botonDevGuardar.config(state='normal')
        self.botonDevCancelar.config(state='normal')
        
    def funcionGuardarDev(self):
        if self.varDevNombre.get() and self.varHabilidad.get():
            self.developer.devNombre = self.varDevNombre.get()
            self.developer.habilidad = self.varHabilidad.get()
            self.developer.InsertarDB()
            self.actualizarTablaDev()
            self.funcionCancelarDev()
        else:
            messagebox.showerror("Error","No puede dejar un campo vacio.")
        
    def funcionCancelarDev(self):
        self.varDevNombre.set('')
        self.varHabilidad.set('')  
        self.cuadroDevNombre.config(state='disabled')
        self.cuadroHabilidad.config(state='disabled')  
        self.botonDevGuardar.config(state='disabled')
        self.botonDevCancelar.config(state='disabled')  
         
    # FUNCIONES AL DAR CLIC EN NUEVO, GUARDAR Y CANCELAR EN PROJECTS    
       
    def funcionNuevoProject(self):
        self.varProjectNombre.set('')
        self.varDevID.set(0)  
        self.cuadroProjectNombre.config(state='normal')
        self.cuadroDevID.config(state='normal')
        self.botonProjectGuardar.config(state='normal')
        self.botonProjectCancelar.config(state='normal')
        
    def funcionGuardarProject(self):
        try:
            if self.varProjectNombre.get() and self.varDevID.get():
                if self.developer.BuscarId(self.varDevID.get(),"Developers"):
                    self.project.projectNombre = self.varProjectNombre.get()
                    self.project.devID = self.varDevID.get()
                    self.project.InsertarDB()
                    self.actualizarTablaProject()
                    self.funcionCancelarProject()
                else:
                    messagebox.showerror("Error","No hay un desarollador con esa ID.")
            else:
                messagebox.showerror("Error","No puede dejar un campo vacio.")
        except:
            messagebox.showerror("Error","No se pudo guardar en la tabla de Projects.")    
        
    def funcionCancelarProject(self):
        self.varProjectNombre.set('')
        self.varDevID.set('')  
        self.cuadroProjectNombre.config(state='disabled')
        self.cuadroDevID.config(state='disabled')  
        self.botonProjectGuardar.config(state='disabled')
        self.botonProjectCancelar.config(state='disabled')    
          
    # TABLA CON LA BASE DE DATOS DE DEVELOPERS    
    def tablaDev(self):
        self.tablaDeDev = ttk.Treeview(self.frameTablaDev, show="headings")
        self.tablaDeDev.config(columns=("ID", "Nombre", "Habilidad"))
        self.tablaDeDev.heading("ID", text="ID")
        self.tablaDeDev.heading("Nombre", text="NOMBRE")
        self.tablaDeDev.heading("Habilidad", text="HABILIDAD")
        self.tablaDeDev.grid(row=0, column=0)
        
        self.scrollDeDev = tk.Scrollbar(self.frameTablaDev,command=self.tablaDeDev.yview)
        self.scrollDeDev.grid(row=0, column=1, sticky="ns")
        self.tablaDeDev.config(yscrollcommand=self.scrollDeDev.set)  
        
    # TABLA CON LA BASE DE DATOS DE PROJECTS      
    def tablaProject(self):
        self.tablaDeProject = ttk.Treeview(self.frameTablaProject, show="headings")
        self.tablaDeProject.config(columns=("ID", "Nombre", "Dev_ID"))
        self.tablaDeProject.heading("ID", text="ID")
        self.tablaDeProject.heading("Nombre", text="NOMBRE")
        self.tablaDeProject.heading("Dev_ID", text="DEV_ID")
        self.tablaDeProject.grid(row=0, column=0)
        
        self.scrollDeProject = tk.Scrollbar(self.frameTablaProject,command=self.tablaDeProject.yview)
        self.scrollDeProject.grid(row=0, column=1, sticky="ns")
        self.tablaDeProject.config(yscrollcommand=self.scrollDeProject.set)  
        
    # CARGAR LOS DATOS DE LA TABLA DEVELOPERS DE LA BASE DE DATOS A LA INTERFAZ      
    def actualizarTablaDev(self):
        try:
            self.developer.LeerDB()
            self.tablaDeDev.delete(*self.tablaDeDev.get_children())
            for fila in self.developer.listaDeDatos:
                self.tablaDeDev.insert("","end",values=fila)
        except:
            messagebox.showerror("Error","No se pudo actualizar la tabla de Developers.")       
            
    # CARGAR LOS DATOS DE LA TABLA PROJECTS DE LA BASE DE DATOS A LA INTERFAZ             
    def actualizarTablaProject(self):
        try:
            self.project.LeerDB()
            self.tablaDeProject.delete(*self.tablaDeProject.get_children())
            for fila in self.project.listaDeDatos:
                self.tablaDeProject.insert("","end",values=fila)
        except:
            messagebox.showerror("Error","No se pudo actualizar la tabla de Projects.")   
    
    # CUADRO PARA INGRESAR LA ID DEL DEVELOPER Y BOTONES EDITAR-ELIMINAR EN DEVELOPERS               
    def inferiorDev(self):
        self.labelDevInferiorID = tk.Label(self.frameInferiorDev, text="ID:")
        self.labelDevInferiorID.config(font=("Arial",12,"bold"))
        self.labelDevInferiorID.grid(row=0, column=0)
        
        self.varDevInferiorID = tk.IntVar()
        self.cuadroDevInferiorID = tk.Entry (self.frameInferiorDev, textvariable=self.varDevInferiorID)
        self.cuadroDevInferiorID.config(bd=5, relief="ridge", background="#606060", font=("Arial", 12))
        self.cuadroDevInferiorID.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
        
        self.botonDevEditar = tk.Button(self.frameInferiorDev, text="Editar", command=self.funcionEditarDev)
        self.botonDevEditar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonDevEditar.grid(row=1, column=1,padx=10)
        
        self.botonDevEliminar = tk.Button(self.frameInferiorDev, text="Eliminar", command=self.funcionEliminarDev)
        self.botonDevEliminar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonDevEliminar.grid(row=1, column=2,padx=10)     
   
    # CUADRO PARA INGRESAR LA ID DEL PROJECT Y BOTONES EDITAR-ELIMINAR EN PROJECTS      
    def inferiorProject(self):
        self.labelProjectInferiorID = tk.Label(self.frameInferiorProject, text="ID:")
        self.labelProjectInferiorID.config(font=("Arial",12,"bold"))
        self.labelProjectInferiorID.grid(row=0, column=0)
        
        self.varProjectInferiorID = tk.IntVar()
        self.cuadroProjectInferiorID = tk.Entry (self.frameInferiorProject, textvariable=self.varProjectInferiorID)
        self.cuadroProjectInferiorID.config(bd=5, relief="ridge", background="#606060", font=("Arial", 12))
        self.cuadroProjectInferiorID.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
        
        self.botonProjectEditar = tk.Button(self.frameInferiorProject, text="Editar", command=self.funcionEditarProject)
        self.botonProjectEditar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonProjectEditar.grid(row=1, column=1,padx=10)
        
        self.botonProjectEliminar = tk.Button(self.frameInferiorProject, text="Eliminar", command= self.funcionEliminarProject)
        self.botonProjectEliminar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonProjectEliminar.grid(row=1, column=2,padx=10)   
        
    # FUNCIONES AL DAR CLICK EN EDITAR Y ELIMINAR EN DEVELOPERS     
     
    def funcionEditarDev(self):
        try:
            if self.varDevInferiorID.get():
                if self.varDevNombre.get():
                    confirmar = messagebox.askokcancel("Developers",f"¿Desea editar el nombre en ID: {self.varDevInferiorID.get()}?")
                    if confirmar:
                        if self.developer.EditarDB(self.varDevNombre.get(),"NOMBRE",self.varDevInferiorID.get()):
                            self.actualizarTablaDev()
                        else:
                            messagebox.showerror("Error","No hay un desarollador con esa ID.")
                            
                if self.varHabilidad.get():
                    confirmar = messagebox.askokcancel("Developers",f"¿Desea editar la habilidad en ID: {self.varDevInferiorID.get()}?")
                    if confirmar:
                        if self.developer.EditarDB(self.varHabilidad.get(),"HABILIDAD",self.varDevInferiorID.get()):
                            self.actualizarTablaDev()
                        else:
                            messagebox.showerror("Error","No hay un desarollador con esa ID.")             
            else:
                messagebox.showerror("Error","No puede dejar un campo vacio.")   
        except:
            messagebox.showerror("Error","No se pudo editar en la tabla de Developers.") 
            
    def funcionEliminarDev(self):
        try:
            if self.varDevInferiorID.get():
                confirmar = messagebox.askokcancel("Developers",f"¿Desea eliminar el registro en ID: {self.varDevInferiorID.get()}?")
                if confirmar:
                    if self.developer.EliminarDB(self.varDevInferiorID.get()):
                        self.project.EliminarProyectosDev(self.varDevInferiorID.get())
                        self.actualizarTablaDev()
                        self.actualizarTablaProject()
                    else:
                        messagebox.showerror("Error","No hay un desarollador con esa ID.")          
            else:
                messagebox.showerror("Error","No puede dejar un campo vacio.")   
        except:
            messagebox.showerror("Error","No se pudo eliminar en la tabla de Developers.")  
            
    # FUNCIONES AL DAR CLICK EN EDITAR Y ELIMINAR EN PROJECTS     
         
    def funcionEditarProject(self):
        try:
            if self.varProjectInferiorID.get():
                if self.varProjectNombre.get():
                    confirmar = messagebox.askokcancel("Projects",f"¿Desea editar el nombre en ID: {self.varProjectInferiorID.get()}?")
                    if confirmar:
                        if self.project.EditarDB(self.varProjectNombre.get(),"NOMBRE",self.varProjectInferiorID.get()):
                            self.actualizarTablaProject()
                        else:
                            messagebox.showerror("Error","No hay un proyecto con esa ID.")
                try:       
                    if self.varDevID.get():
                        if self.developer.BuscarId(self.varDevID.get(),"Developers"):
                            confirmar = messagebox.askokcancel("Projects",f"¿Desea editar el dev_id en ID: {self.varProjectInferiorID.get()}?")
                            if confirmar:
                                if self.project.EditarDB(self.varDevID.get(),"DEV_ID",self.varProjectInferiorID.get()):
                                    self.actualizarTablaProject()
                                else:
                                    messagebox.showerror("Error","No hay un proyecto con esa ID.")  
                        else:
                            messagebox.showerror("Error","No hay un desarollador con esa ID.") 
                except:
                    pass                      
            else:
                messagebox.showerror("Error","No puede dejar un campo vacio.")   
        except:
            messagebox.showerror("Error","No se pudo editar en la tabla de Projects.")   
            
    def funcionEliminarProject(self):
        try:
            if self.varProjectInferiorID.get():
                confirmar = messagebox.askokcancel("Projects",f"¿Desea eliminar el registro en ID: {self.varProjectInferiorID.get()}?")
                if confirmar:
                    if self.project.EliminarDB(self.varProjectInferiorID.get()):
                        self.actualizarTablaProject()
                    else:
                        messagebox.showerror("Error","No hay un proyecto con esa ID.")          
            else:
                messagebox.showerror("Error","No puede dejar un campo vacio.")   
        except:
            messagebox.showerror("Error","No se pudo eliminar en la tabla de Projects.")       