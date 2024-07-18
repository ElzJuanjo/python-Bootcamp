from tkinter import *
from tkinter.filedialog import *
import tkinter
import sv_ttk

class Editor:
    def __init__(self, dimension="500x500", titulo="Editor"):
        self.dimension=dimension
        self.titulo=titulo
        self.archivoAbierto = None
        self.ventana = self.CrearVentana()
        self.CrearMenu()
        self.CrearComponentes()  
        sv_ttk.use_dark_theme()
    
    def CrearVentana(self):
        ventana = Tk()
        # ventana.geometry(self.dimension)
        ventana.title(self.titulo)
        ventana.resizable(False,False)  
        ventana.iconbitmap("Tkinter/Imagenes/LogoIcono.ico")
        ventana.protocol("WM_DELETE_WINDOW",self.Salir)
        return ventana
    
    def MostrarVentana(self):
        self.ventana.mainloop()
        
    def CrearComponentes(self):
        frameDatos = Frame()
        frameDatos.grid(row=0, column=0 ,padx=5)
        
        botonAbrir = Button(frameDatos, text="Abrir", command=self.abrirArchivo)
        botonAbrir.config(relief="raised", bd=5, bg="#d35631")
        botonAbrir.grid(row=0, column=0,pady=5)
        
        botonGuardar = Button(frameDatos, text="Guardar", command=self.guardarArchivo)
        botonGuardar.config(relief="raised", bd=5,bg="#d35631")
        botonGuardar.grid(row=1, column=0,pady=5)
        
        botonGuardarComo = Button(frameDatos, text="Guardar Como", command=self.guardarComoArchivo)
        botonGuardarComo.config(relief="raised", bd=5,bg="#d35631")
        botonGuardarComo.grid(row=2, column=0,pady=5)   
        
        botonSalir = Button(frameDatos, text="Salir", command=self.Salir)
        botonSalir.config(relief="raised", bd=5,bg="#d35631")
        botonSalir.grid(row=3, column=0,pady=5)          
        
        self.campoDeTexto = Text()
        self.campoDeTexto.config(bd=5, relief="ridge", width=50, background="#606060", font=("Arial", 12))
        self.campoDeTexto.grid(row=0, column=1,pady=5)    
        
        scrollCampoDeTexto = Scrollbar(command=self.campoDeTexto.yview)
        scrollCampoDeTexto.grid(row=0, column=2, padx=5, pady=5, sticky="ns")
        self.campoDeTexto.config(yscrollcommand=scrollCampoDeTexto.set)
        
    def CrearMenu(self):
        menuNavegacion = Menu()   
        subMenuArchivo = Menu(tearoff=0)
        menuNavegacion.add_cascade(label='Archivo',menu=subMenuArchivo)
        subMenuArchivo.add_command(label='Abrir',command=self.abrirArchivo)
        subMenuArchivo.add_command(label='Guardar',command=self.guardarArchivo)
        subMenuArchivo.add_command(label='Guardar Como',command=self.guardarComoArchivo)
        subMenuArchivo.add_separator()
        subMenuArchivo.add_command(label='Salir',command=self.Salir)
        self.ventana.config(menu=menuNavegacion)  

    def abrirArchivo(self):
        self.archivoAbierto = askopenfile(mode='r+')
        if self.archivoAbierto:
            self.campoDeTexto.delete(1.0,END)
            with open(self.archivoAbierto.name, 'r+', encoding="UTF-8") as documento:
                texto = documento.read()
                self.campoDeTexto.insert(1.0,texto)
                self.ventana.title(f"{self.titulo} - {documento.name}")

    def guardarArchivo(self):
        if self.archivoAbierto:
            with open(self.archivoAbierto.name,'w',encoding="UTF-8") as documento:
                texto = self.campoDeTexto.get(1.0,END)
                documento.write(texto)
                self.ventana.title(f"{self.titulo} - {documento.name}")
        else:
            self.guardarComoArchivo() 

    def guardarComoArchivo(self):
        archivo = asksaveasfilename(defaultextension='txt',
                                         filetypes=[('Documentos de texto','*.txt'),
                                                    ('Todos los archivos','*.*')])
        if archivo:
            with open(archivo,'w',encoding="UTF-8") as documento:
                texto = self.campoDeTexto.get(1.0,END)
                documento.write(texto)
                self.ventana.title(f"{self.titulo} - {documento.name}")
                self.archivoAbierto= documento
    
    def Salir(self):
        texto = self.campoDeTexto.get(1.0,END)
        if texto.strip():
            respuesta = tkinter.messagebox.askyesnocancel(f"{self.titulo}", "¿Quieres guardar los cambios?")
            if respuesta is True:
                self.guardarArchivo()
                self.ventana.destroy()
            elif respuesta is False:
                self.ventana.destroy()
            else:
                pass
        else:
            self.ventana.destroy()
        
nuevoEditor= Editor()
nuevoEditor.MostrarVentana()