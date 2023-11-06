# Generated by Django 3.2.8 on 2023-11-05 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Papeleria', '0003_auto_20231105_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='DESC_FACTURA',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Descuento en la factura'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='IVA_FACTURA',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='IVA del producto'),
        ),
    ]