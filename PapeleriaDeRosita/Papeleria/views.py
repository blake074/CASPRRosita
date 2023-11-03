from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *


# Create your views here.

def Inicio(request):
    return render(request, 'MenuPrincipal.html')


def VerFactura(request):
    facturas = Factura.objects.select_related('ID_CLIENTE_FACTURA', 'ID_PRODUCTO_FACTURA').all()
    return render (request, 'Factura/VerFactura.html', {'facturas':facturas})

def CrearFactura(request):
    formulario=FacturaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('VerFactura')
    return render(request,'Factura/CrearFactura.html', {'formulario':formulario})



def VerProducto(request):
    Productos = Producto.objects.select_related('ID_CATEGORIA_PRODUCTO').all()
    return render (request, 'Producto/VerProducto.html', {'Productos':Productos})

def CrearProducto(request):
    formulario=ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('VerProducto')
    return render(request,'Producto/CrearProducto.html', {'formulario':formulario})

def MovimientoProductoVista(request):
    Productos = MovimientoProducto.objects.select_related('ID_PRODUCTO_MOVIMIENTO').all()
    return render (request, 'Producto/MovimientosProductoView.html', {'Productos':Productos})



def VerClientes(request):
    cliente = Cliente.objects.all()
    return render (request, 'Cliente/VerCliente.html', {'cliente':cliente})

def CrearCliente(request):
    formulario=ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('VerClientes')
    return render(request,'Cliente/CrearCliente.html', {'formulario':formulario})



def VerProveedores(request):
    prov = Proveedor.objects.all()
    return render (request, 'Proveedor/VerProveedor.html', {'prov':prov})

def CrearProveedor(request):
    formulario=ProveedorForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('VerProveedores')
    return render(request,'Proveedor/CrearProveedor.html', {'formulario':formulario})



def VerCategoria(request):
    Cat = Categoria.objects.all()
    return render (request, 'Categoria/VerCategoria.html', {'Cat':Cat})

def CrearCategoria(request):
    formulario=CategoriaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('VerCategoria')
    return render(request,'Categoria/CrearCategoria.html', {'formulario':formulario})