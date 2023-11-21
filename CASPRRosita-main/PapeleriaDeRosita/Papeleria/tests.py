from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Cliente, Proveedor, Producto, Factura, Pedido, Categoria
from .forms import LoginForm, ClienteForm, ProveedorForm, ProductoForm, FacturaForm, PedidoForm, CategoriaForm

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('Rosita', 'test@test.com', 'testpassword')  # Cambia 'testuser' a 'Rosita'
        self.client.login(username='Rosita', password='testpassword')  # Cambia 'testuser' a 'Rosita'

    def test_inicio_view(self):
        response = self.client.get(reverse('MenuPrincipal'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'MenuPrincipal.html')

    def test_ver_factura_view(self):
        response = self.client.get(reverse('VerFactura'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Factura/VerFactura.html')

    def test_ver_producto_view(self):
        response = self.client.get(reverse('VerProducto'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Producto/VerProducto.html')

    def test_ver_clientes_view(self):
        response = self.client.get(reverse('VerClientes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Cliente/VerCliente.html')

    def test_ver_proveedores_view(self):
        response = self.client.get(reverse('VerProveedores'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Proveedor/VerProveedor.html')

    def test_ver_categoria_view(self):
        response = self.client.get(reverse('VerCategoria'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Categoria/VerCategoria.html')

    def test_ver_pedido_view(self):
        response = self.client.get(reverse('VerPedido'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Pedido/VerPedido.html')

    def test_crear_factura_view(self):
        form_data = {
            'ID_CLIENTE_FACTURA': 1,
            'ID_PRODUCTO_FACTURA': 1,
            'CANTIDAD_VENDIDA': 10,
            'SUBTOTAL_FACTURA': 100.0,
            'TOTAL_FACTURA': 110.0,
            'DESC_FACTURA': 'Factura de prueba',
            'FECHA_FACTURA': '2023-12-31',
        }
        response = self.client.post(reverse('CrearFactura'), form_data)

    def test_crear_factura_view_invalido(self):
        form_data = {
            'ID_CLIENTE_FACTURA': 1,
            'ID_PRODUCTO_FACTURA': 1,
            'CANTIDAD_VENDIDA': 10,
            'SUBTOTAL_FACTURA': 100.0,
            'TOTAL_FACTURA': '',  # Total vacío no es válido
            'DESC_FACTURA': 'Factura de prueba',
            'FECHA_FACTURA': '2023-12-31',
        }
        response = self.client.post(reverse('CrearFactura'), form_data)
        self.assertEqual(response.status_code, 200)  # Esperamos que la página se vuelva a renderizar con errores

    def test_crear_producto_view(self):
        form_data = {
            'ID_CATEGORIA_PRODUCTO': 1,
            'DESCRIPCION_PRODUCTO': 'Producto de prueba',
            'CANTIDAD_EXIS_PRODUCTO': 10,
            'PRECIO_VENTA_PRODUCTO': 100.0,
            'IVA_FACTURA': 10.0,
            'ESTADO_PRODUCTO': 'A',
        }
        response = self.client.post(reverse('CrearProducto'), form_data)

    def test_crear_producto_view_invalido(self):
        form_data = {
            'ID_CATEGORIA_PRODUCTO': 1,
            'DESCRIPCION_PRODUCTO': '',  # Descripción vacía no es válida
            'CANTIDAD_EXIS_PRODUCTO': 10,
            'PRECIO_VENTA_PRODUCTO': 100.0,
            'IVA_FACTURA': 10.0,
            'ESTADO_PRODUCTO': 'A',
        }
        response = self.client.post(reverse('CrearProducto'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_crear_cliente_view(self):
        form_data = {
            'NOMBRE_CLIENTE': 'Nombre de prueba',
            'APELLIDO_CLIENTE': 'Apellido de prueba',
            'DIRECCION_CLIENTE': 'Direccion de prueba',
            'TELEFONO_CLIENTE': '1234567890',
            'CORREO_CLIENTE': 'cliente@prueba.com',
            
        }
        response = self.client.post(reverse('CrearCliente'), form_data)
        self.assertEqual(response.status_code, 302)

    def test_crear_cliente_view_invalido(self):
        form_data = {
            'NOMBRE_CLIENTE': '',  # Nombre vacío no es válido
            'APELLIDO_CLIENTE': 'Apellido de prueba',
            'DIRECCION_CLIENTE': 'Direccion de prueba',
            'TELEFONO_CLIENTE': '1234567890',
            'CORREO_CLIENTE': 'cliente@prueba.com',
        }
        response = self.client.post(reverse('CrearCliente'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_crear_proveedor_view(self):
        response = self.client.post(reverse('CrearProveedor'), {
            'NOMBRE_PROVEEDOR': 'Proveedor de prueba',
            'DIRECCION_PROVEEDOR': 'Direccion de prueba',
            'CORREO_PROVEEDOR': 'proveedor@prueba.com',
            'TELEFONO_PROVEEDOR': '1234567890',
            'ESTADO_PROVEEDOR': 'A',
           
        })
        self.assertEqual(response.status_code, 302)  

    def test_crear_proveedor_view_invalido(self):
        form_data = {
            'NOMBRE_PROVEEDOR': '',  # Nombre vacío no es válido
            'DIRECCION_PROVEEDOR': 'Direccion de prueba',
            'CORREO_PROVEEDOR': 'proveedor@prueba.com',
            'TELEFONO_PROVEEDOR': '1234567890',
            'ESTADO_PROVEEDOR': 'A',
            # Asegúrate de incluir cualquier otro campo que tu formulario requiera
        }
        response = self.client.post(reverse('CrearProveedor'), form_data)
        self.assertEqual(response.status_code, 200)

    def test_crear_categoria_view(self):
        form_data = {
            'DESCRIPCION_CATEGORIA': 'Categoria de prueba',
            'ESTADO_PRODUCTO': 'A',
        }
        response = self.client.post(reverse('CrearCategoria'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('VerCategoria'))
        self.assertEqual(Categoria.objects.count(), 1)

    def test_crear_categoria_view_invalido(self):
        form_data = {
            'DESCRIPCION_CATEGORIA': '',  # Campo vacío, lo que debería ser inválido
            'ESTADO_PRODUCTO': 'A',
        }
        response = self.client.post(reverse('CrearCategoria'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Categoria.objects.count(), 0)

    def test_crear_pedido_view(self):
        form_data = {
            'ID_PROVEEDOR_PEDIDO': 1,  
            'ID_PRODUCTO_PEDIDO': 1,  
            'CANTIDAD_COMPRADA': 10,
            'PRECIO_TOTAL': 100.0,
            'FECHA_PEDIDO': '2023-01-01',
            'FECHA_PEDIDO_LLEGADA': '2023-01-02',
            'ESTADO_PEDIDO': 'A',
        }
        response = self.client.post(reverse('CrearPedido'), form_data)



    def test_crear_pedido_view_invalido(self):
        form_data = {
            'ID_PROVEEDOR_PEDIDO': 1,  # Pasa el ID del proveedor
            'ID_PRODUCTO_PEDIDO': 1,  # Pasa el ID del producto
            'CANTIDAD_COMPRADA': 20,  # Cambiamos la cantidad comprada
            'PRECIO_TOTAL': -200.0,  # Un precio total negativo debería ser inválido
            'FECHA_PEDIDO': '2023-01-01',
            'FECHA_PEDIDO_LLEGADA': '2023-01-02',
            'ESTADO_PEDIDO': 'A',
        }
        response = self.client.post(reverse('CrearPedido'), form_data)
        # Comprueba que la respuesta tiene un código de estado 200 (éxito)
        # Esto es porque la vista debería volver a mostrar el formulario con errores
        self.assertEqual(response.status_code, 200)
        # Comprueba que no se ha creado ningún pedido nuevo
        self.assertEqual(Pedido.objects.count(), 0)

    def test_editar_proveedor_view(self):
        # Primero, crea un objeto Proveedor para editar
        proveedor = Proveedor.objects.create(
            NOMBRE_PROVEEDOR='Proveedor de prueba',
            DIRECCION_PROVEEDOR='Direccion de prueba',
            CORREO_PROVEEDOR='proveedor@prueba.com',
            TELEFONO_PROVEEDOR='1234567890',
            ESTADO_PROVEEDOR='A',
        )

        response = self.client.post(reverse('EditarProveedor', args=[proveedor.ID_PROVEEDOR]), {
            'NOMBRE_PROVEEDOR': 'Proveedor de prueba actualizado',
            'DIRECCION_PROVEEDOR': 'Direccion de prueba actualizada',
            'CORREO_PROVEEDOR': 'proveedoractualizado@prueba.com',
            'TELEFONO_PROVEEDOR': '0987654321',
            'ESTADO_PROVEEDOR': 'I',
        })

        if response.status_code == 200:
            form = ProveedorForm(response.context['form'].initial)
            print(form.errors)

    def tearDown(self):
        self.user.delete()
