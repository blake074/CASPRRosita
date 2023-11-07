from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *


# Create your views here.

def InicioS(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Principal')
    else:
        form = LoginForm()

    return render(request, 'inicioS.html', {'form': form})     


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

def EditarProducto(request, ID_PRODUCTO):
    prov = Producto.objects.get(ID_PRODUCTO=ID_PRODUCTO)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=prov)
        if form.is_valid():
            form.save()
            return redirect('VerProducto')  # Redirige a la lista de clientes o a donde desees.
    else:
        form = ProductoForm(instance=prov)
    return render(request, 'Producto/EditarProducto.html', {'form': form, 'prov': prov}) 



def VerClientes(request):
    cliente = Cliente.objects.all()
    return render (request, 'Cliente/VerCliente.html', {'cliente':cliente})

def CrearCliente(request):
    formulario=ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('VerClientes')
    return render(request,'Cliente/CrearCliente.html', {'formulario':formulario})

def BorrarClientes(request, ID_CLIENTE):
    cliente = Cliente.objects.get(ID_CLIENTE=ID_CLIENTE)
    cliente.delete()
    return redirect('VerClientes')

def EditarCliente(request, ID_CLIENTE):
    cliente = Cliente.objects.get(ID_CLIENTE=ID_CLIENTE)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('VerClientes')  # Redirige a la lista de clientes o a donde desees.
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'Cliente/EditarCliente.html', {'form': form, 'cliente': cliente}) 



def VerProveedores(request):
    prov = Proveedor.objects.all()
    return render (request, 'Proveedor/VerProveedor.html', {'prov':prov})

def CrearProveedor(request):
    formulario=ProveedorForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('VerProveedores')
    return render(request,'Proveedor/CrearProveedor.html', {'formulario':formulario})

def BorrarProveedor(request, ID_PROVEEDOR):
    proveedor = Proveedor.objects.get(ID_PROVEEDOR=ID_PROVEEDOR)
    proveedor.delete()
    return redirect('VerProveedores')

def EditarProveedor(request, ID_PROVEEDOR):
    prov = Proveedor.objects.get(ID_PROVEEDOR=ID_PROVEEDOR)

    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=prov)
        if form.is_valid():
            form.save()
            return redirect('VerProveedores')  # Redirige a la lista de clientes o a donde desees.
    else:
        form = ProveedorForm(instance=prov)
    return render(request, 'Proveedor/EditarProveedor.html', {'form': form, 'prov': prov}) 



def VerCategoria(request):
    Cat = Categoria.objects.all()
    return render (request, 'Categoria/VerCategoria.html', {'Cat':Cat})

def CrearCategoria(request):
    formulario=CategoriaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('VerCategoria')
    return render(request,'Categoria/CrearCategoria.html', {'formulario':formulario})

def BorrarCategoria(request, ID_CATEGORIA):
    cliente = Categoria.objects.get(ID_CATEGORIA=ID_CATEGORIA)
    cliente.delete()
    return redirect('VerCategoria')

def EditarCategoria(request, ID_CATEGORIA):
    Cat = Categoria.objects.get(ID_CATEGORIA=ID_CATEGORIA)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=Cat)
        if form.is_valid():
            form.save()
            return redirect('VerCategoria')  # Redirige a la lista de clientes o a donde desees.
    else:
        form = CategoriaForm(instance=Cat)
    return render(request, 'Categoria/EditarCategoria.html', {'form': form, 'Cat': Cat}) 



def VerPedido(request):
    pedido = Pedido.objects.select_related('ID_PROVEEDOR_PEDIDO', 'ID_PRODUCTO_PEDIDO').all()
    return render (request, 'Pedido/VerPedido.html', {'pedido':pedido})

def CrearPedido(request):
    formulario=PedidoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('VerPedido')
    return render(request,'Pedido/CrearPedido.html', {'formulario':formulario})

def BorrarPedido(request, ID_PEDIDO):
    Pedid = Pedido.objects.get(ID_PEDIDO=ID_PEDIDO)
    Pedid.delete()
    return redirect('VerPedido')

def EditarPedido(request, ID_PEDIDO):
    prov = Pedido.objects.get(ID_PEDIDO=ID_PEDIDO)

    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=prov)
        if form.is_valid():
            form.save()
            return redirect('VerPedido')  # Redirige a la lista de clientes o a donde desees.
    else:
        form = PedidoForm(instance=prov)
    return render(request, 'Pedido/EditarPedido.html', {'form': form, 'prov': prov}) 