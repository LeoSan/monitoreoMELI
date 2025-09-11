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

class Migration(migrations.Migration):

    dependencies = [
        # Asegúrate de que apunte a tu última migración
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(crear_marcas_iniciales),
        migrations.RunPython(crear_categorias_iniciales),
    ]