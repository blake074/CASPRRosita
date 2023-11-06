from django.urls import path
from . import views

urlpatterns = [
    path ('', views.Inicio, name='MenuPrincipal'),

    path ('VerFactura', views.VerFactura, name='VerFactura'),
    path ('CrearFactura', views.CrearFactura, name='CrearFactura'),

    path ('VerProducto', views.VerProducto, name='VerProducto'),
    path ('CrearProducto', views.CrearProducto, name='CrearProducto'),
    path ('MovimientoProductoVista', views.MovimientoProductoVista, name='MovimientoProductoVista'),
    path ('EditarProducto/<int:ID_PRODUCTO>',views.EditarProducto, name='EditarProducto'),

    path ('VerClientes', views.VerClientes, name='VerClientes'),
    path ('CrearCliente', views.CrearCliente, name='CrearCliente'),
    path ('BorrarClientes/<int:ID_CLIENTE>',views.BorrarClientes, name='BorrarClientes'),
    path ('EditarCliente/<int:ID_CLIENTE>',views.EditarCliente, name='EditarCliente'),

    path ('VerProveedores', views.VerProveedores, name='VerProveedores'),
    path ('CrearProveedor', views.CrearProveedor, name='CrearProveedor'),
    path ('BorrarProveedor/<int:ID_PROVEEDOR>',views.BorrarProveedor, name='BorrarProveedor'),
    path ('EditarProveedor/<int:ID_PROVEEDOR>',views.EditarProveedor, name='EditarProveedor'),

    path ('VerCategoria', views.VerCategoria, name='VerCategoria'),
    path ('CrearCategoria', views.CrearCategoria, name='CrearCategoria'),
    path ('BorrarCategoria/<int:ID_CATEGORIA>',views.BorrarCategoria, name='BorrarCategoria'),
    path ('EditarCategoria/<int:ID_CATEGORIA>',views.EditarCategoria, name='EditarCategoria'),

    path ('VerPedido', views.VerPedido, name='VerPedido'),
    path ('CrearPedido', views.CrearPedido, name='CrearPedido'),
    path ('BorrarPedido/<int:ID_PEDIDO>',views.BorrarPedido, name='BorrarPedido'),
    path ('EditarPedido/<int:ID_PEDIDO>',views.EditarPedido, name='EditarPedido'),



]