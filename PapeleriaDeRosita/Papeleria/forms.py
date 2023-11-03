from django import forms
from .models import *

from django.core.validators import validate_email


class FacturaForm(forms.ModelForm):
    class Meta:
        model= Factura
        fields = ('ID_CLIENTE_FACTURA', 'ID_PRODUCTO_FACTURA', 'CANTIDAD_VENDIDA', 'SUBTOTAL_FACTURA', 'TOTAL_FACTURA', 'DESC_FACTURA', 'IVA_FACTURA', 'SALDO_FACTURA', 'FECHA_FACTURA')
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
        fields = ('ID_CATEGORIA_PRODUCTO', 'DESCRIPCION_PRODUCTO', 'CANTIDAD_EXIS_PRODUCTO', 'PRECIO_VENTA_PRODUCTO', 'ESTADO_PRODUCTO')
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
