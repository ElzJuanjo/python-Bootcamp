from tkinter import *
from tkinter.filedialog import *
from tkinter import ttk
import sv_ttk
import tkinter
from Pelicula import Pelicula

class Aplicacion():
    def __init__(self):
        self.pelicula = Pelicula()
        self.ventana=Tk()
        self.ventana.title("Películas")
        self.ventana.iconbitmap("Tkinter/Imagenes/LogoIcono.ico")
        self.ventana.resizable(False,False)
        self.frameDatosPelicula=Frame(self.ventana)
        self.frameDatosPelicula.grid(row=0, column=0, pady=10, padx=10)
        self.frameBotonesPelicula = Frame(self.ventana)
        self.frameBotonesPelicula.grid(row=1, column=0, pady=10, padx=10)
        self.frameTablaPeliculas = Frame(self.ventana)
        self.frameTablaPeliculas.grid(row=2, column=0, pady=10, padx=10)
        self.frameBotonesTabla = Frame(self.ventana)
        self.frameBotonesTabla.grid(row=3, column=0, pady=10, padx=10)
        self.barraDeMenu()
        self.datosPelicula()
        self.botonesPelicula()
        self.tablaPeliculas()
        self.botonesTabla()
        sv_ttk.use_dark_theme()
        
    def mostrarVentana(self):
        self.ventana.mainloop()
        
    def barraDeMenu(self):
        menuNavegacion = Menu()   
        subMenuInicio = Menu(tearoff=0)
        subMenuConsultas = Menu(tearoff=0)
        subMenuAjustes = Menu (tearoff=0)
        subMenuAyuda = Menu(tearoff=0)
        menuNavegacion.add_cascade(label='Inicio',menu=subMenuInicio)
        menuNavegacion.add_cascade(label='Consultas',menu=subMenuConsultas)
        menuNavegacion.add_cascade(label='Ajustes',menu=subMenuAjustes)
        menuNavegacion.add_cascade(label='Ayuda',menu=subMenuAyuda)
        self.ventana.config(menu=menuNavegacion) 
        
    def datosPelicula(self):
        self.labelNombre = Label(self.frameDatosPelicula, text="Nombre:")
        self.labelNombre.config(font=("Arial",12,"bold"))
        self.labelNombre.grid(row=0, column=0)
        
        self.varNombre = StringVar()
        self.cuadroNombre = Entry (self.frameDatosPelicula, textvariable=self.varNombre)
        self.cuadroNombre.config(bd=5, relief="ridge", background="#606060", font=("Arial", 12))
        self.cuadroNombre.grid(row=0, column=1, padx=5, pady=5)
        
        self.labelDuracion = Label(self.frameDatosPelicula, text="Duración:")
        self.labelDuracion.config(font=("Arial",12,"bold"))
        self.labelDuracion.grid(row=1, column=0)
        
        self.varDuracion = StringVar()
        self.cuadroDuracion = Entry (self.frameDatosPelicula, textvariable=self.varDuracion)
        self.cuadroDuracion.config(bd=5, relief="ridge", background="#606060", font=("Arial", 12))
        self.cuadroDuracion.grid(row=1, column=1, padx=5, pady=5)
        
        self.labelGenero = Label(self.frameDatosPelicula, text="Género:")
        self.labelGenero.config(font=("Arial",12,"bold"))
        self.labelGenero.grid(row=2, column=0)
        
        self.varGenero = StringVar()
        self.cuadroGenero = Entry (self.frameDatosPelicula, textvariable=self.varGenero)
        self.cuadroGenero.config(bd=5, relief="ridge", background="#606060", font=("Arial", 12))
        self.cuadroGenero.grid(row=2, column=1, padx=5, pady=5)
        
    def botonesPelicula(self):
        self.botonNuevo = Button(self.frameBotonesPelicula, text="Nuevo", command=self.habilitarCampos)
        self.botonNuevo.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonNuevo.grid(row=0, column=0,padx=10)
        
        self.botonGuardar = Button(self.frameBotonesPelicula, text="Guardar", command=self.guardarDatos)
        self.botonGuardar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonGuardar.grid(row=0, column=1,padx=10)
        
        self.botonCancelar = Button(self.frameBotonesPelicula, text="Cancelar", command=self.deshabilitarCampos)
        self.botonCancelar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonCancelar.grid(row=0, column=2,padx=10)
        
    def habilitarCampos(self):
        self.varNombre.set('')
        self.varDuracion.set('')
        self.varGenero.set('')       
        self.cuadroNombre.config(state='normal')
        self.cuadroDuracion.config(state='normal')
        self.cuadroGenero.config(state='normal')     
        self.botonGuardar.config(state='normal')
        self.botonCancelar.config(state='normal')
        
    def deshabilitarCampos(self):
        self.varNombre.set('')
        self.varDuracion.set('')
        self.varGenero.set('')       
        self.cuadroNombre.config(state='disabled')
        self.cuadroDuracion.config(state='disabled')
        self.cuadroGenero.config(state='disabled')     
        self.botonGuardar.config(state='disabled')
        self.botonCancelar.config(state='disabled')

    def guardarDatos(self):
        self.pelicula.nombre = self.varNombre.get()
        self.pelicula.duracion = self.varDuracion.get()
        self.pelicula.genero = self.varGenero.get()
        self.pelicula.insertarDato()
        self.actualizarTabla()
        self.deshabilitarCampos()
        tkinter.messagebox.showinfo("Peliculas", "Se agregaron los datos correctamente.")
    
    def tablaPeliculas(self): 
        self.tablaDeLista = ttk.Treeview(self.frameTablaPeliculas, show="headings")
        self.tablaDeLista.config(columns=("ID", "Nombre", "Duración", "Género"))
        self.tablaDeLista.heading("ID", text="ID")
        self.tablaDeLista.heading("Nombre", text="NOMBRE")
        self.tablaDeLista.heading("Duración", text="DURACIÓN")
        self.tablaDeLista.heading("Género", text="GÉNERO")
        self.tablaDeLista.grid(row=0, column=0)
        
        self.scrollTabla = Scrollbar(self.frameTablaPeliculas,command=self.tablaDeLista.yview)
        self.scrollTabla.grid(row=0, column=1, sticky="ns")
        self.tablaDeLista.config(yscrollcommand=self.scrollTabla.set)        
        
        self.actualizarTabla()
            
    def actualizarTabla(self):
        self.pelicula.verTabla()
        self.tablaDeLista.delete(*self.tablaDeLista.get_children())
        for fila in self.pelicula.datosEnDB:
            self.tablaDeLista.insert("","end",values=fila)
    
    def botonesTabla(self):
        self.botonEditar = Button(self.frameBotonesTabla, text="Editar", command=self.editarDatos)
        self.botonEditar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonEditar.grid(row=0, column=0,padx=10)
        
        self.botonEliminar = Button(self.frameBotonesTabla, text="Eliminar", command=self.eliminarDatos)
        self.botonEliminar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonEliminar.grid(row=0, column=1,padx=10)
    
    def editarDatos(self):
        self.frameBuscarID = Frame(self.ventana)
        self.frameBuscarID.grid(row=4,column=0, pady=10, padx=10)
        
        self.labelID = Label(self.frameBuscarID, text="ID:")
        self.labelID.config(font=("Arial",12,"bold"))
        self.labelID.grid(row=0, column=0)        
        
        self.varID = IntVar()
        self.cuadroID = Entry (self.frameBuscarID, textvariable=self.varID)
        self.cuadroID.config(bd=5, relief="ridge", background="#606060", font=("Arial", 12))
        self.cuadroID.grid(row=0, column=1, padx=5, pady=5)
        
        self.frameBotonesID = Frame(self.frameBuscarID)
        self.frameBotonesID.grid(row=1, column=0, columnspan=2)
        self.botonAplicar = Button(self.frameBotonesID, text="Aplicar", command=self.editarDato)
        self.botonAplicar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonAplicar.grid(row=0, column=0, padx=10)
        self.botonRegresar = Button(self.frameBotonesID, text="Regresar", command=self.deshabilitarID)
        self.botonRegresar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonRegresar.grid(row=0, column=1, padx=10)
        
    def deshabilitarID(self): 
        self.frameBuscarID.destroy()
        
    def editarDato(self):
        if self.varID.get():
            ventana = False
            if self.varNombre.get():   
                if self.pelicula.ActualizarDatos(self.varNombre.get(),"Peliculas","NOMBRE",self.varID.get()):
                    self.tablaDeLista.delete(*self.tablaDeLista.get_children())         
                    self.actualizarTabla()   
                else:
                    tkinter.messagebox.showinfo("Peliculas", "La ID ingresada no es válida.")
                    ventana = True    
                                
            if self.varDuracion.get():
                if self.pelicula.ActualizarDatos(self.varDuracion.get(),"Peliculas","DURACION",self.varID.get()):
                    self.tablaDeLista.delete(*self.tablaDeLista.get_children())
                    self.actualizarTabla()   
                else:
                    if not ventana:
                        tkinter.messagebox.showinfo("Peliculas", "La ID ingresada no es válida.")  
                        ventana = True  
                    
            if self.varGenero.get():
                if self.pelicula.ActualizarDatos(self.varGenero.get(),"Peliculas","GENERO",self.varID.get()):
                    self.tablaDeLista.delete(*self.tablaDeLista.get_children())       
                    self.actualizarTabla()   
                else:
                    if not ventana:
                        tkinter.messagebox.showinfo("Peliculas", "La ID ingresada no es válida.")   
        else:
            tkinter.messagebox.showinfo("Peliculas", "La ID ingresada no es válida.")   
    
    def eliminarDatos(self):
        self.frameBuscarID = Frame(self.ventana)
        self.frameBuscarID.grid(row=4,column=0, pady=10, padx=10)
        
        self.labelID = Label(self.frameBuscarID, text="ID:")
        self.labelID.config(font=("Arial",12,"bold"))
        self.labelID.grid(row=0, column=0)        
        
        self.varID = IntVar()
        self.cuadroID = Entry (self.frameBuscarID, textvariable=self.varID)
        self.cuadroID.config(bd=5, relief="ridge", background="#606060", font=("Arial", 12))
        self.cuadroID.grid(row=0, column=1, padx=5, pady=5)
        
        self.frameBotonesID = Frame(self.frameBuscarID)
        self.frameBotonesID.grid(row=1, column=0, columnspan=2)
        self.botonAplicar = Button(self.frameBotonesID, text="Aplicar", command=self.eliminarDato)
        self.botonAplicar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonAplicar.grid(row=0, column=0, padx=10)
        self.botonRegresar = Button(self.frameBotonesID, text="Regresar", command=self.deshabilitarID)
        self.botonRegresar.config(relief="raised", bd=5, bg="#d35631", font=("Arial", 10, "bold"))
        self.botonRegresar.grid(row=0, column=1, padx=10)
        
    def eliminarDato(self):
        if self.pelicula.EliminarDatos("Peliculas",self.varID.get()):
            self.tablaDeLista.delete(*self.tablaDeLista.get_children())
            self.actualizarTabla()   
        else:
            tkinter.messagebox.showinfo("Peliculas", "La ID ingresada no es válida.")   