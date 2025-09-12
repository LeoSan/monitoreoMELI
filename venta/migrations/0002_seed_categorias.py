# migrations/000Y_seed_categorias.py

# 0006_seed_categorias.py
from django.db import migrations

def crear_marcas_iniciales(apps, schema_editor):

    # Obtenemos los modelos necesarios para la migración
    TMarcas = apps.get_model('venta', 'TMarcas')

    # 2. Lista de nombres de categorías a crear
    nombres_marcas = [
        "NUBE", 
        "BAZARU", 
        "KABUDU", 
        "VIGOREM", 
    ]

    # 3. Iteramos y creamos cada categoría, evitando duplicados
    for nombre_marcas in nombres_marcas:
        TMarcas.objects.get_or_create(
            nombre=nombre_marcas,
            descripcion="Marca generada automáticamente",
        )


def crear_categorias_iniciales(apps, schema_editor):

    # Obtenemos los modelos necesarios para la migración
    TMarca = apps.get_model('venta', 'TMarcas')
    TCategoria = apps.get_model('venta', 'TCategorias')

    # 1. Creamos o recuperamos la marca genérica para asociar las categorías
    marca_NUBE, created = TMarca.objects.get_or_create(nombre='NUBE')

    # 2. Lista de nombres de categorías a crear
    nombres_categorias = [
        "Andaderas ortopédicas", "Andaderas y correpasillos para bebés",
        "Baterías de cocina", "Bicicletas", "Bicicletas de equilibrio",
        "Camillas y sillas para masajes", "Campanas, extractores y purificadores de cocina",
        "Carriolas para bebés", "Carritos de mandados", "Centros de actividades y gimnasios para bebés",
        "Cobijas y mantas", "Colchas y cobertores", "Colchones",
        "Cortinas y persianas manuales para interiores", "Cubre colchones",
        "Cubrebocas quirúrgicos e industriales", "Cubresillas", "Escurridores de trastes",
        "Extractores de leche", "Fabricadoras de hielo", "Fundas para sofás, futones y sillones",
        "Ganchos para ropa", "Gazebos plegables", "Hidrolavadoras", "Jarras eléctricas",
        "Lámparas de piso, techo y pared", "Licuadoras", "Maletas", "Mancuernas",
        "Máquinas de cortar cabello, afeitadoras eléctricas y recortadoras de cabello",
        "Mesas de exterior", "Mini trampolines", "Parrillas", "Percheros", "Sábanas",
        "Sillas de baño y ducha", "Sillas de comedor", "Sillas mecedoras para bebé",
        "Sillas, bancos y sillones de jardín", "Sillas y banquetas de camping",
        "Soldadoras", "Tiendas de campaña infantiles", "Tinas de baño para bebés",
        "Triciclos infantiles", "Ventiladores", "Zapateras"
    ]

    # 3. Iteramos y creamos cada categoría, evitando duplicados
    for nombre_cat in nombres_categorias:
        TCategoria.objects.get_or_create(
            nombre=nombre_cat,
            marca_fk=marca_NUBE
        )

        
def crear_un_producto_inicial(apps, schema_editor):

    # Obtenemos los modelos necesarios para la migración
    TMarca = apps.get_model('venta', 'TMarcas')
    TCategoria = apps.get_model('venta', 'TCategorias')
    TProductos = apps.get_model('venta', 'TProductos')

    # 1. Creamos 
    marca_NUBE, created = TMarca.objects.get_or_create(nombre='NUBE')
    categoria_asignar, created = TCategoria.objects.get_or_create(nombre='Andaderas y correpasillos para bebés')

    # 2. Lista 
    dummy_productos = {
        "nombre": "Andadera Caminadera Musical Interactiva Plegable Para Bebé Juguete Educativo Interactiva Seguro Multifuncional Color Azul Nube",
        "descripcion": "Andadera Caminadera Musical Interactiva Plegable Para Bebé Juguete Educativo Interactiva Seguro Multifuncional Color Azul Nube",
        "sku": "SKU12345",
        "precio_tachado": 698.00,
        "precio_oferta": 0,
        "total_stock": 100,
        "activo": True,
        "imagen": "http://example.com/imagen.jpg",
        "marca_fk": marca_NUBE,
        "categoria_fk": categoria_asignar,  # Asignar la primera categoría disponible
    }

    # 3. Iteramos y creamos 
    for producto in dummy_productos:
        TProductos.objects.get_or_create(
            nombre=producto['nombre'],
            descripcion=producto['descripcion'],
            sku=producto['sku'],
            precio_tachado=producto['precio_tachado'],
            precio_oferta=producto['precio_oferta'],
            total_stock=producto['total_stock'],
            activo=producto['activo'],
            imagen=producto['imagen'],
            marca_fk=producto['marca_fk'],
            categoria_fk=producto['categoria_fk'],                   
        )        

def crear_una_competencia_inicial(apps, schema_editor):

    # Obtenemos los modelos necesarios para la migración
    TMarca = apps.get_model('venta', 'TMarcas')
    TProductos = apps.get_model('venta', 'TProductos')

    # 1. Creamos 
    marca, created = TMarca.objects.get_or_create(nombre='VIGOREM')
    producto_asignar, created = TProductos.objects.get_or_create(nombre='Andadera Caminadera Musical Interactiva Plegable Para Bebé Juguete Educativo Interactiva Seguro Multifuncional Color Azul Nube')

    # 2. Lista 
    dummy_competencia = {
        "nombre_producto": "Andadera Caminadera Musical Plegable KIDDOS Bebe Juguete Educativo Interactiva Segura Multifuncional Color Azul",
        "precio": 0,
        "precio_tachado": 0,
        "url": "https://www.mercadolibre.com.mx/andadera-caminadera-musical-plegable-kiddos-bebe-juguete-educativo-interactiva-segura-multifuncional-color-azul/p/MLM43982375#polycard_client=search_best-seller&tracking_id=d3efc8cb-5745-4e7a-bfdf-b92b7ed3568b&wid=MLM3480979894&sid=search",
        "productos_fk": producto_asignar,
        "marca_fk": marca,
    }

    # 3. Iteramos y creamos 
    for producto in dummy_competencia:
        TProductos.objects.get_or_create(
            nombre_producto=producto['nombre_producto'],
            precio=producto['precio'],
            precio_tachado=producto['precio_tachado'],
            url=producto['url'],
            productos_fk=producto['productos_fk'],
            marca_fk=producto['marca_fk'],
        ) 


class Migration(migrations.Migration):

    dependencies = [
        # Asegúrate de que apunte a tu última migración
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(crear_marcas_iniciales),
        migrations.RunPython(crear_categorias_iniciales),
        migrations.RunPython(crear_un_producto_inicial),
    ]