from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Factura)
admin.site.register(MovimientoProducto)
admin.site.register(Pedido)