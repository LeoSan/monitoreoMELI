# python
from django.test import TestCase
from .models import TMarcas

class TMarcasModelTest(TestCase):
    def test_create_full_fields(self):
        marca = TMarcas.objects.create(
            nombre="NUBE",
            descripcion="Marca de prueba",
            url="http://example.com",
            activo=True
        )
        self.assertEqual(marca.nombre, "NUBE")
        self.assertEqual(marca.descripcion, "Marca de prueba")
        self.assertEqual(marca.url, "http://example.com")
        self.assertTrue(marca.activo)

    def test_create_only_required_fields(self):
        marca = TMarcas.objects.create(nombre="BAZARU")
        self.assertEqual(marca.nombre, "BAZARU")
        self.assertIsNone(marca.descripcion)
        self.assertIsNone(marca.url)
        self.assertTrue(marca.activo)

    def test_str_representation(self):
        marca = TMarcas.objects.create(nombre="KABUDU", activo=False)
        self.assertEqual(str(marca), "KABUDU - False")

    def test_update_marca(self):
        marca = TMarcas.objects.create(nombre="VIGOREM")
        marca.descripcion = "Nueva descripción"
        marca.activo = False
        marca.save()
        marca.refresh_from_db()
        self.assertEqual(marca.descripcion, "Nueva descripción")
        self.assertFalse(marca.activo)

    def test_delete_marca(self):
        marca = TMarcas.objects.create(nombre="FOUND")
        marca_id = marca.id
        marca.delete()
        self.assertFalse(TMarcas.objects.filter(id=marca_id).exists())

    def test_filter_activo(self):
        TMarcas.objects.create(nombre="ACTIVA", activo=True)
        TMarcas.objects.create(nombre="INACTIVA", activo=False)
        activas = TMarcas.objects.filter(activo=True)
        inactivas = TMarcas.objects.filter(activo=False)
        self.assertEqual(activas.count(), 1)
        self.assertEqual(inactivas.count(), 1)

    def test_duplicate_nombre(self):
        TMarcas.objects.create(nombre="DUPLICADA")
        marca2 = TMarcas.objects.create(nombre="DUPLICADA")
        self.assertEqual(marca2.nombre, "DUPLICADA")