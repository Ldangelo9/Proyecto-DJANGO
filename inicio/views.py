from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Aerosol    
from inicio.form import FormularioCrearAerosol


def inicio(request):
    
    return render(request, 'inicio/inicio.html')
    
def crear_aerosol(request):
    
    if request.method == "POST":
        formulario = FormularioCrearAerosol(request.POST)
        if formulario.is_valid():
            marca_nueva = formulario.cleaned_data.get('marca')
            color_nuevo = formulario.cleaned_data.get('color')
            
            aerosol = Aerosol(marca=marca_nueva, color=color_nuevo)
            aerosol.save()
            
            return redirect("lista_aerosoles")
    else: 
        formulario = FormularioCrearAerosol()
    
    
    return render(request, 'inicio/crear_aerosol.html', {'formulario': formulario})   

def lista_aerosoles(request):
    
    aerosol = Aerosol.objects.all()
    
    return render(request,'inicio/lista_aerosoles.html',{'lista_aerosoles': aerosol})
    