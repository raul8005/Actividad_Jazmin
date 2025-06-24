from django.shortcuts import render, redirect
from .models import Servicio, Beneficio, Noticia, Contacto
from .forms import Afiliacion, ContactoForm, AfiliacionForm

# Create your views here.
def inicio(request):
    return render(request, 'principal/inicio.html')

def afiliacion(request):
    if request.method == 'POST':
        form = AfiliacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AfiliacionForm()
    return render(request, 'principal/afiliacion.html', {'form': form})

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'principal/servicios.html', {'servicios': servicios})

def beneficios(request):
    beneficios = Beneficio.objects.all()
    return render(request, 'principal/beneficios.html', {'beneficios': beneficios})

def noticias(request):
    noticias = Noticia.objects.order_by('-fecha_publicacion')[:6]
    return render(request, 'principal/noticias.html', {'noticias': noticias})

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ContactoForm()
    return render(request, 'principal/contacto.html', {'form': form})