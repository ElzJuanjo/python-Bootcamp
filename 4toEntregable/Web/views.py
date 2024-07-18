from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    mensajeError = ""
    showError = False
    if request.method == 'POST':
        usuario = request.POST['usuario']
        clave = request.POST['clave']
        
        try:
          usuarioEncontrado = Cliente.objects.get(USUARIO=usuario)  
          if usuarioEncontrado.CLAVE == clave:
              return redirect('/categorias/')
          else:
              mensajeError = "La contraseña ingresada es incorrecta."
              showError = True
        except:
            mensajeError = "El usuario no se encuentra registrado."
            showError = True
    
    return render(request, 'login.html', {
        "mensajeError":mensajeError,
        "showError":showError
    })

def register(request):
    mensajeError = ""
    showError = False
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        edad = request.POST['edad']
        correo = request.POST['correo']
        usuario = request.POST['usuario']
        clave = request.POST['clave']
        
        try:
            usuarioExistente = Cliente.objects.get(USUARIO=usuario)
            mensajeError = "Este usuario ya se encuentra en uso."
            showError = True
        except:
            edad = int(edad)
            if edad < 14 or edad > 80:
                mensajeError = "La edad debe ser entre 14 y 80 años."
                showError = True
            else:
                nuevoCliente = Cliente.objects.create(NOMBRE=nombre, APELLIDOS=apellidos, EDAD=edad, CORREO=correo, USUARIO=usuario, CLAVE=clave)
                return redirect('/login/')
        
    return render(request, 'register.html', {
        "mensajeError":mensajeError,
        "showError": showError
    })