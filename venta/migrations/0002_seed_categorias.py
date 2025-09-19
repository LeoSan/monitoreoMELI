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
        "FOUND", 
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
    categoria_andadera, created = TCategoria.objects.get_or_create(nombre='Andaderas y correpasillos para bebés')
    categoria_orto, created = TCategoria.objects.get_or_create(nombre='Andaderas ortopédicas')

    # 2. Lista 
    dummy_productos_modelo = [
        {
            "nombre": "Andadera Caminadera Musical Interactiva Plegable Para Bebé Juguete Educativo Interactiva Seguro Multifuncional Color Azul Nube",
            "descripcion": "Andadera Caminadera Musical Interactiva Plegable Para Bebé Juguete Educativo Interactiva Seguro Multifuncional Color Azul Nube",
            "sku": "ANDA-BEBÉ-659A-AZUL",
            "precio_tachado": 729.00,
            "precio_oferta": 488.00,
            "total_stock": 220,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/andadera-caminadera-musical-interactiva-plegable-para-bebe-juguete-educativo-interactiva-seguro-multifuncional-color-azul-nube/p/MLM35709810?pdp_filters=item_id:MLM2049662411",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_andadera,  # Asignar la primera categoría disponible
        },
        {
            "nombre": "Andadera Caminadera Musical Interactiva Plegable Para Bebé Juguete Educativo Interactiva Seguro Multifuncional Color Morado Nube",
            "descripcion": "Andadera Caminadera Musical Interactiva Plegable Para Bebé Juguete Educativo Interactiva Seguro Multifuncional Color Morado Nube",
            "sku": "ANDA-BEBÉ-659A-LILA",
            "precio_tachado": 729.00,
            "precio_oferta": 488.00,
            "total_stock": 188,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/andadera-caminadera-musical-interactiva-plegable-para-bebe-juguete-educativo-interactiva-seguro-multifuncional-color-morado-nube/p/MLM36314855?pdp_filters=item_id:MLM2059349051",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_andadera,  # Asignar la primera categoría disponible
        },
        {
            "nombre": "Andadera Caminadera Musical Interactiva Plegable Para Bebé Juguete Educativo Interactiva Seguro Multifuncional Color Rosa Nube",
            "descripcion": "Andadera Caminadera Musical Interactiva Plegable Para Bebé Juguete Educativo Interactiva Seguro Multifuncional Color Rosa Nube",
            "sku": "ANDA-BEBÉ-659A-ROSA",
            "precio_tachado": 729.00,
            "precio_oferta": 488.00,
            "total_stock": 263,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/andadera-caminadera-musical-interactiva-plegable-para-bebe-juguete-educativo-interactiva-seguro-multifuncional-color-rosa-nube/p/MLM35610877?pdp_filters=item_id:MLM3005066268",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_andadera,  # Asignar la primera categoría disponible
        },
        {
            "nombre": "Andadera Musical Para Bebé Interactiva Plegable Con Ruedas Color Verde",
            "descripcion": "Andadera Musical Para Bebé Interactiva Plegable Con Ruedas Color Verde",
            "sku": "ANDA-BEBÉ-659A-VERDE",
            "precio_tachado": 729.00,
            "precio_oferta": 488.00,
            "total_stock": 122,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/andadera-musical-para-bebe-interactiva-plegable-con-ruedas-color-verde/p/MLM36185115?pdp_filters=item_id:MLM3032027580",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_andadera,  # Asignar la primera categoría disponible
        },
        {
            "nombre": "Andadera Ortopédica Adulto Asiento Silla Con Ruedas Nube",
            "descripcion": "Andadera Ortopédica Adulto Asiento Silla Con Ruedas Nube",
            "sku": "ANDA-ORTO-NB003-MARINO",
            "precio_tachado": 3499,
            "precio_oferta": 1399,
            "total_stock": 230,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://articulo.mercadolibre.com.mx/MLM-3348269400-andadera-ortopedica-adulto-asiento-silla-con-ruedas-nube-_JM",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_orto,  # Asignar la primera categoría disponible
        },         
        {
            "nombre": "Andadera Ortopédica Adulto Asiento Silla Con Ruedas Nube",
            "descripcion": "Andadera Ortopédica Adulto Asiento Silla Con Ruedas Nube",
            "sku": "ANDA-ORTO-NB003-GRIS",
            "precio_tachado": 3499,
            "precio_oferta": 1399,
            "total_stock": 223,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://articulo.mercadolibre.com.mx/MLM-3348269400-andadera-ortopedica-adulto-asiento-silla-con-ruedas-nube-_JM",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_orto,  # Asignar la primera categoría disponible
        },         
        {
            "nombre": "Andadera Ortopédica Adulto Asiento Silla Con Ruedas Nube",
            "descripcion": "Andadera Ortopédica Adulto Asiento Silla Con Ruedas Nube",
            "sku": "ANDA-ORTO-NB003-ROJO",
            "precio_tachado": 3499,
            "precio_oferta": 1399,
            "total_stock": 202,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://articulo.mercadolibre.com.mx/MLM-3348269400-andadera-ortopedica-adulto-asiento-silla-con-ruedas-nube-_JM",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_orto,  # Asignar la primera categoría disponible
        },         
    ]

    # 3. Iteramos y creamos 
    for producto_data in dummy_productos_modelo:
        TProductos.objects.get_or_create(**producto_data)     


def crear_una_competencia_inicial(apps, schema_editor):

    # Obtenemos los modelos necesarios para la migración
    TMarca = apps.get_model('venta', 'TMarcas')
    TProductos = apps.get_model('venta', 'TProductos')
    TProductoCompetencias = apps.get_model('venta', 'TProductoCompetencias')

    # 1. Creamos 
    ##ANDADERAS BEBES MUSICALES VIGOREM
    marca, created = TMarca.objects.get_or_create(nombre='VIGOREM')
    producto_anda_azul, created = TProductos.objects.get_or_create(sku='ANDA-BEBÉ-659A-AZUL')
    producto_anda_lila, created = TProductos.objects.get_or_create(sku='ANDA-BEBÉ-659A-LILA')
    producto_anda_rosa, created = TProductos.objects.get_or_create(sku='ANDA-BEBÉ-659A-ROSA')
    producto_anda_verde, created = TProductos.objects.get_or_create(sku='ANDA-BEBÉ-659A-VERDE')

    # 2. Lista 
    dummy_competencia = [
        {
            "nombre_producto": "Andadera Caminadera Musical Plegable KIDDOS Bebe Juguete Educativo Interactiva Segura Multifuncional Color Azul",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/andadera-caminadera-musical-plegable-kiddos-bebe-juguete-educativo-interactiva-segura-multifuncional-color-azul/p/MLM43982375#polycard_client=search_best-seller&tracking_id=d3efc8cb-5745-4e7a-bfdf-b92b7ed3568b&wid=MLM3480979894&sid=search",
            "productos_fk": producto_anda_azul,
            "marca_fk": marca,
        },
        {
            "nombre_producto": "Andadera Caminadera Musical Plegable KIDDOS Bebe Juguete Educativo Interactiva Segura Multifuncional Color Azul",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/andadera-caminadera-musical-plegable-kiddos-bebe-juguete-educativo-interactiva-segura-multifuncional-color-azul/p/MLM43982375#polycard_client=search_best-seller&tracking_id=d3efc8cb-5745-4e7a-bfdf-b92b7ed3568b&wid=MLM3480979894&sid=search",
            "productos_fk": producto_anda_lila,
            "marca_fk": marca,
        },
        {
            "nombre_producto": "Andadera Caminadera Musical Plegable KIDDOS Bebe Juguete Educativo Interactiva Segura Multifuncional Color Azul",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/andadera-caminadera-musical-plegable-kiddos-bebe-juguete-educativo-interactiva-segura-multifuncional-color-azul/p/MLM43982375#polycard_client=search_best-seller&tracking_id=d3efc8cb-5745-4e7a-bfdf-b92b7ed3568b&wid=MLM3480979894&sid=search",
            "productos_fk": producto_anda_rosa,
            "marca_fk": marca,
        },
        {
            "nombre_producto": "Andadera Caminadera Musical Plegable KIDDOS Bebe Juguete Educativo Interactiva Segura Multifuncional Color Azul",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/andadera-caminadera-musical-plegable-kiddos-bebe-juguete-educativo-interactiva-segura-multifuncional-color-azul/p/MLM43982375#polycard_client=search_best-seller&tracking_id=d3efc8cb-5745-4e7a-bfdf-b92b7ed3568b&wid=MLM3480979894&sid=search",
            "productos_fk": producto_anda_verde,
            "marca_fk": marca,
        }
    ]

    # 3. Iteramos y creamos 
    for producto_data in dummy_competencia:
        TProductoCompetencias.objects.get_or_create(**producto_data)  


class Migration(migrations.Migration):

    dependencies = [
        # Asegúrate de que apunte a tu última migración
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(crear_marcas_iniciales),
        migrations.RunPython(crear_categorias_iniciales),
        migrations.RunPython(crear_un_producto_inicial),
        migrations.RunPython(crear_una_competencia_inicial),
    ]
