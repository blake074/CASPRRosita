# Generated by Django 3.2.8 on 2023-11-01 04:21

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('ID_CATEGORIA', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la categoria')),
                ('DESCRIPCION_CATEGORIA', models.CharField(max_length=30, verbose_name='Descripcion de la categoria')),
                ('ESTADO_PRODUCTO', models.CharField(max_length=1, verbose_name='Estado de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('ID_CLIENTE', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del empleado')),
                ('NOMBRE_CLIENTE', models.CharField(max_length=30, verbose_name='Nombre del cliente')),
                ('APELLIDO_CLIENTE', models.CharField(max_length=30, verbose_name='Apellido del cliente')),
                ('DIRECCION_CLIENTE', models.CharField(max_length=30, verbose_name='Direccion de residencia del cliente')),
                ('TELEFONO_CLIENTE', models.CharField(max_length=30, verbose_name='Telefono del cliente')),
                ('CORREO_CLIENTE', models.CharField(max_length=30, verbose_name='Correo del cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('ID_PROVEEDOR', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del proveedor')),
                ('NOMBRE_PROVEEDOR', models.CharField(max_length=30, verbose_name='Nombre del proveedor')),
                ('DIRECCION_PROVEEDOR', models.CharField(max_length=30, verbose_name='Direccion del proveedor')),
                ('CORREO_PROVEEDOR', models.CharField(max_length=30, verbose_name='Correo del proveedor')),
                ('TELEFONO_PROVEEDOR', models.CharField(max_length=30, verbose_name='Telefono del proveedor')),
                ('ESTADO_PROVEEDOR', models.CharField(max_length=1, verbose_name='Estado del proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('ID_PRODUCTO', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del producto')),
                ('DESCRIPCION_PRODUCTO', models.CharField(max_length=30, verbose_name='Descripcion del producto')),
                ('CANTIDAD_EXIS_PRODUCTO', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0, message='La cantidad no puede ser negativa.')], verbose_name='Cantidad de existencias del producto')),
                ('PRECIO_VENTA_PRODUCTO', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0, message='La cantidad no puede ser negativa.')], verbose_name='Precio de venta unitario del producto')),
                ('ESTADO_PRODUCTO', models.CharField(max_length=1, verbose_name='Estado del producto')),
                ('ID_CATEGORIA_PRODUCTO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Papeleria.categoria', verbose_name='ID de la categoria del producto')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('ID_PEDIDO', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del pedido')),
                ('CANTIDAD_COMPRADA', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0, message='La cantidad no puede ser negativa.')], verbose_name='Cantidad de existencias compradas')),
                ('PRECIO_TOTAL', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0, message='La cantidad no puede ser negativa.')], verbose_name='Total de la compra')),
                ('ESTADO_PEDIDO', models.CharField(max_length=1, verbose_name='Estado del pedido')),
                ('ID_PRODUCTO_PEDIDO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Papeleria.producto', verbose_name='ID del producto que se compro')),
                ('ID_PROVEEDOR_PEDIDO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Papeleria.proveedor', verbose_name='ID del proveedor al que se le hizo el pedido')),
            ],
        ),
        migrations.CreateModel(
            name='MovimientoProducto',
            fields=[
                ('ID_MOVIMIENTO', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del movimiento')),
                ('DESCRIPCION_MOVIMIENTO', models.CharField(max_length=30, verbose_name='Descripcion del movimiento')),
                ('CANTIDAD_MOVIMIENTO', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0, message='La cantidad no puede ser negativa.')], verbose_name='Cantidad de existencias adquiridas/vendidas en el movimiento')),
                ('FECHA_MOVIMIENTO', models.DateField(default=datetime.date.today, verbose_name='Fecha del movimiento')),
                ('ID_PRODUCTO_MOVIMIENTO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Papeleria.producto', verbose_name='ID del producto que se le hizo el movimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('ID_FACTURA', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la factura')),
                ('CANTIDAD_VENDIDA', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0, message='La cantidad no puede ser negativa.')], verbose_name='Cantidad de existencias vendidas')),
                ('SUBTOTAL_FACTURA', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0, message='La cantidad no puede ser negativa.')], verbose_name='Subtotal de la factura')),
                ('TOTAL_FACTURA', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0, message='La cantidad no puede ser negativa.')], verbose_name='Total de la factura')),
                ('DESC_FACTURA', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Descuento en la factura')),
                ('IVA_FACTURA', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='IVA en la factura')),
                ('SALDO_FACTURA', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0, message='La cantidad no puede ser negativa.')], verbose_name='Saldo de la factura')),
                ('FECHA_FACTURA', models.DateField(default=datetime.date.today, verbose_name='Fecha de generacion de la factura')),
                ('ID_CLIENTE_FACTURA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Papeleria.cliente', verbose_name='ID del cliente al que se le creo la factura')),
                ('ID_PRODUCTO_FACTURA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Papeleria.producto', verbose_name='ID del producto que se compro')),
            ],
        ),
    ]