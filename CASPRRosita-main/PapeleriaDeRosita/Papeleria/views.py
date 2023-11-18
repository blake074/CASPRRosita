from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.base import TemplateView
from django.contrib.auth import logout
from django.views import View
from django.db.models import Count
from django.db.models import Sum

from datetime import datetime

from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
import tempfile
from reportlab.pdfgen import canvas
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as pltprod
import matplotlib
matplotlib.use('Agg') 
import io
import base64

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
                return redirect('MenuPrincipal')
    else:
        form = LoginForm()

    return render(request, 'inicioS.html', {'form': form})  

def CerrarSesion(request):
    logout(request)
    return redirect('InicioSesion')


def usuarioRosita(user):
    return user.username == 'Rosita'



@login_required
def Inicio(request):
    return render(request, 'MenuPrincipal.html')

@login_required
def VerFactura(request):
    facturas = Factura.objects.select_related('ID_CLIENTE_FACTURA', 'ID_PRODUCTO_FACTURA').all()
    return render (request, 'Factura/VerFactura.html', {'facturas':facturas})

@login_required
def CrearFactura(request):
    formulario=FacturaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('VerFactura')
    return render(request,'Factura/CrearFactura.html', {'formulario':formulario})



@login_required
def VerProducto(request):
    Productos = Producto.objects.select_related('ID_CATEGORIA_PRODUCTO').all()
    return render (request, 'Producto/VerProducto.html', {'Productos':Productos})

@user_passes_test(usuarioRosita)
def CrearProducto(request):
    formulario=ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('VerProducto')
    return render(request,'Producto/CrearProducto.html', {'formulario':formulario})

@user_passes_test(usuarioRosita)
def MovimientoProductoVista(request):
    Productos = MovimientoProducto.objects.select_related('ID_PRODUCTO_MOVIMIENTO').all()
    return render (request, 'Producto/MovimientosProductoView.html', {'Productos':Productos})

@user_passes_test(usuarioRosita)
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



@login_required
def VerClientes(request):
    cliente = Cliente.objects.all()
    return render (request, 'Cliente/VerCliente.html', {'cliente':cliente})

@login_required
def CrearCliente(request):
    formulario=ClienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('VerClientes')
    return render(request,'Cliente/CrearCliente.html', {'formulario':formulario})

@login_required
def BorrarClientes(request, ID_CLIENTE):
    cliente = Cliente.objects.get(ID_CLIENTE=ID_CLIENTE)
    cliente.delete()
    return redirect('VerClientes')

@login_required
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



@user_passes_test(usuarioRosita)
def VerProveedores(request):
    prov = Proveedor.objects.all()
    return render (request, 'Proveedor/VerProveedor.html', {'prov':prov})

@user_passes_test(usuarioRosita)
def CrearProveedor(request):
    formulario=ProveedorForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('VerProveedores')
    return render(request,'Proveedor/CrearProveedor.html', {'formulario':formulario})

@user_passes_test(usuarioRosita)
def BorrarProveedor(request, ID_PROVEEDOR):
    proveedor = Proveedor.objects.get(ID_PROVEEDOR=ID_PROVEEDOR)
    proveedor.delete()
    return redirect('VerProveedores')

@user_passes_test(usuarioRosita)
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



@login_required
def VerCategoria(request):
    Cat = Categoria.objects.all()
    return render (request, 'Categoria/VerCategoria.html', {'Cat':Cat})

@user_passes_test(usuarioRosita)
def CrearCategoria(request):
    formulario=CategoriaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('VerCategoria')
    return render(request,'Categoria/CrearCategoria.html', {'formulario':formulario})

@user_passes_test(usuarioRosita)
def BorrarCategoria(request, ID_CATEGORIA):
    cliente = Categoria.objects.get(ID_CATEGORIA=ID_CATEGORIA)
    cliente.delete()
    return redirect('VerCategoria')

@user_passes_test(usuarioRosita)
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



@login_required
def VerPedido(request):
    pedido = Pedido.objects.select_related('ID_PROVEEDOR_PEDIDO', 'ID_PRODUCTO_PEDIDO').all()
    return render (request, 'Pedido/VerPedido.html', {'pedido':pedido})

@user_passes_test(usuarioRosita)
def CrearPedido(request):
    formulario=PedidoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('VerPedido')
    return render(request,'Pedido/CrearPedido.html', {'formulario':formulario})

@user_passes_test(usuarioRosita)
def BorrarPedido(request, ID_PEDIDO):
    Pedid = Pedido.objects.get(ID_PEDIDO=ID_PEDIDO)
    Pedid.delete()
    return redirect('VerPedido')

@user_passes_test(usuarioRosita)
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

@user_passes_test(usuarioRosita)
def InformeVentas(request):

    resultados = Factura.objects.values('ID_CLIENTE_FACTURA__NOMBRE_CLIENTE').annotate(cantidad_facturas=Count('ID_CLIENTE_FACTURA'))

    resultadosproducto = Factura.objects.values('ID_PRODUCTO_FACTURA__DESCRIPCION_PRODUCTO').annotate(cantidad_productos=Count('ID_PRODUCTO_FACTURA'))

    df_resultados = pd.DataFrame(resultados)

    df_resultadosproducto = pd.DataFrame(resultadosproducto)

    # Crear la primera gráfica
    plt.figure(figsize=(8, 4))
    plt.bar(df_resultados['ID_CLIENTE_FACTURA__NOMBRE_CLIENTE'], df_resultados['cantidad_facturas'])
    plt.xlabel('Cliente')
    plt.ylabel('Cantidad de Facturas')
    plt.title('Ventas por Cliente')

    # Guardar la primera gráfica en un buffer
    buffer1 = io.BytesIO()
    plt.savefig(buffer1, format='png')
    buffer1.seek(0)
    image_base64 = base64.b64encode(buffer1.read()).decode('utf-8')

    # Crear la segunda gráfica
    plt.figure(figsize=(8, 4))
    plt.bar(df_resultadosproducto['ID_PRODUCTO_FACTURA__DESCRIPCION_PRODUCTO'], df_resultadosproducto['cantidad_productos'])
    plt.xlabel('Producto')
    plt.ylabel('Ventas por producto')
    plt.title('Ventas por Producto')

    # Guardar la segunda gráfica en un buffer
    buffer2 = io.BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    image_prod = base64.b64encode(buffer2.read()).decode('utf-8')


    resultadosPorProveedor = Factura.objects.values('ID_CLIENTE_FACTURA__NOMBRE_CLIENTE').annotate(total_precios=Sum('TOTAL_FACTURA'))

    resultadosPorProducto = Factura.objects.values('ID_PRODUCTO_FACTURA__DESCRIPCION_PRODUCTO').annotate(total_precios=Sum('TOTAL_FACTURA'))

    proveedores = [resultado['ID_CLIENTE_FACTURA__NOMBRE_CLIENTE'] for resultado in resultadosPorProveedor]
    total_precios = [resultado['total_precios'] for resultado in resultadosPorProveedor]
    plt.figure(figsize=(8, 8))
    plt.pie(total_precios, labels=proveedores, autopct=lambda p: '{:.1f}% ({:.0f})'.format(p, p * sum(total_precios) / 100), startangle=140)

    plt.title('Distribución de compras por cliente')

    buffer3 = io.BytesIO()
    plt.savefig(buffer3, format='png')
    buffer3.seek(0)
    imagenPorProveedor = base64.b64encode(buffer3.read()).decode('utf-8')


    proveedores = [resultado['ID_PRODUCTO_FACTURA__DESCRIPCION_PRODUCTO'] for resultado in resultadosPorProducto]
    total_precios = [resultado['total_precios'] for resultado in resultadosPorProducto]
    plt.figure(figsize=(8, 8))
    plt.pie(total_precios, labels=proveedores, autopct=lambda p: '{:.1f}% ({:.0f})'.format(p, p * sum(total_precios) / 100), startangle=140)

    plt.title('Distribución de compras por producto')

    buffer4 = io.BytesIO()
    plt.savefig(buffer4, format='png')
    buffer4.seek(0)
    imagenPorProducto = base64.b64encode(buffer4.read()).decode('utf-8')

    return render(request, 'Informe/InformeVentas.html', {'imagenPorProducto':imagenPorProducto, 'imagenPorProveedor':imagenPorProveedor, 'image_base64':image_base64, 'image_prod':image_prod} ) 


@user_passes_test(usuarioRosita)
def InformeVentasPDF(request):

    resultados = Factura.objects.values('ID_CLIENTE_FACTURA__NOMBRE_CLIENTE').annotate(cantidad_facturas=Count('ID_CLIENTE_FACTURA'))

    resultadosproducto = Factura.objects.values('ID_PRODUCTO_FACTURA__DESCRIPCION_PRODUCTO').annotate(cantidad_productos=Count('ID_PRODUCTO_FACTURA'))

    df_resultados = pd.DataFrame(resultados)

    df_resultadosproducto = pd.DataFrame(resultadosproducto)

    # Crear la primera gráfica
    plt.figure(figsize=(8, 4))
    plt.bar(df_resultados['ID_CLIENTE_FACTURA__NOMBRE_CLIENTE'], df_resultados['cantidad_facturas'])
    plt.xlabel('Cliente')
    plt.ylabel('Cantidad de Facturas')
    plt.title('Ventas por Cliente')

    # Guardar la primera gráfica en un buffer
    buffer1 = io.BytesIO()
    plt.savefig(buffer1, format='png')
    buffer1.seek(0)
    image_base64 = base64.b64encode(buffer1.read()).decode('utf-8')

    # Crear la segunda gráfica
    plt.figure(figsize=(8, 4))
    plt.bar(df_resultadosproducto['ID_PRODUCTO_FACTURA__DESCRIPCION_PRODUCTO'], df_resultadosproducto['cantidad_productos'])
    plt.xlabel('Producto')
    plt.ylabel('Ventas por producto')
    plt.title('Ventas por Producto')

    # Guardar la segunda gráfica en un buffer
    buffer2 = io.BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    image_prod = base64.b64encode(buffer2.read()).decode('utf-8')


    resultadosPorProveedor = Factura.objects.values('ID_CLIENTE_FACTURA__NOMBRE_CLIENTE').annotate(total_precios=Sum('TOTAL_FACTURA'))

    resultadosPorProducto = Factura.objects.values('ID_PRODUCTO_FACTURA__DESCRIPCION_PRODUCTO').annotate(total_precios=Sum('TOTAL_FACTURA'))

    proveedores = [resultado['ID_CLIENTE_FACTURA__NOMBRE_CLIENTE'] for resultado in resultadosPorProveedor]
    total_precios = [resultado['total_precios'] for resultado in resultadosPorProveedor]
    plt.figure(figsize=(8, 8))
    plt.pie(total_precios, labels=proveedores, autopct=lambda p: '{:.1f}% ({:.0f})'.format(p, p * sum(total_precios) / 100), startangle=140)

    plt.title('Distribución de compras por cliente')

    buffer3 = io.BytesIO()
    plt.savefig(buffer3, format='png')
    buffer3.seek(0)
    imagenPorProveedor = base64.b64encode(buffer3.read()).decode('utf-8')


    proveedores = [resultado['ID_PRODUCTO_FACTURA__DESCRIPCION_PRODUCTO'] for resultado in resultadosPorProducto]
    total_precios = [resultado['total_precios'] for resultado in resultadosPorProducto]
    plt.figure(figsize=(8, 8))
    plt.pie(total_precios, labels=proveedores, autopct=lambda p: '{:.1f}% ({:.0f})'.format(p, p * sum(total_precios) / 100), startangle=140)

    plt.title('Distribución de compras por producto')

    buffer4 = io.BytesIO()
    plt.savefig(buffer4, format='png')
    buffer4.seek(0)
    imagenPorProducto = base64.b64encode(buffer4.read()).decode('utf-8')

    # Obtener la fecha actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Crear un objeto PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="InformeDeVentas{fecha_actual}.pdf"'

    # Crear el documento PDF con ReportLab
    pdf = canvas.Canvas(response)

    # Guardar las imágenes en archivos temporales
    temp_image_base64 = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    temp_image_prod = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    temp_imagenPorProveedor = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    temp_imagenPorProducto = tempfile.NamedTemporaryFile(delete=False, suffix=".png")

    with open(temp_image_base64.name, 'wb') as img_file:
        img_file.write(base64.b64decode(image_base64))

    with open(temp_image_prod.name, 'wb') as img_file:
        img_file.write(base64.b64decode(image_prod))

    with open(temp_imagenPorProveedor.name, 'wb') as img_file:
        img_file.write(base64.b64decode(imagenPorProveedor))

    with open(temp_imagenPorProducto.name, 'wb') as img_file:
        img_file.write(base64.b64decode(imagenPorProducto))

    # Añadir las imágenes al documento PDF con ReportLab

    title = "Informe de ventas."
    title_width = pdf.stringWidth(title, "Helvetica", 16)
    pdf.setFont("Helvetica", 16)
    pdf.drawString((letter[0] - title_width) / 2, 800, title)

    pdf.drawString(100, 700, "Ventas por cliente")
    pdf.drawImage(ImageReader(temp_image_base64.name), 100, 450, width=400, height=200)

    pdf.drawString(100, 400, "Ventas por Producto")
    pdf.drawImage(ImageReader(temp_image_prod.name), 100, 150, width=400, height=200)

    # Cambiar a una nueva página
    pdf.showPage()

    pdf.drawString(100, 450, "Distribución de compras por clientes")
    pdf.drawImage(ImageReader(temp_imagenPorProveedor.name), 100, 350, width=400, height=400)

    pdf.drawString(100, 100, "Distribución de compras por producto")
    pdf.drawImage(ImageReader(temp_imagenPorProducto.name), 100, 10, width=400, height=400)

    pdf.save()

    # Cerrar y eliminar archivos temporales
    temp_image_base64.close()
    temp_image_prod.close()
    temp_imagenPorProveedor.close()

    return response







@user_passes_test(usuarioRosita)
def InformePedidos(request):

    resultados = Pedido.objects.values('ID_PROVEEDOR_PEDIDO__NOMBRE_PROVEEDOR').annotate(cantidad_facturas=Count('ID_PROVEEDOR_PEDIDO'))

    resultadosproducto = Pedido.objects.values('ID_PRODUCTO_PEDIDO__DESCRIPCION_PRODUCTO').annotate(cantidad_productos=Count('ID_PRODUCTO_PEDIDO'))

    df_resultados = pd.DataFrame(resultados)

    df_resultadosproducto = pd.DataFrame(resultadosproducto)

    # Crear la primera gráfica
    plt.figure(figsize=(8, 4))
    plt.bar(df_resultados['ID_PROVEEDOR_PEDIDO__NOMBRE_PROVEEDOR'], df_resultados['cantidad_facturas'])
    plt.xlabel('Proveedor')
    plt.ylabel('Cantidad de pedidos')
    plt.title('Pedidos por proveedor')

    # Guardar la primera gráfica en un buffer
    buffer1 = io.BytesIO()
    plt.savefig(buffer1, format='png')
    buffer1.seek(0)
    image_base64 = base64.b64encode(buffer1.read()).decode('utf-8')

    # Crear la segunda gráfica
    plt.figure(figsize=(8, 4))
    plt.bar(df_resultadosproducto['ID_PRODUCTO_PEDIDO__DESCRIPCION_PRODUCTO'], df_resultadosproducto['cantidad_productos'])
    plt.xlabel('Producto')
    plt.ylabel('Numero de Pedidos')
    plt.title('pedidos por producto')

    # Guardar la segunda gráfica en un buffer
    buffer2 = io.BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    image_prod = base64.b64encode(buffer2.read()).decode('utf-8')

    
    resultadosPorProveedor = Pedido.objects.values('ID_PROVEEDOR_PEDIDO__NOMBRE_PROVEEDOR').annotate(total_precios=Sum('PRECIO_TOTAL'))
    
    resultadosPorProducto = Pedido.objects.values('ID_PRODUCTO_PEDIDO__DESCRIPCION_PRODUCTO').annotate(total_precios=Sum('PRECIO_TOTAL'))
    
    # Extrae los datos para el gráfico
    proveedores = [resultado['ID_PROVEEDOR_PEDIDO__NOMBRE_PROVEEDOR'] for resultado in resultadosPorProveedor]
    total_precios = [resultado['total_precios'] for resultado in resultadosPorProveedor]
    # Crea el gráfico de torta
    plt.figure(figsize=(8, 8))
    plt.pie(total_precios, labels=proveedores, autopct=lambda p: '{:.1f}% ({:.0f})'.format(p, p * sum(total_precios) / 100), startangle=140)
 #   plt.pie(total_precios, labels=proveedores, autopct='%1.1f%%', startangle=140)
    # Añade un título
    plt.title('Distribución de precios por proveedor')

    buffer3 = io.BytesIO()
    plt.savefig(buffer3, format='png')
    buffer3.seek(0)
    imagenPorProveedor = base64.b64encode(buffer3.read()).decode('utf-8')


    proveedores = [resultado['ID_PRODUCTO_PEDIDO__DESCRIPCION_PRODUCTO'] for resultado in resultadosPorProducto]
    total_precios = [resultado['total_precios'] for resultado in resultadosPorProducto]
    plt.figure(figsize=(8, 8))
    plt.pie(total_precios, labels=proveedores, autopct=lambda p: '{:.1f}% ({:.0f})'.format(p, p * sum(total_precios) / 100), startangle=140)

    plt.title('Distribución de precios por producto')

    buffer4 = io.BytesIO()
    plt.savefig(buffer4, format='png')
    buffer4.seek(0)
    imagenPorProducto = base64.b64encode(buffer4.read()).decode('utf-8')

    return render(request, 'Informe/InformePedidos.html', {'imagenPorProducto':imagenPorProducto, 'imagenPorProveedor':imagenPorProveedor, 'image_base64':image_base64, 'image_prod':image_prod} ) 

@user_passes_test(usuarioRosita)
def InformePedidosPDF(request):

    resultados = Pedido.objects.values('ID_PROVEEDOR_PEDIDO__NOMBRE_PROVEEDOR').annotate(cantidad_facturas=Count('ID_PROVEEDOR_PEDIDO'))

    resultadosproducto = Pedido.objects.values('ID_PRODUCTO_PEDIDO__DESCRIPCION_PRODUCTO').annotate(cantidad_productos=Count('ID_PRODUCTO_PEDIDO'))

    df_resultados = pd.DataFrame(resultados)

    df_resultadosproducto = pd.DataFrame(resultadosproducto)

    plt.figure(figsize=(8, 4))
    plt.bar(df_resultados['ID_PROVEEDOR_PEDIDO__NOMBRE_PROVEEDOR'], df_resultados['cantidad_facturas'])
    plt.xlabel('Proveedor')
    plt.ylabel('Cantidad de pedidos')
    plt.title('Pedidos por proveedor')

    buffer1 = io.BytesIO()
    plt.savefig(buffer1, format='png')
    buffer1.seek(0)
    image_base64 = base64.b64encode(buffer1.read()).decode('utf-8')

    plt.figure(figsize=(8, 4))
    plt.bar(df_resultadosproducto['ID_PRODUCTO_PEDIDO__DESCRIPCION_PRODUCTO'], df_resultadosproducto['cantidad_productos'])
    plt.xlabel('Producto')
    plt.ylabel('Numero de Pedidos')
    plt.title('pedidos por producto')

    buffer2 = io.BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    image_prod = base64.b64encode(buffer2.read()).decode('utf-8')

    
    resultadosPorProveedor = Pedido.objects.values('ID_PROVEEDOR_PEDIDO__NOMBRE_PROVEEDOR').annotate(total_precios=Sum('PRECIO_TOTAL'))
    
    resultadosPorProducto = Pedido.objects.values('ID_PRODUCTO_PEDIDO__DESCRIPCION_PRODUCTO').annotate(total_precios=Sum('PRECIO_TOTAL'))
    
    proveedores = [resultado['ID_PROVEEDOR_PEDIDO__NOMBRE_PROVEEDOR'] for resultado in resultadosPorProveedor]
    total_precios = [resultado['total_precios'] for resultado in resultadosPorProveedor]

    plt.figure(figsize=(8, 8))
    plt.pie(total_precios, labels=proveedores, autopct=lambda p: '{:.1f}% ({:.0f})'.format(p, p * sum(total_precios) / 100), startangle=140)

    plt.title('Distribución de precios por proveedor')

    buffer3 = io.BytesIO()
    plt.savefig(buffer3, format='png')
    buffer3.seek(0)
    imagenPorProveedor = base64.b64encode(buffer3.read()).decode('utf-8')


    proveedores = [resultado['ID_PRODUCTO_PEDIDO__DESCRIPCION_PRODUCTO'] for resultado in resultadosPorProducto]
    total_precios = [resultado['total_precios'] for resultado in resultadosPorProducto]
    plt.figure(figsize=(8, 8))
    plt.pie(total_precios, labels=proveedores, autopct=lambda p: '{:.1f}% ({:.0f})'.format(p, p * sum(total_precios) / 100), startangle=140)

    plt.title('Distribución de precios por producto')

    buffer4 = io.BytesIO()
    plt.savefig(buffer4, format='png')
    buffer4.seek(0)
    imagenPorProducto = base64.b64encode(buffer4.read()).decode('utf-8')

    # Obtener la fecha actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Crear un objeto PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="InformeDePedidos{fecha_actual}.pdf"'

    # Crear el documento PDF con ReportLab
    pdf = canvas.Canvas(response)

    # Guardar las imágenes en archivos temporales
    temp_image_base64 = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    temp_image_prod = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    temp_imagenPorProveedor = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    temp_imagenPorProducto = tempfile.NamedTemporaryFile(delete=False, suffix=".png")

    with open(temp_image_base64.name, 'wb') as img_file:
        img_file.write(base64.b64decode(image_base64))

    with open(temp_image_prod.name, 'wb') as img_file:
        img_file.write(base64.b64decode(image_prod))

    with open(temp_imagenPorProveedor.name, 'wb') as img_file:
        img_file.write(base64.b64decode(imagenPorProveedor))

    with open(temp_imagenPorProducto.name, 'wb') as img_file:
        img_file.write(base64.b64decode(imagenPorProducto))

    # Añadir las imágenes al documento PDF con ReportLab

    title = "Informe de compras a proveedores."
    title_width = pdf.stringWidth(title, "Helvetica", 16)
    pdf.setFont("Helvetica", 16)
    pdf.drawString((letter[0] - title_width) / 2, 800, title)

    pdf.drawString(100, 700, "Compras por Proveedor")
    pdf.drawImage(ImageReader(temp_image_base64.name), 100, 450, width=400, height=200)

    pdf.drawString(100, 400, "Compras por Producto")
    pdf.drawImage(ImageReader(temp_image_prod.name), 100, 150, width=400, height=200)

    # Cambiar a una nueva página
    pdf.showPage()

    pdf.drawString(100, 450, "Distribución de precios por proveedor")
    pdf.drawImage(ImageReader(temp_imagenPorProveedor.name), 100, 350, width=400, height=400)

    pdf.drawString(100, 100, "Distribución de precios por producto")
    pdf.drawImage(ImageReader(temp_imagenPorProducto.name), 100, 10, width=400, height=400)

    pdf.save()

    # Cerrar y eliminar archivos temporales
    temp_image_base64.close()
    temp_image_prod.close()
    temp_imagenPorProveedor.close()

    return response