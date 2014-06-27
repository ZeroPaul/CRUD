from app_crud.models import Producto
from django.shortcuts import render, render_to_response,get_object_or_404
from app_crud.forms import ProductoForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def read(request):
    productos = Producto.objects.all().order_by('-id')
    return render(request, 'app_crud/inicio.html',
                  {'productos': productos})

def agregar(request):
    if request.method == "POST":
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = ProductoForm()
    return render_to_response('app_crud/agregar.html',
                                {'formulario': formulario},
                                 context_instance = RequestContext(request))

def editar (request, id):
        producto= Producto.objects.get(pk=id)
        if request.method == 'POST':
            formulario = ProductoForm(request.POST, instance = producto)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/")
        else:
            formulario = ProductoForm(instance= producto)
        return render_to_response('app_crud/editar.html',
                                   {'formulario': formulario},
                                   context_instance = RequestContext(request))
def borrar (request, id):
    producto = get_object_or_404(Producto, pk=id)
    producto.delete()
    return HttpResponseRedirect("/")
