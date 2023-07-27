from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Persona

# ======================================
# Funciones para manejar las vistas html
# ======================================
def index(request):
    return redirect('home')

def home(request):
    personas = Persona.objects.all()

    context = {'personas': personas}
    return render(request, 'home.html', context=context)

# ==========================================
# Funciones para manejar las peticiones http
# ==========================================
def form_post_persona(request):
    if request.method == 'GET':
        return render(request, 'view_post_persona.html', {})
    elif request.method == 'POST':
        db_create_persona(request=request)
        return redirect('form_post_persona')
    return redirect('home')

def form_update_persona(request):
    if request.method == 'GET':
        try:
            persona = Persona.objects.filter(id=request.GET['txtId']).first()
            context = {
                'persona': persona
            }
            if persona:
                return render(request, 'view_update_persona.html', context=context)
        except Exception as ex:
            pass
    elif request.method == 'POST':
        db_update_persona(request=request)                
    return redirect('home')


def form_delete_persona(request, id):
    if request.method == 'GET':         
        db_delete_persona(id=id)
    
    return redirect('home')

# ================================================
# Funciones CRUD para interactuar con las base de datos
# ================================================    
def db_create_persona(request):
    try:
        txt_nombre = request.POST['txtNombre']
        txt_apellido = request.POST['txtApellido']
        txt_fecha_nacimiento = request.POST['txtFechaNacimiento']
        txt_genero = request.POST['txtGenero']
        txt_telefono = request.POST['txtTelefono']
        txt_correo = request.POST['txtCorreo']

        persona = Persona(
            nombre=txt_nombre.title(), 
            apellido=txt_apellido.title(), 
            fecha_nacimiento=txt_fecha_nacimiento, 
            genero=txt_genero, 
            telefono=txt_telefono, 
            correo=txt_correo
        )
        persona.save()
    except Exception as ex:
        print(f"ERROR: {ex}")
        messages.error(request=request, message=ex, extra_tags="alert-danger")
        

def db_update_persona(request):    

    txt_id = request.POST['txtId']
    persona = Persona.objects.filter(id=txt_id).first()
    if persona:
        txt_nombre = request.POST['txtNombre']
        txt_apellido = request.POST['txtApellido']
        txt_fecha_nacimiento = request.POST['txtFechaNacimiento']
        txt_genero = request.POST['txtGenero']
        txt_telefono = request.POST['txtTelefono']
        txt_correo = request.POST['txtCorreo']

        persona.nombre = txt_nombre.title()
        persona.apellido = txt_apellido.title()
        persona.genero = txt_genero
        persona.fecha_nacimiento = txt_fecha_nacimiento
        persona.telefono = txt_telefono
        persona.correo = txt_correo
        persona.save()

def db_delete_persona(id):    
    p = Persona.objects.filter(id=id).all()
    if p:
        p.delete()            
