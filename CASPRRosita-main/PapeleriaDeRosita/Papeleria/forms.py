from django import forms
from .models import *

from django.core.validators import validate_email


class FacturaForm(forms.ModelForm):
    class Meta:
        model= Factura
        fields = ('ID_CLIENTE_FACTURA', 'ID_PRODUCTO_FACTURA', 'CANTIDAD_VENDIDA', 'SUBTOTAL_FACTURA', 'TOTAL_FACTURA', 'DESC_FACTURA',  'FECHA_FACTURA')
    def __init__(self, *args, **kwargs):
        super(FacturaForm, self).__init__(*args, **kwargs)
        # Cambiar el widget del campo de llave foránea para mostrar nombres en lugar de IDs
        self.fields['ID_PRODUCTO_FACTURA'].widget = forms.Select(choices=Producto.objects.values_list('ID_PRODUCTO', 'DESCRIPCION_PRODUCTO'))
        self.fields['ID_CLIENTE_FACTURA'].widget = forms.Select(choices=Cliente.objects.values_list('ID_CLIENTE', 'NOMBRE_CLIENTE'))
        # Puedes agregar widgets personalizados para campos de fecha si es necesario
        self.fields['FECHA_FACTURA'].widget = forms.SelectDateWidget()


class ProductoForm(forms.ModelForm):
    class Meta:
        model= Producto
        fields = ('ID_CATEGORIA_PRODUCTO', 'DESCRIPCION_PRODUCTO', 'CANTIDAD_EXIS_PRODUCTO', 'PRECIO_VENTA_PRODUCTO', 'IVA_FACTURA', 'ESTADO_PRODUCTO')
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        # Cambiar el widget del campo de llave foránea para mostrar nombres en lugar de IDs
        self.fields['ID_CATEGORIA_PRODUCTO'].widget = forms.Select(choices=Categoria.objects.values_list('ID_CATEGORIA', 'DESCRIPCION_CATEGORIA'))
       


class ClienteForm(forms.ModelForm):
    class Meta:
        model= Cliente
        fields = ('NOMBRE_CLIENTE', 'APELLIDO_CLIENTE', 'DIRECCION_CLIENTE', 'TELEFONO_CLIENTE', 'CORREO_CLIENTE')
    def clean_CORREO_CLIENTE(self):
        correo = self.cleaned_data['CORREO_CLIENTE']
        try:
            validate_email(correo)
        except:
            raise forms.ValidationError("Correo electrónico no válido. Ejemplo de correo: correo@hotmail.com")
        return correo

class ProveedorForm(forms.ModelForm):
    class Meta:
        model= Proveedor
        fields = ('NOMBRE_PROVEEDOR', 'DIRECCION_PROVEEDOR', 'CORREO_PROVEEDOR', 'TELEFONO_PROVEEDOR', 'ESTADO_PROVEEDOR')
    def clean_CORREO_PROVEEDOR(self):
        correo = self.cleaned_data['CORREO_PROVEEDOR']
        try:
            validate_email(correo)
        except:
            raise forms.ValidationError("Correo electrónico no válido. Ejemplo de correo: correo@hotmail.com")
        return correo

class CategoriaForm(forms.ModelForm):
    class Meta:
        model= Categoria
        fields = ('DESCRIPCION_CATEGORIA', 'ESTADO_PRODUCTO')

class PedidoForm(forms.ModelForm):
    class Meta:
        model= Pedido
        fields = ('ID_PROVEEDOR_PEDIDO', 'ID_PRODUCTO_PEDIDO', 'CANTIDAD_COMPRADA', 'PRECIO_TOTAL', 'FECHA_PEDIDO', 'FECHA_PEDIDO_LLEGADA', 'ESTADO_PEDIDO')
    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)

        self.fields['ID_PRODUCTO_PEDIDO'].widget = forms.Select(choices=Producto.objects.values_list('ID_PRODUCTO', 'DESCRIPCION_PRODUCTO'))
        self.fields['ID_PROVEEDOR_PEDIDO'].widget = forms.Select(choices=Proveedor.objects.values_list('ID_PROVEEDOR', 'NOMBRE_PROVEEDOR'))

        self.fields['FECHA_PEDIDO'].widget = forms.SelectDateWidget()
        self.fields['FECHA_PEDIDO_LLEGADA'].widget = forms.SelectDateWidget()
    def clean_ESTADO_PEDIDO(self):
        estado_pedido = self.cleaned_data['ESTADO_PEDIDO']
        
        if estado_pedido not in ['A', 'I']:
            raise forms.ValidationError("El estado del pedido debe ser 'A' (Activo) o 'I' (Inactivo).")

        return estado_pedido

    def clean(self):
        cleaned_data = super().clean()
        fecha_pedido = cleaned_data.get('FECHA_PEDIDO')
        fecha_pedido_llegada = cleaned_data.get('FECHA_PEDIDO_LLEGADA')

        if fecha_pedido and fecha_pedido_llegada and fecha_pedido_llegada <= fecha_pedido:
            self.add_error('FECHA_PEDIDO_LLEGADA', "La fecha de llegada debe ser posterior a la fecha en que se realiza el pedido.")