from django.db import models
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Cliente(models.Model):
    ID_CLIENTE=models.AutoField(primary_key=True, verbose_name="ID del empleado");
    NOMBRE_CLIENTE=models.CharField(max_length=30, verbose_name="Nombre del cliente", null=False);
    APELLIDO_CLIENTE=models.CharField(max_length=30, verbose_name="Apellido del cliente",null=False);
    DIRECCION_CLIENTE=models.CharField(max_length=30, verbose_name="Direccion de residencia del cliente",null=False);
    TELEFONO_CLIENTE=models.CharField(max_length=30, verbose_name="Telefono del cliente",null=False);
    CORREO_CLIENTE=models.CharField(max_length=30, verbose_name="Correo del cliente",null=False);
    def __str__(self):
        return self.NOMBRE_CLIENTE

class Proveedor(models.Model):
    ID_PROVEEDOR=models.AutoField(primary_key=True, verbose_name="ID del proveedor");
    NOMBRE_PROVEEDOR=models.CharField(max_length=30, verbose_name="Nombre del proveedor", null=False);
    DIRECCION_PROVEEDOR=models.CharField(max_length=30, verbose_name="Direccion del proveedor",null=False);
    CORREO_PROVEEDOR=models.CharField(max_length=30, verbose_name="Correo del proveedor",null=False);
    TELEFONO_PROVEEDOR=models.CharField(max_length=30, verbose_name="Telefono del proveedor",null=False);
    ESTADO_PROVEEDOR=models.CharField(max_length=1, verbose_name="Estado del proveedor",null=False);
    def __str__(self):
        return self.NOMBRE_PROVEEDOR

class Categoria(models.Model):
    ID_CATEGORIA=models.AutoField(primary_key=True, verbose_name="ID de la categoria");
    DESCRIPCION_CATEGORIA=models.CharField(max_length=30, verbose_name="Descripcion de la categoria",null=False);
    ESTADO_PRODUCTO=models.CharField(max_length=1, verbose_name="Estado de la categoria",null=False);
    def __str__(self):
        return self.DESCRIPCION_CATEGORIA


class Producto(models.Model):
    ID_PRODUCTO=models.AutoField(primary_key=True, verbose_name="ID del producto");
    ID_CATEGORIA_PRODUCTO=models.ForeignKey('Categoria', on_delete=models.CASCADE, verbose_name="ID de la categoria del producto",null=False);
    DESCRIPCION_PRODUCTO=models.CharField(max_length=30, verbose_name="Descripcion del producto",null=False);
    CANTIDAD_EXIS_PRODUCTO=models.IntegerField(verbose_name="Cantidad de existencias del producto",null=False, validators=[
            MinValueValidator(limit_value=0, message="La cantidad no puede ser negativa.")
        ]);
    PRECIO_VENTA_PRODUCTO=models.IntegerField(verbose_name="Precio de venta unitario del producto",null=False, validators=[
            MinValueValidator(limit_value=0, message="La cantidad no puede ser negativa.")
        ]);
    IVA_FACTURA=models.DecimalField(max_digits=5, decimal_places=2, verbose_name="IVA del producto",null=False, default=0.00);
    ESTADO_PRODUCTO=models.CharField(max_length=1, verbose_name="Estado del producto",null=False);
    def __str__(self):
        return self.DESCRIPCION_PRODUCTO

class Factura(models.Model):
    ID_FACTURA=models.AutoField(primary_key=True, verbose_name="ID de la factura");
    ID_PRODUCTO_FACTURA=models.ForeignKey('Producto', on_delete=models.CASCADE, verbose_name="ID del producto que se compro",null=False);
    ID_CLIENTE_FACTURA=models.ForeignKey('Cliente', on_delete=models.CASCADE, verbose_name="ID del cliente al que se le creo la factura", null=False);
    CANTIDAD_VENDIDA=models.IntegerField(verbose_name="Cantidad de existencias vendidas",null=False, validators=[
            MinValueValidator(limit_value=0, message="La cantidad no puede ser negativa.")
        ]);
    SUBTOTAL_FACTURA=models.IntegerField(verbose_name="Subtotal de la factura",null=False, validators=[
            MinValueValidator(limit_value=0, message="La cantidad no puede ser negativa.")
        ]);
    TOTAL_FACTURA=models.IntegerField(verbose_name="Total de la factura",null=False, validators=[
            MinValueValidator(limit_value=0, message="La cantidad no puede ser negativa.")
        ]);
    DESC_FACTURA=models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Descuento en la factura",null=False);
    FECHA_FACTURA=models.DateField(default=date.today, verbose_name="Fecha de generacion de la factura",null=False);

class MovimientoProducto(models.Model):
    ID_MOVIMIENTO=models.AutoField(primary_key=True, verbose_name="ID del movimiento");
    ID_PRODUCTO_MOVIMIENTO=models.ForeignKey('Producto', on_delete=models.CASCADE, verbose_name="ID del producto que se le hizo el movimiento",null=False);
    DESCRIPCION_MOVIMIENTO=models.CharField(max_length=30, verbose_name="Descripcion del movimiento",null=False);
    CANTIDAD_MOVIMIENTO=models.IntegerField(verbose_name="Cantidad de existencias adquiridas/vendidas en el movimiento",null=False, validators=[
            MinValueValidator(limit_value=0, message="La cantidad no puede ser negativa.")
        ]);
    FECHA_MOVIMIENTO=models.DateField(default=date.today, verbose_name="Fecha del movimiento",null=False);

class Pedido(models.Model):
    ID_PEDIDO=models.AutoField(primary_key=True, verbose_name="ID del pedido");
    ID_PROVEEDOR_PEDIDO=models.ForeignKey('Proveedor', on_delete=models.CASCADE, verbose_name="ID del proveedor al que se le hizo el pedido",null=False);
    ID_PRODUCTO_PEDIDO=models.ForeignKey('Producto', on_delete=models.CASCADE, verbose_name="ID del producto que se compro",null=False);
    CANTIDAD_COMPRADA=models.IntegerField(verbose_name="Cantidad de existencias compradas",null=False, validators=[
            MinValueValidator(limit_value=0, message="La cantidad no puede ser negativa.")
        ]);
    PRECIO_TOTAL=models.IntegerField(verbose_name="Total de la compra",null=False, validators=[
            MinValueValidator(limit_value=0, message="La cantidad no puede ser negativa.")
        ]);
    FECHA_PEDIDO=models.DateField(default=date.today, verbose_name="Fecha en que se realizo el pedido",null=False);
    FECHA_PEDIDO_LLEGADA=models.DateField(default=date.today, verbose_name="Fecha en la que se espera que llegue el pedido",null=False);
    ESTADO_PEDIDO=models.CharField(max_length=1, verbose_name="Estado del pedido",null=False);
