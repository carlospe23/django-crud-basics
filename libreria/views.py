from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm
# Create your views here.

def home(request):
    return render(request, 'paginas/home.html')


def about(request):
    return render(request, 'paginas/about.html')


def libros(request):
    libros = Libro.objects.all()

    return render(request, 'libros/index.html', context={
        'libros': libros
    })


def crear_libro(request):
    formulario = LibroForm(
        request.POST or None, 
        request.FILES or None
    )
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', context={
        'formulario':formulario
    })


def editar_libro(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(
        request.POST or None, 
        request.FILES or None, 
        instance=libro
    )
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    
    return render(request, 'libros/editar.html', context={
        'formulario': formulario
    })


def borrar_libro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')