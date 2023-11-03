from django.urls import path
from . import views

urlpatterns = [
    path ('', views.Inicio, name='MenuPrincipal'),

    path ('VerFactura', views.VerFactura, name='VerFactura'),
    path ('CrearFactura', views.CrearFactura, name='CrearFactura'),

    path ('VerProducto', views.VerProducto, name='VerProducto'),
    path ('CrearProducto', views.CrearProducto, name='CrearProducto'),
    path ('MovimientoProductoVista', views.MovimientoProductoVista, name='MovimientoProductoVista'),

    path ('VerClientes', views.VerClientes, name='VerClientes'),
    path ('CrearCliente', views.CrearCliente, name='CrearCliente'),

    path ('VerProveedores', views.VerProveedores, name='VerProveedores'),
    path ('CrearProveedor', views.CrearProveedor, name='CrearProveedor'),

    path ('VerCategoria', views.VerCategoria, name='VerCategoria'),
    path ('CrearCategoria', views.CrearCategoria, name='CrearCategoria'),


]