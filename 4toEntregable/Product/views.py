from django.shortcuts import render, redirect
from django.templatetags.static import static
from .models import categoriaUno, categoriaDos

# Create your views here.
def categorias(request):
    return render(request, 'categorias.html')

def infoCategoria(request, category):
    if category == "apps":
        try:
            items = list(categoriaUno.objects.all())    
            tittle = "Aplicaciones"  
            tabla = "apps"
        except:
            return redirect('/categorias/')
        
    if category == "asesorys":
        try:
            items = list(categoriaDos.objects.all())    
            tittle = "Asesorias"  
            tabla = "asesorys"
        except:
            return redirect('/categorias/')
        
    return render(request, 'infoCategoria.html', {
        "tittle":tittle,
        "items":items,
        "tabla":tabla
    })

def producto(request, tabla, id):
    if tabla == "apps":
        try:
            item = categoriaUno.objects.get(ID=id)
            img = static(item.IMG)
        except:
            return redirect('/categorias/')
        
    if tabla == "asesorys":
        try:
            item = categoriaDos.objects.get(ID=id)
            img = static(item.IMG)
        except:
            return redirect('/categorias/')
            
    return render(request, 'producto.html', {
        "nombreProducto":item.NOMBRE,
        "detalleProducto":item.DESCRIPCION,
        "imgProducto":img
    })