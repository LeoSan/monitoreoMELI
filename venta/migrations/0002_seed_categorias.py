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
        "BLUEWAVEBLUEWA", 
        "SHOPMALL", 
        "BLUELANDER", 
        "BIKE101", 
        "AMOSAGDL", 
        "ADIR", 
        "TECNOLAM", 
        "TRENDY_KIDS",
        "EASYTAO", 
    ]

    # 3. Iteramos y creamos cada categoría, evitando duplicados
    for nombre_marcas in nombres_marcas:
        
        
        TMarcas.objects.get_or_create(
            nombre=nombre_marcas,
            descripcion="Marca generada automáticamente",
            activo = True if nombre_marcas == 'NUBE' or nombre_marcas == 'BAZARU' or nombre_marcas == 'KABUDU' else False
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
        "Baterías de cocina", "Bicicletas de equilibrio", "Bicicletas", 
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
    categoria_bateria, created = TCategoria.objects.get_or_create(nombre='Baterías de cocina')
    categoria_bici_equi, created = TCategoria.objects.get_or_create(nombre='Bicicletas de equilibrio')
    categoria_bici, created = TCategoria.objects.get_or_create(nombre='Bicicletas')
    categoria_masaje, created = TCategoria.objects.get_or_create(nombre='Camillas y sillas para masajes')
    categoria_carri_compras, created = TCategoria.objects.get_or_create(nombre='Carritos de mandados')
    categoria_campanas, created = TCategoria.objects.get_or_create(nombre='Campanas, extractores y purificadores de cocina')
    categoria_carriolas, created = TCategoria.objects.get_or_create(nombre='Carriolas para bebés')
    categoria_centro_gym_bebe, created = TCategoria.objects.get_or_create(nombre='Centros de actividades y gimnasios para bebés')
    categoria_colchones, created = TCategoria.objects.get_or_create(nombre='Colchones')
    categoria_cortinas, created = TCategoria.objects.get_or_create(nombre='Cortinas y persianas manuales para interiores')
    categoria_cubre_colchon, created = TCategoria.objects.get_or_create(nombre='Cubre colchones')

    # 2. Lista 
    dummy_productos_modelo = [
        ## "Andaderas ortopédicas"
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
            "categoria_fk": categoria_orto,  
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
            "categoria_fk": categoria_orto,  
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
            "categoria_fk": categoria_orto,  
        },         
        ## "Andaderas y correpasillos para bebés"
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
            "categoria_fk": categoria_andadera,  
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
            "categoria_fk": categoria_andadera,  
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
            "categoria_fk": categoria_andadera,  
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
            "categoria_fk": categoria_andadera,  
        },
        ## "Baterías de cocina"
        {
            "nombre": "Bateria De Cocina Nube 10 Piezas Antiadherente Color Negra Negro",
            "descripcion": "Bateria De Cocina Nube 10 Piezas Antiadherente Color Negra Negro",
            "sku": "JUEG-COCI-UT-001-NEGRO",
            "precio_tachado":1350.00,
            "precio_oferta": 916.65,
            "total_stock": 287,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/bateria-de-cocina-nube-10-piezas-antiadherente-color-negra/up/MLMU819544792",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_bateria,  
        },
        ## Bicicletas de equilibrio
        {
            "nombre": "Bicicleta Sin Pedales Entrenadora Para Niños Equilibrio Nube Color Rosa",
            "descripcion": "Bicicleta Sin Pedales Entrenadora Para Niños Equilibrio Nube Color Rosa",
            "sku": "BICI-EQUI-YM-CB-1-ROSA",
            "precio_tachado":789.00,
            "precio_oferta": 389.65,
            "total_stock": 154,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/bicicleta-sin-pedales-entrenadora-para-ninos-equilibrio-nube-color-rosa/p/MLM42077782?pdp_filters=item_id:MLM3421928608",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_bici_equi,  
        },        
        {
            "nombre": "Bicicleta Sin Pedales Entrenadora Para Niños Equilibrio Nube Color Rojo",
            "descripcion": "Bicicleta Sin Pedales Entrenadora Para Niños Equilibrio Nube Color Rojo",
            "sku": "BICI-EQUI-YM-CB-1-ROJO",
            "precio_tachado":789.00,
            "precio_oferta": 389.65,
            "total_stock": 372,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/bicicleta-sin-pedales-entrenadora-para-ninos-equilibrio-nube-color-rojo/p/MLM48943561?pdp_filters=item_id:MLM3667189168",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_bici_equi,  
        },        
        {
            "nombre": "Bicicleta Sin Pedales Entrenadora Para Niños Equilibrio Nube Color Morado",
            "descripcion": "Bicicleta Sin Pedales Entrenadora Para Niños Equilibrio Nube Color Morado",
            "sku": "BICI-EQUI-YM-CB-1-MORADO",
            "precio_tachado":789.00,
            "precio_oferta": 389.65,
            "total_stock": 372,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/bicicleta-sin-pedales-entrenadora-para-ninos-equilibrio-nube-color-morado/p/MLM48943553?pdp_filters=item_id:MLM3667026750",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_bici_equi,  
        },       
        ## Bicicletas
        {
            "nombre": "Bicicleta De Montaña Rodada 26 Profesional 21v Nube",
            "descripcion": "Bicicleta De Montaña Rodada 26 Profesional 21v Nube",
            "sku": "BICI-MONT-MOD-003-B-ROJO",
            "precio_tachado":4299.00,
            "precio_oferta": 0,
            "total_stock": 0,
            "activo": False,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://articulo.mercadolibre.com.mx/MLM-2868470040-bicicleta-de-montana-rodada-26-profesional-21v-nube-_JM",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_bici,  
        },                 
        {
            "nombre": "Bicicleta De Montaña Rodada 26 Profesional 21v Nube",
            "descripcion": "Bicicleta De Montaña Rodada 26 Profesional 21v Nube",
            "sku": "BICI-MONT-MOD-003-B-AZUL",
            "precio_tachado":4299.00,
            "precio_oferta": 0,
            "total_stock": 0,
            "activo": False,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://articulo.mercadolibre.com.mx/MLM-2868470040-bicicleta-de-montana-rodada-26-profesional-21v-nube-_JM",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_bici,  
        },                 
        {
            "nombre": "Bicicleta De Aluminio R29 Doble Suspension Nube Color Rojo Tamaño del cuadro 29",
            "descripcion": "Bicicleta De Aluminio R29 Doble Suspension Nube Color Rojo Tamaño del cuadro 29",
            "sku": "BICI-MONT-MOD-002-B-ROJO",
            "precio_tachado":4299.00,
            "precio_oferta": 0,
            "total_stock": 0,
            "activo": False,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/bicicleta-de-aluminio-r29-doble-suspension-nube-color-rojo-tamano-del-cuadro-29/p/MLM46681659",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_bici,  
        },                 
        ## Camillas y sillas para masajes
        {
            "nombre": "Cama Masaje Profesional! Plegable Spa Portatil Tattoo",
            "descripcion": "Cama Masaje Profesional! Plegable Spa Portatil Tattoo",
            "sku": "CAMAMASAJEGRIS",
            "precio_tachado":2479.00,
            "precio_oferta": 1735.30,
            "total_stock": 0,
            "activo": False,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://articulo.mercadolibre.com.mx/MLM-1422572635-cama-masaje-profesional-plegable-spa-portatil-tattoo-_JM",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_masaje,  
        }, 
        ## Carritos de mandados
        {
            "nombre": "Carrito para Mandados de Compras Plegable Multiusos Resistente Nube Color Gris",
            "descripcion": "Carrito para Mandados de Compras Plegable Multiusos Resistente Nube Color Gris",
            "sku": "CARR-COMP-MOD-CC001-GRIS",
            "precio_tachado":399.00,
            "precio_oferta": 208,
            "total_stock": 150,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/carrito-para-mandados-de-compras-plegable-multiusos-resistente-nube-color-gris/p/MLM53340906?pdp_filters=item_id:MLM3928527640",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_carri_compras,  
        }, 
        {
            "nombre": "Carrito Para Mandados De Compras Plegable Multiusos Resistente Nube Color Azul",
            "descripcion": "Carrito Para Mandados De Compras Plegable Multiusos Resistente Nube Color Azul",
            "sku": "CARR-COMP-MOD-CC001-AZUL",
            "precio_tachado":399.00,
            "precio_oferta": 208,
            "total_stock": 150,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/carrito-para-mandados-de-compras-plegable-multiusos-resistente-nube-color-azul/p/MLM53607133?pdp_filters=item_id:MLM3928527650",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_carri_compras,  
        }, 
        ## Campanas, extractores y purificadores de cocina
        {
            "nombre": "Campana Extractora 75cm Botones De Pared Nube Plata",
            "descripcion": "Campana Extractora 75cm Botones De Pared Nube Plata",
            "sku": "CAMPABOT90CPLA027",
            "precio_tachado":4999.00,
            "precio_oferta": 3199.00,
            "total_stock": 11,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/campana-extractora-75cm-botones-de-pared-nube/up/MLMU718935559?pdp_filters=item_id:MLM3244460252",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_campanas,  
        },     
        ## Carriolas para bebés
        {
            "nombre": "Carriola De Baston Plegable Para Bebe Carreola Reclinable Color Negro Chasis Negro",
            "descripcion": "Carriola De Baston Plegable Para Bebe Carreola Reclinable Color Negro Chasis Negro",
            "sku": "CARR-ACCE-YMBT7P-PANDA NEGRO",
            "precio_tachado":1420.00,
            "precio_oferta": 989.00,
            "total_stock": 29,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/carriola-de-baston-plegable-para-bebe-carreola-reclinable-color-negro-chasis-negro/p/MLM41352955?pdp_filters=item_id:MLM3938643898",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_campanas,  
        },     
        {
            "nombre": "Carriola Baston Plegable Para Bebe Reclinable Con Bolsa Mamá Color Morado Con Bolsa Chasis Negro",
            "descripcion": "Carriola Baston Plegable Para Bebe Reclinable Con Bolsa Mamá Color Morado Con Bolsa Chasis Negro",
            "sku": "CARR-ACCE-YMBT7P-UNICORNIO MORADO",
            "precio_tachado":1420.00,
            "precio_oferta": 989.00,
            "total_stock": 42,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/carriola-baston-plegable-para-bebe-reclinable-con-bolsa-mama-color-morado-con-bolsa-chasis-negro/p/MLM53902225?pdp_filters=item_id:MLM3938593264",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_carriolas,  
        },     
        {
            "nombre": "Carriola De Baston Plegable Para Bebe Carreola Reclinable Color Azul Oscuro Chasis Negro",
            "descripcion": "Carriola De Baston Plegable Para Bebe Carreola Reclinable Color Azul Oscuro Chasis Negro",
            "sku": "CARR-ACCE-YMBT7P-PANDA AZUL",
            "precio_tachado":1420.00,
            "precio_oferta": 989.00,
            "total_stock": 38,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/carriola-de-baston-plegable-para-bebe-carreola-reclinable-color-azul-oscuro-chasis-negro/p/MLM40672046?pdp_filters=item_id:MLM2417731947",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_carriolas,  
        },     
        {
            "nombre": "Carriola De Baston Plegable Para Bebe Carreola Reclinable Color Gris Chasis Negro",
            "descripcion": "Carriola De Baston Plegable Para Bebe Carreola Reclinable Color Gris Chasis Negro",
            "sku": "CARR-ACCE-YMBT7P-PANDA GRIS",
            "precio_tachado":1420.00,
            "precio_oferta": 989.00,
            "total_stock": 62,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/carriola-de-baston-plegable-para-bebe-carreola-reclinable-color-gris-chasis-negro/p/MLM41355001?pdp_filters=item_id:MLM3942825282",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_carriolas,  
        },
        ## Centros de actividades y gimnasios para bebés 
        {
            "nombre": "Gimnasio Bebé Interactivo Tapete Didáctico Infantil Nube",
            "descripcion": "Gimnasio Bebé Interactivo Tapete Didáctico Infantil Nube",
            "sku": "GIMBEBESPACAZU361",
            "precio_tachado":899.00,
            "precio_oferta": 439.00,
            "total_stock": 383,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/carriola-de-baston-plegable-para-bebe-carreola-reclinable-color-azul-oscuro-chasis-negro/p/MLM40672046?pdp_filters=item_id:MLM2417731947",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_centro_gym_bebe,  
        },             
        {
            "nombre": "Gimnasio Bebé Interactivo Tapete Didáctico Infantil Nube",
            "descripcion": "Gimnasio Bebé Interactivo Tapete Didáctico Infantil Nube",
            "sku": "GIMBEBUNICOROS363",
            "precio_tachado":899.00,
            "precio_oferta": 439.00,
            "total_stock": 238,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/carriola-de-baston-plegable-para-bebe-carreola-reclinable-color-azul-oscuro-chasis-negro/p/MLM40672046?pdp_filters=item_id:MLM2417731947",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_centro_gym_bebe,  
        },
        ## Colchones
        {
            "nombre": "Colchon En Caja Matrimonial Memory Foam Con Resorte",
            "descripcion": "Colchon En Caja Matrimonial Memory Foam Con Resorte",
            "sku": "COLC-RESO-MR-2451-MAT-CAJA",
            "precio_tachado":4789.00,
            "precio_oferta": 1858.10,
            "total_stock": 360,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/colchon-en-caja-matrimonial-memory-foam-con-resorte/up/MLMU708650365",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_colchones,  
        },        
        {
            "nombre": "Colchón Nube Memory Foam Matrimonial Firme Cooling Gel Tech Blanco",
            "descripcion": "Colchón Nube Memory Foam Matrimonial Firme Cooling Gel Tech Blanco",
            "sku": "GIMBEBUNICOROS363",
            "precio_tachado":4799.00,
            "precio_oferta": 2048.20,
            "total_stock": 61,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/colchon-nube-memory-foam-matrimonial-firme-cooling-gel-tech/up/MLMU3162730071",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_colchones,  
        },        
        {
            "nombre": "Colchón Nube Memory Foam Matrimonial Firme Cooling Gel Tech Blanco",
            "descripcion": "Colchón Nube Memory Foam Matrimonial Firme Cooling Gel Tech Blanco",
            "sku": "COLC-SM01-135-MAT",
            "precio_tachado":12000.00,
            "precio_oferta": 4899.20,
            "total_stock": 32,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/colchon-nube-memory-foam-matrimonial-firme-cooling-gel-tech/up/MLMU3162730071",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_colchones,  
        },         
        {
            "nombre": "Colchón Individual Nube Premium Memory Foam Anti Movimiento",
            "descripcion": "Colchón Individual Nube Premium Memory Foam Anti Movimiento",
            "sku": "COLC-RESO-PSM01-100-INDIVIDUAL",
            "precio_tachado":12000.00,
            "precio_oferta": 3009.30,
            "total_stock": 41,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/colchon-individual-nube-premium-memory-foam-anti-movimiento/up/MLMU3168270490",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_colchones,  
        },         
        {
            "nombre": "Colchón King Size Nube Premium Memory Foam Anti Movimiento",
            "descripcion": "Colchón King Size Nube Premium Memory Foam Anti Movimiento",
            "sku": "COLC-RESO-PSM01-200-KING",
            "precio_tachado":12000.00,
            "precio_oferta": 4899.30,
            "total_stock": 71,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/colchon-king-size-nube-premium-memory-foam-anti-movimiento/p/MLM53349971?pdp_filters=item_id:MLM3881655008",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_colchones,  
        },         
        {
            "nombre": "Colchón Matrimonial Nube Premium Memory Foam Anti Movimiento",
            "descripcion": "Colchón Matrimonial Nube Premium Memory Foam Anti Movimiento",
            "sku": "COLC-RESO-PSM01-135-MATRIMONIAL",
            "precio_tachado":12000.00,
            "precio_oferta": 3919.30,
            "total_stock": 246,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/colchon-matrimonial-nube-premium-memory-foam-anti-movimiento/p/MLM53364226?pdp_filters=item_id:MLM3883249152",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_colchones,  
        },         
        {
            "nombre": "Colchón Nube Memory Foam Individual Firme Cooling Gel Tech",
            "descripcion": "Colchón Nube Memory Foam Individual Firme Cooling Gel Tech",
            "sku": "COLC-SM01-100-INDI",
            "precio_tachado":12000.00,
            "precio_oferta": 3240.30,
            "total_stock": 48,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/colchon-nube-memory-foam-individual-firme-cooling-gel-tech/up/MLMU3168239786",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_colchones,  
        },         
        {
            "nombre": "Colchón Nube Matrimonial Memory Foam Tecno Alemana Premium",
            "descripcion": "Colchón Nube Matrimonial Memory Foam Tecno Alemana Premium",
            "sku": "COLC-SMAH01-135-MAT",
            "precio_tachado":18000.00,
            "precio_oferta": 4899,
            "total_stock": 222,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/colchon-nube-matrimonial-memory-foam-tecno-alemana-premium/up/MLMU3188786735",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_colchones,  
        },         
        {
            "nombre": "Colchón Nube Individual Memory Foam Tecno Alemana Premium",
            "descripcion": "Colchón Nube Individual Memory Foam Tecno Alemana Premium",
            "sku": "COLC-SMAH01-135-MAT",
            "precio_tachado":18000.00,
            "precio_oferta": 2989,
            "total_stock": 49,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/colchon-nube-individual-memory-foam-tecno-alemana-premium/up/MLMU3188777741",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_colchones,  
        },         
        {
            "nombre": "Colchón Nube King Memory Foam Tecno Alemana Premium",
            "descripcion": "Colchón Nube King Memory Foam Tecno Alemana Premium",
            "sku": "COLC-SMAH01-200-KIN",
            "precio_tachado":18000.00,
            "precio_oferta": 5899,
            "total_stock": 116,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/colchon-nube-king-memory-foam-tecno-alemana-premium/up/MLMU3188868557",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_colchones,  
        }, 
        ## Cortinas y persianas manuales para interiores   
        {
            "nombre": "Cortina Blackout Premium Quality! 2 Paneles 280x220cm VINO",
            "descripcion": "Cortina Blackout Premium Quality! 2 Paneles 280x220cm VINO",
            "sku": "CORT-BLAC-CORB-24-VINO",
            "precio_tachado":503.99,
            "precio_oferta": 238,
            "total_stock": 239,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://articulo.mercadolibre.com.mx/MLM-1459671640-cortina-blackout-premium-quality-2-paneles-280x220cm-_JM",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_cortinas,  
        },              
        {
            "nombre": "Cortina Blackout Premium Quality! 2 Paneles 280x220cm BEIGE",
            "descripcion": "Cortina Blackout Premium Quality! 2 Paneles 280x220cm BEIGE",
            "sku": "CORT-BLAC-CORB-24-BEIGE",
            "precio_tachado":503.99,
            "precio_oferta": 238,
            "total_stock": 90,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://articulo.mercadolibre.com.mx/MLM-1459671640-cortina-blackout-premium-quality-2-paneles-280x220cm-_JM",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_cortinas,  
        },              
        {
            "nombre": "Cortina Blackout Premium Quality! 2 Paneles 280x220cm NEGRO",
            "descripcion": "Cortina Blackout Premium Quality! 2 Paneles 280x220cm NEGRO",
            "sku": "CORT-BLAC-CORB-24-NEGRO",
            "precio_tachado":503.99,
            "precio_oferta": 238,
            "total_stock": 135,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://articulo.mercadolibre.com.mx/MLM-1459671640-cortina-blackout-premium-quality-2-paneles-280x220cm-_JM",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_cortinas,  
        },              
        {
            "nombre": "Cortina Blackout Premium Quality! 2 Paneles 280x220cm OXFORD",
            "descripcion": "Cortina Blackout Premium Quality! 2 Paneles 280x220cm OXFORD",
            "sku": "CORT-BLAC-CORB-24-OXFORD",
            "precio_tachado":503.99,
            "precio_oferta": 238,
            "total_stock": 92,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://articulo.mercadolibre.com.mx/MLM-1459671640-cortina-blackout-premium-quality-2-paneles-280x220cm-_JM",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_cortinas,  
        },              
        {
            "nombre": "Cortina Blackout Premium Quality! 2 Paneles 280x220cm CHOCOLATE",
            "descripcion": "Cortina Blackout Premium Quality! 2 Paneles 280x220cm CHOCOLATE",
            "sku": "CORT-BLAC-CORB-24-CHOCOLATE",
            "precio_tachado":503.99,
            "precio_oferta": 238,
            "total_stock": 306,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://articulo.mercadolibre.com.mx/MLM-1459671640-cortina-blackout-premium-quality-2-paneles-280x220cm-_JM",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_cortinas,  
        },              
        {
            "nombre": "Cortina Blackout Premium Quality! 2 Paneles 280x220cm TAUPE",
            "descripcion": "Cortina Blackout Premium Quality! 2 Paneles 280x220cm TAUPE",
            "sku": "CORT-BLAC-CORB-24-TAUPE",
            "precio_tachado":503.99,
            "precio_oferta": 238,
            "total_stock": 612,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://articulo.mercadolibre.com.mx/MLM-1459671640-cortina-blackout-premium-quality-2-paneles-280x220cm-_JM",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_cortinas,  
        },              
        {
            "nombre": "Set 2 Cortinas Blackout 280x220cm Lisa Premium Grabada Nube",
            "descripcion": "Set 2 Cortinas Blackout 280x220cm Lisa Premium Grabada Nube",
            "sku": "CORTBLACKOUTSHEDRONTULIP",
            "precio_tachado":429.99,
            "precio_oferta": 179,
            "total_stock": 49,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://articulo.mercadolibre.com.mx/MLM-1427382130-set-2-cortinas-blackout-280x220cm-lisa-premium-grabada-nube-_JM",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_cortinas,  
        },              
        {
            "nombre": "Set 2 Cortinas Blackout 280x220cm Lisa Premium Grabada Nube",
            "descripcion": "Set 2 Cortinas Blackout 280x220cm Lisa Premium Grabada Nube",
            "sku": "CORTBLACKOUTMALVATULIP",
            "precio_tachado":429.99,
            "precio_oferta": 179,
            "total_stock": 368,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://articulo.mercadolibre.com.mx/MLM-1427382130-set-2-cortinas-blackout-280x220cm-lisa-premium-grabada-nube-_JM",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_cortinas,  
        },
        ## Cubre colchones
        {
            "nombre": "Cubrecolchón Suave Cubrecolchon Antiacaros Cloud Sleep Blanco A Prueba De Agua Matrimonial De 137 X 192 X 40cm Modelo Mr-112",
            "descripcion": "Cubrecolchón Suave Cubrecolchon Antiacaros Cloud Sleep Blanco A Prueba De Agua Matrimonial De 137 X 192 X 40cm Modelo Mr-112",
            "sku": "CUBR-COLC-MR-112-MAT",
            "precio_tachado":449,
            "precio_oferta": 249,
            "total_stock": 1583,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/cubrecolchon-suave-cubrecolchon-antiacaros-cloud-sleep-blanco-a-prueba-de-agua-matrimonial-de-137-x-192-x-40cm-modelo-mr-112/p/MLM35579769#polycard_client=search_best-seller&tracking_id=d545d6bb-3256-42ba-83bb-322de7ebb12c&wid=MLM3004978178&sid=search",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_cubre_colchon,  
        },                      
        {
            "nombre": "Cubrecolchón Suave Cubrecolchon Antiacaros Cloud Sleep Blanco A Prueba De Agua King Size De 202 X 192 X 40cm Modelo Mr-112",
            "descripcion": "Cubrecolchón Suave Cubrecolchon Antiacaros Cloud Sleep Blanco A Prueba De Agua King Size De 202 X 192 X 40cm Modelo Mr-112",
            "sku": "CUBR-COLC-MR-112-KZ",
            "precio_tachado":449,
            "precio_oferta": 278,
            "total_stock": 837,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/cubrecolchon-suave-cubrecolchon-antiacaros-cloud-sleep-blanco-a-prueba-de-agua-king-size-de-202-x-192-x-40cm-modelo-mr-112/p/MLM27957074?pdp_filters=item_id:MLM2660824948",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_cubre_colchon,  
        },                      
        {
            "nombre": "Protector Cubre Colchón Impermeable Antiacaros Individual Color Blanco 192x102x40 Modelo Mr-112",
            "descripcion": "Cubrecolchón Suave Cubrecolchon Antiacaros Cloud Sleep Blanco A Prueba De Agua King Size De 202 X 192 X 40cm Modelo Mr-112",
            "sku": "CUBR-COLC-MR-112-IND",
            "precio_tachado":549,
            "precio_oferta": 176,
            "total_stock": 389,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/protector-cubre-colchon-impermeable-antiacaros-individual-color-blanco-192x102x40-modelo-mr-112/p/MLM53342247?pdp_filters=item_id:MLM3881651006",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_cubre_colchon,  
        },                      
        {
            "nombre": "Protector Colchón Hipoalergénico Impermeable Matrimonial Blanco Liso Cubre Cama Funda Colchon Cubrecolchon 137x192x40cm Mod Fsm",
            "descripcion": "Protector Colchón Hipoalergénico Impermeable Matrimonial Blanco Liso Cubre Cama Funda Colchon Cubrecolchon 137x192x40cm Mod Fsm",
            "sku": "CUBR-COLC-FSMF01-135-MAT",
            "precio_tachado":500,
            "precio_oferta": 189,
            "total_stock": 568,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/protector-colchon-hipoalergenico-impermeable-matrimonial-blanco-liso-cubre-cama-funda-colchon-cubrecolchon-137x192x40cm-mod-fsm/p/MLM54005750?pdp_filters=item_id:MLM3966971004",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_cubre_colchon,  
        },                      
        {
            "nombre": "Protector De Colchón Hipoalergénico Impermeable Individual Blanco Liso Individual Modelo Fsm",
            "descripcion": "Protector De Colchón Hipoalergénico Impermeable Individual Blanco Liso Individual Modelo Fsm",
            "sku": "CUBR-COLC-FSMF01-100-IND",
            "precio_tachado":400,
            "precio_oferta": 158,
            "total_stock": 542,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/protector-de-colchon-hipoalergenico-impermeable-individual-blanco-liso-individual-modelo-fsm/p/MLM53341587?pdp_filters=item_id:MLM3881650394",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_cubre_colchon,  
        },                      
        {
            "nombre": "Protector De Colchón King Size Hipoalergénico Impermeable Blanco Liso King Modelo Fsm",
            "descripcion": "Protector De Colchón King Size Hipoalergénico Impermeable Blanco Liso King Modelo Fsm",
            "sku": "CUBR-COLC-FSMF01-200-KZ",
            "precio_tachado":600,
            "precio_oferta": 210,
            "total_stock": 414,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/protector-de-colchon-hipoalergenico-impermeable-individual-blanco-liso-individual-modelo-fsm/p/MLM53341587?pdp_filters=item_id:MLM3881650394",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_cubre_colchon,  
        },                      
        {
            "nombre": "Cubrecolchón Impermeable Toallin A Prueba De Agua Individual Blanco Textura Individual",
            "descripcion": "Cubrecolchón Impermeable Toallin A Prueba De Agua Individual Blanco Textura Individual",
            "sku": "CUBR-COLC-FSCT01-100-IND",
            "precio_tachado":400,
            "precio_oferta": 169,
            "total_stock": 188,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/cubrecolchon-impermeable-toallin-a-prueba-de-agua-individual-blanco-textura-individual/p/MLM53602834?pdp_filters=item_id:MLM3903153102",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_cubre_colchon,  
        },                      
        {
            "nombre": "Cubrecolchon Impermeable Toallin Matrimonial 1.92mx1.37mx40c Blanco Textura Matrimonial",
            "descripcion": "Cubrecolchon Impermeable Toallin Matrimonial 1.92mx1.37mx40c Blanco Textura Matrimonial",
            "sku": "CUBR-COLC-FSCT01-135-MAT",
            "precio_tachado":500,
            "precio_oferta": 185,
            "total_stock": 152,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/cubrecolchon-impermeable-toallin-a-prueba-de-agua-individual-blanco-textura-individual/p/MLM53602834?pdp_filters=item_id:MLM3903153102",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_cubre_colchon,  
        },                      
        {
            "nombre": "Cubrecolchon Impermeable Toallin King Size 2.02mx1.92mx40cm",
            "descripcion": "Cubrecolchon Impermeable Toallin King Size 2.02mx1.92mx40cm",
            "sku": "CUBR-COLC-FSCT01-200-KZ",
            "precio_tachado":600,
            "precio_oferta": 218,
            "total_stock": 45,
            "activo": True,
            "imagen": "http://example.com/imagen.jpg",
            "url": "https://www.mercadolibre.com.mx/cubrecolchon-impermeable-toallin-a-prueba-de-agua-individual-blanco-textura-individual/p/MLM53602834?pdp_filters=item_id:MLM3903153102",
            "marca_fk": marca_NUBE,
            "categoria_fk": categoria_cubre_colchon,  
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

    # 1. Consultamos Marca de competencia ya creada  
    marca_vigorem, created = TMarca.objects.get_or_create(nombre='VIGOREM')
    marca_FOUND, created = TMarca.objects.get_or_create(nombre='FOUND')
    marca_bateria, created = TMarca.objects.get_or_create(nombre='BLUEWAVEBLUEWA')
    marca_bici_equi, created = TMarca.objects.get_or_create(nombre='SHOPMALL')
    marca_bicicletas, created = TMarca.objects.get_or_create(nombre='BLUELANDER')
    marca_bicicletas_B, created = TMarca.objects.get_or_create(nombre='BIKE101')
    marca_camilla_masajes, created = TMarca.objects.get_or_create(nombre='AMOSAGDL')
    marca_carrito_compras, created = TMarca.objects.get_or_create(nombre='ADIR')
    marca_campana, created = TMarca.objects.get_or_create(nombre='TECNOLAM')
    marca_carriola, created = TMarca.objects.get_or_create(nombre='TRENDY_KIDS')
    marca_easytao, created = TMarca.objects.get_or_create(nombre='EASYTAO')


    # 2. Consultamos Productos ya creado 
    ##ANDADERAS BEBES MUSICALES VIGOREM
    producto_anda_azul, created = TProductos.objects.get_or_create(sku='ANDA-BEBÉ-659A-AZUL')
    producto_anda_lila, created = TProductos.objects.get_or_create(sku='ANDA-BEBÉ-659A-LILA')
    producto_anda_rosa, created = TProductos.objects.get_or_create(sku='ANDA-BEBÉ-659A-ROSA')
    producto_anda_verde, created = TProductos.objects.get_or_create(sku='ANDA-BEBÉ-659A-VERDE')
    
    ## Andadera Ottopedica NUBE 
    producto_anda_orto_gris, created = TProductos.objects.get_or_create(sku='ANDA-ORTO-NB003-GRIS')
    producto_anda_orto_marino, created = TProductos.objects.get_or_create(sku='ANDA-ORTO-NB003-MARINO')
    producto_anda_orto_rojo, created = TProductos.objects.get_or_create(sku='ANDA-ORTO-NB003-ROJO')
        
    ## BATERIA DE COCINA
    producto_bateria, created = TProductos.objects.get_or_create(sku='JUEG-COCI-UT-001-NEGRO')
    
    ## Bicicletas de equilibrio
    producto_bici_equilibrio_rosa, created = TProductos.objects.get_or_create(sku='BICI-EQUI-YM-CB-1-ROSA')
    producto_bici_equilibrio_roja, created = TProductos.objects.get_or_create(sku='BICI-EQUI-YM-CB-1-ROJO')
    producto_bici_equilibrio_mora, created = TProductos.objects.get_or_create(sku='BICI-EQUI-YM-CB-1-MORADO')
    
    ## Bicicletas 
    producto_bici_rojo_2, created = TProductos.objects.get_or_create(sku='BICI-MONT-MOD-002-B-ROJO')
    producto_bici_rojo_3, created = TProductos.objects.get_or_create(sku='BICI-MONT-MOD-003-B-ROJO')
    producto_bici_azul, created = TProductos.objects.get_or_create(sku='BICI-MONT-MOD-003-B-AZUL')
    
    ## Camillas y sillas para masajes
    producto_camilla_gris, created = TProductos.objects.get_or_create(sku='CAMAMASAJEGRIS')
    
    ## Carritos de mandados
    producto_carri_compra_gris, created = TProductos.objects.get_or_create(sku='CARR-COMP-MOD-CC001-GRIS')
    producto_carri_compra_azul, created = TProductos.objects.get_or_create(sku='CARR-COMP-MOD-CC001-AZUL')
    
    ## Campanas, extractores y purificadores de cocina
    producto_campana, created = TProductos.objects.get_or_create(sku='CAMPABOT90CPLA027')
    
    ## Carriolas para bebés
    producto_carriola, created = TProductos.objects.get_or_create(sku='CARR-ACCE-YMBT7P-PANDA NEGRO')
    
    ## Centros de actividades y gimnasios para bebés
    producto_gym_bb_azul, created = TProductos.objects.get_or_create(sku='GIMBEBESPACAZU361')    
    producto_gym_bb_rosa, created = TProductos.objects.get_or_create(sku='GIMBEBUNICOROS363')    
    
    
    ## Cortinas y persianas manuales para interiores  
    producto_cortina_taupe, created = TProductos.objects.get_or_create(sku='CORT-BLAC-CORB-24-TAUPE')    
    producto_cortina_chocolate, created = TProductos.objects.get_or_create(sku='CORT-BLAC-CORB-24-CHOCOLATE')    
    producto_cortina_oxford, created = TProductos.objects.get_or_create(sku='CORT-BLAC-CORB-24-OXFORD')    
    producto_cortina_negro, created = TProductos.objects.get_or_create(sku='CORT-BLAC-CORB-24-NEGRO')    
    producto_cortina_beige, created = TProductos.objects.get_or_create(sku='CORT-BLAC-CORB-24-BEIGE')    
    producto_cortina_vino, created = TProductos.objects.get_or_create(sku='CORT-BLAC-CORB-24-VINO')    
   
    # 3. Creamos las competencias   
    dummy_competencia = [
        ## ANDADERAS BEBES MUSICALES VIGOREM
        {
            "nombre_producto": "Andadera Caminadera Musical Plegable KIDDOS Bebe Juguete Educativo Interactiva Segura Multifuncional Color Azul",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/andadera-caminadera-musical-plegable-kiddos-bebe-juguete-educativo-interactiva-segura-multifuncional-color-azul/p/MLM43982375#polycard_client=search_best-seller&tracking_id=d3efc8cb-5745-4e7a-bfdf-b92b7ed3568b&wid=MLM3480979894&sid=search",
            "productos_fk": producto_anda_azul,
            "marca_fk": marca_vigorem,
        },
        {
            "nombre_producto": "Andadera Caminadera Musical Plegable KIDDOS Bebe Juguete Educativo Interactiva Segura Multifuncional Color Azul",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/andadera-caminadera-musical-plegable-kiddos-bebe-juguete-educativo-interactiva-segura-multifuncional-color-azul/p/MLM43982375#polycard_client=search_best-seller&tracking_id=d3efc8cb-5745-4e7a-bfdf-b92b7ed3568b&wid=MLM3480979894&sid=search",
            "productos_fk": producto_anda_lila,
            "marca_fk": marca_vigorem,
        },
        {
            "nombre_producto": "Andadera Caminadera Musical Plegable KIDDOS Bebe Juguete Educativo Interactiva Segura Multifuncional Color Azul",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/andadera-caminadera-musical-plegable-kiddos-bebe-juguete-educativo-interactiva-segura-multifuncional-color-azul/p/MLM43982375#polycard_client=search_best-seller&tracking_id=d3efc8cb-5745-4e7a-bfdf-b92b7ed3568b&wid=MLM3480979894&sid=search",
            "productos_fk": producto_anda_rosa,
            "marca_fk": marca_vigorem,
        },
        {
            "nombre_producto": "Andadera Caminadera Musical Plegable KIDDOS Bebe Juguete Educativo Interactiva Segura Multifuncional Color Azul",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/andadera-caminadera-musical-plegable-kiddos-bebe-juguete-educativo-interactiva-segura-multifuncional-color-azul/p/MLM43982375#polycard_client=search_best-seller&tracking_id=d3efc8cb-5745-4e7a-bfdf-b92b7ed3568b&wid=MLM3480979894&sid=search",
            "productos_fk": producto_anda_verde,
            "marca_fk": marca_vigorem,
        },
        
        ## Andadera Ortopedica Medical
        {
            "nombre_producto": "Andadera Ortopedica Asiento Silla Adulto Andador Con Ruedas",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/andadera-ortopedica-asiento-silla-adulto-andador-con-ruedas/p/MLM27989307#polycard_client=search-nordic&search_layout=grid&position=5&type=product&tracking_id=1b2a352a-6d08-49e5-ac6e-35b514710d0b&wid=MLM2664700976&sid=search",
            "productos_fk": producto_anda_orto_rojo,
            "marca_fk": marca_FOUND,
        },
        {
            "nombre_producto": "Andadera Ortopedica Asiento Silla Adulto Con Ruedas Y Frenos FOUND HEALTH Aulto Mayor Todo Terreno",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/andadera-ortopedica-asiento-silla-adulto-con-ruedas-y-frenos-found-health-aulto-mayor-todo-terreno/p/MLM28491368?product_trigger_id=MLM27989307&picker=true&quantity=1",
            "productos_fk": producto_anda_orto_gris,
            "marca_fk": marca_FOUND,
        },
        {
            "nombre_producto": "Andaderas Para Adultos Con Asiento Ortopedicas Ancianos",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://articulo.mercadolibre.com.mx/MLM-2030789151-andaderas-para-adultos-con-asiento-ortopedicas-ancianos-_JM#polycard_client=recommendations_pdp-pads-up&reco_backend=recomm_platform_base_merge_pads_rfa&reco_model=search_recos_backend_merge&reco_client=pdp-pads-up&reco_item_pos=5&reco_backend_type=low_level&reco_id=8836ded9-aeb0-4efe-acd8-cd712aebd0da&is_advertising=true&ad_domain=PDPDESKTOP_UP&ad_position=6&ad_click_id=ZWNkMDM3NWQtMzY4MS00OThiLWJjMTgtZjgxMGYxMGM4ZTc1",
            "productos_fk": producto_anda_orto_marino,
            "marca_fk": marca_FOUND,
        },
        
        ## BATERIA DE COCINA
        {
            "nombre_producto": "Batería De Cocina Orfeld 18 Piezas De Aluminio Con Antiadherente Set De Utensilios Cocina Color Negro",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/bateria-de-cocina-orfeld-18-piezas-de-aluminio-con-antiadherente-set-de-utensilios-cocina-color-negro/p/MLM42114095#polycard_client=search_best-seller-categories&tracking_id=d6e2ed0d-d02c-4f92-b9c1-8aea68f7e652&wid=MLM3501861906&sid=search",
            "productos_fk": producto_bateria,
            "marca_fk": marca_bateria,
        },
        ## Bicicletas de equilibrio
        {
            "nombre_producto": "Batería De Cocina Orfeld 18 Piezas De Aluminio Con Antiadherente Set De Utensilios Cocina Color Negro",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/bateria-de-cocina-orfeld-18-piezas-de-aluminio-con-antiadherente-set-de-utensilios-cocina-color-negro/p/MLM42114095#polycard_client=search_best-seller-categories&tracking_id=d6e2ed0d-d02c-4f92-b9c1-8aea68f7e652&wid=MLM3501861906&sid=search",
            "productos_fk": producto_bici_equilibrio_rosa,
            "marca_fk": marca_bici_equi,
        },
        {
            "nombre_producto": "Batería De Cocina Orfeld 18 Piezas De Aluminio Con Antiadherente Set De Utensilios Cocina Color Negro",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/bateria-de-cocina-orfeld-18-piezas-de-aluminio-con-antiadherente-set-de-utensilios-cocina-color-negro/p/MLM42114095#polycard_client=search_best-seller-categories&tracking_id=d6e2ed0d-d02c-4f92-b9c1-8aea68f7e652&wid=MLM3501861906&sid=search",
            "productos_fk": producto_bici_equilibrio_roja,
            "marca_fk": marca_bici_equi,
        },
        {
            "nombre_producto": "Batería De Cocina Orfeld 18 Piezas De Aluminio Con Antiadherente Set De Utensilios Cocina Color Negro",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/bateria-de-cocina-orfeld-18-piezas-de-aluminio-con-antiadherente-set-de-utensilios-cocina-color-negro/p/MLM42114095#polycard_client=search_best-seller-categories&tracking_id=d6e2ed0d-d02c-4f92-b9c1-8aea68f7e652&wid=MLM3501861906&sid=search",
            "productos_fk": producto_bici_equilibrio_mora,
            "marca_fk": marca_bici_equi,
        },
        ## Bicicletas 
        {
            "nombre_producto": "Bicicleta De Montaña Tourney Rodada 26 Freno De Disco 21 Velocidades Color Negro Rojo Bluelander",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/bicicleta-de-montana-tourney-rodada-26-freno-de-disco-21-velocidades-color-negro-rojo-bluelander/p/MLM24703330#polycard_client=recommendations_vip-v2p&reco_backend=ranker_retrieval_online_vpp_v2p&reco_model=rk_online_v4_retsys_vpp_v2p%2C+coldstart_high_exposition%2C+coldstart_low_exposition&reco_client=vip-v2p&reco_item_pos=0&reco_backend_type=low_level&reco_id=15bcc60f-d0fe-4caa-b7d6-a633c54bd15a&wid=MLM2383354634&sid=recos",
            "productos_fk": producto_bici_rojo_2,
            "marca_fk": marca_bicicletas,
        },        
        {
            "nombre_producto": "Bicicleta De Montaña Tourney Rodada 26 Freno De Disco 21 Velocidades Color Negro Rojo Bluelander",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/bicicleta-de-montana-tourney-rodada-26-freno-de-disco-21-velocidades-color-negro-rojo-bluelander/p/MLM24703330#polycard_client=recommendations_vip-v2p&reco_backend=ranker_retrieval_online_vpp_v2p&reco_model=rk_online_v4_retsys_vpp_v2p%2C+coldstart_high_exposition%2C+coldstart_low_exposition&reco_client=vip-v2p&reco_item_pos=0&reco_backend_type=low_level&reco_id=15bcc60f-d0fe-4caa-b7d6-a633c54bd15a&wid=MLM2383354634&sid=recos",
            "productos_fk": producto_bici_azul,
            "marca_fk": marca_bicicletas,
        },        
        {
            "nombre_producto": "Bicicleta Benotto Montaña Blackcomb R29 Unisex Negro/rojo Unica",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/bicicleta-benotto-montana-blackcomb-r29-unisex-negrorojo-unica/p/MLM28337735#polycard_client=recommendations_pdp-v2p&reco_backend=ranker_retrieval_online_vpp_v2p&reco_model=coldstart_high_exposition%2C+rk_online_v4_retsys_vpp_v2p%2C+coldstart_low_exposition&reco_client=pdp-v2p&reco_item_pos=0&reco_backend_type=low_level&reco_id=29a37c4e-f2cb-49ca-8d15-edef8f16f8a7&wid=MLM2017647741&sid=recos",
            "productos_fk": producto_bici_rojo_3,
            "marca_fk": marca_bicicletas_B,
        }, 
        ## Camillas y sillas para masajes
        {
            "nombre_producto": "Cama De Masajes, Spa, Tatuajes, Terapia Física, Pleg. 60cm",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://articulo.mercadolibre.com.mx/MLM-1491275680-cama-de-masajes-spa-tatuajes-terapia-fisica-pleg-60cm-_JM?searchVariation=175137737806#polycard_client=recommendations_vip-v2p&reco_backend=ranker_retrieval_online_vpp_v2p&reco_model=coldstart_high_exposition%2C+rk_online_v4_retsys_vpp_v2p%2C+coldstart_low_exposition&reco_client=vip-v2p&reco_item_pos=0&reco_backend_type=low_level&reco_id=1509e569-15ef-4a11-805c-a6fabdf526fe",
            "productos_fk": producto_camilla_gris,
            "marca_fk": marca_camilla_masajes,
        },         
        ## Carritos de mandados
        {
            "nombre_producto": "Cama De Masajes, Spa, Tatuajes, Terapia Física, Pleg. 60cm",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/carrito-para-mandados-compras-plegable-multiusos-resistente/p/MLM23953221#polycard_client=search_best-seller&tracking_id=e9d07f34-213b-4344-a61e-b8b5c607ba91&wid=MLM2278067932&sid=search",
            "productos_fk": producto_carri_compra_gris,
            "marca_fk": marca_carrito_compras,
        },         
        {
            "nombre_producto": "Cama De Masajes, Spa, Tatuajes, Terapia Física, Pleg. 60cm",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/carrito-para-mandados-compras-plegable-multiusos-resistente/p/MLM23953221#polycard_client=search_best-seller&tracking_id=e9d07f34-213b-4344-a61e-b8b5c607ba91&wid=MLM2278067932&sid=search",
            "productos_fk": producto_carri_compra_azul,
            "marca_fk": marca_carrito_compras,
        }, 
        ## Campanas, extractores y purificadores de cocina
        {
            "nombre_producto": "Campana De Isla Kutchen Kci90890 90 Cm Cristal Curvon Inox. Color Gris",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/campana-de-isla-kutchen-kci90890-90-cm-cristal-curvon-inox-color-gris/p/MLM49567136?pdp_filters=item_id:MLM2307916297#is_advertising=true&searchVariation=MLM49567136&backend_model=search-backend&position=7&search_layout=stack&type=pad&tracking_id=1fd1985f-52d5-4801-a299-d443ad98e45e&ad_domain=VQCATCORE_LST&ad_position=7&ad_click_id=ODE2NzU3M2EtNmQ3ZS00YmQxLWE3ZDUtYzBjZDAxMTE3OTBk",
            "productos_fk": producto_campana,
            "marca_fk": marca_campana,
        },                
        ## Campanas, extractores y purificadores de cocina
        {
            "nombre_producto": "Carriola Para Bebé De Bastón Trendy Kids Zoo Max Reclinable Color Rosa",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/carriola-para-bebe-de-baston-trendy-kids-zoo-max-reclinable-color-rosa/p/MLM28444322#polycard_client=search_best-seller&tracking_id=357ce74a-88e1-427e-8ccc-5dbbe6c46bae&wid=MLM3871226390&sid=search",
            "productos_fk": producto_carriola,
            "marca_fk": marca_carriola,
        },                
        ## Centros de actividades y gimnasios para bebés
        {
            "nombre_producto": "Gimnasio Para Bebe KIDDOS Tapete Interactivo Didáctico Con 30 Pelotas Incluidas Personajes Marinos Tortuga Para Actividades Ayuda Con Desarrollo Cognitivo Y Sensorial",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/gimnasio-para-bebe-kiddos-tapete-interactivo-didactico-con-30-pelotas-incluidas-personajes-marinos-tortuga-para-actividades-ayuda-con-desarrollo-cognitivo-y-sensorial/p/MLM45798371?has_official_store=false&highlight=true&headerTopBrand=true#polycard_client=search-nordic&search_layout=grid&position=50&type=product&tracking_id=80d7de71-a7a6-4b33-8b21-c2b5ae602e2d&wid=MLM2229237639&sid=search",
            "productos_fk": producto_gym_bb_azul,
            "marca_fk": marca_vigorem,
        },                
        {
            "nombre_producto": "Gimnasio Para Bebe KIDDOS Tapete Interactivo Didáctico Con 30 Pelotas Incluidas Personajes Marinos Tortuga Para Actividades Ayuda Con Desarrollo Cognitivo Y Sensorial",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/gimnasio-para-bebe-kiddos-tapete-interactivo-didactico-con-30-pelotas-incluidas-personajes-marinos-tortuga-para-actividades-ayuda-con-desarrollo-cognitivo-y-sensorial/p/MLM45798371?has_official_store=false&highlight=true&headerTopBrand=true#polycard_client=search-nordic&search_layout=grid&position=50&type=product&tracking_id=80d7de71-a7a6-4b33-8b21-c2b5ae602e2d&wid=MLM2229237639&sid=search",
            "productos_fk": producto_gym_bb_rosa,
            "marca_fk": marca_vigorem,
        },                
        ## Cortinas y persianas manuales para interiores  
        {
            "nombre_producto": "Gimnasio Para Bebe KIDDOS Tapete Interactivo Didáctico Con 30 Pelotas Incluidas Personajes Marinos Tortuga Para Actividades Ayuda Con Desarrollo Cognitivo Y Sensorial",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/cortinas-blackout-nanwei-para-ventanassala-recamara2-paneles-270x215cmaislamiento-termico-y-reduccion-de-ruido-tela-impermeable/p/MLM28013035?pdp_filters=item_id:MLM1998763275#is_advertising=true&searchVariation=MLM28013035&backend_model=search-backend&position=3&search_layout=grid&type=pad&tracking_id=725c8ced-6122-43e3-9b9e-de65d5d0231d&ad_domain=VQCATCORE_LST&ad_position=3&ad_click_id=NDg2ZWY1ZjYtODRkNy00N2NmLWFjMzktMGViOGM1NDk5ZmQ0",
            "productos_fk": producto_cortina_vino,
            "marca_fk": marca_easytao,
        },                
        {
            "nombre_producto": "Gimnasio Para Bebe KIDDOS Tapete Interactivo Didáctico Con 30 Pelotas Incluidas Personajes Marinos Tortuga Para Actividades Ayuda Con Desarrollo Cognitivo Y Sensorial",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/cortinas-blackout-nanwei-para-ventanassala-recamara2-paneles-270x215cmaislamiento-termico-y-reduccion-de-ruido-tela-impermeable/p/MLM28013035?pdp_filters=item_id:MLM1998763275#is_advertising=true&searchVariation=MLM28013035&backend_model=search-backend&position=3&search_layout=grid&type=pad&tracking_id=725c8ced-6122-43e3-9b9e-de65d5d0231d&ad_domain=VQCATCORE_LST&ad_position=3&ad_click_id=NDg2ZWY1ZjYtODRkNy00N2NmLWFjMzktMGViOGM1NDk5ZmQ0",
            "productos_fk": producto_cortina_beige,
            "marca_fk": marca_easytao,
        },                
        {
            "nombre_producto": "Gimnasio Para Bebe KIDDOS Tapete Interactivo Didáctico Con 30 Pelotas Incluidas Personajes Marinos Tortuga Para Actividades Ayuda Con Desarrollo Cognitivo Y Sensorial",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/cortinas-blackout-nanwei-para-ventanassala-recamara2-paneles-270x215cmaislamiento-termico-y-reduccion-de-ruido-tela-impermeable/p/MLM28013035?pdp_filters=item_id:MLM1998763275#is_advertising=true&searchVariation=MLM28013035&backend_model=search-backend&position=3&search_layout=grid&type=pad&tracking_id=725c8ced-6122-43e3-9b9e-de65d5d0231d&ad_domain=VQCATCORE_LST&ad_position=3&ad_click_id=NDg2ZWY1ZjYtODRkNy00N2NmLWFjMzktMGViOGM1NDk5ZmQ0",
            "productos_fk": producto_cortina_negro,
            "marca_fk": marca_easytao,
        },                
        {
            "nombre_producto": "Gimnasio Para Bebe KIDDOS Tapete Interactivo Didáctico Con 30 Pelotas Incluidas Personajes Marinos Tortuga Para Actividades Ayuda Con Desarrollo Cognitivo Y Sensorial",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/cortinas-blackout-nanwei-para-ventanassala-recamara2-paneles-270x215cmaislamiento-termico-y-reduccion-de-ruido-tela-impermeable/p/MLM28013035?pdp_filters=item_id:MLM1998763275#is_advertising=true&searchVariation=MLM28013035&backend_model=search-backend&position=3&search_layout=grid&type=pad&tracking_id=725c8ced-6122-43e3-9b9e-de65d5d0231d&ad_domain=VQCATCORE_LST&ad_position=3&ad_click_id=NDg2ZWY1ZjYtODRkNy00N2NmLWFjMzktMGViOGM1NDk5ZmQ0",
            "productos_fk": producto_cortina_oxford,
            "marca_fk": marca_easytao,
        },                
        {
            "nombre_producto": "Gimnasio Para Bebe KIDDOS Tapete Interactivo Didáctico Con 30 Pelotas Incluidas Personajes Marinos Tortuga Para Actividades Ayuda Con Desarrollo Cognitivo Y Sensorial",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/cortinas-blackout-nanwei-para-ventanassala-recamara2-paneles-270x215cmaislamiento-termico-y-reduccion-de-ruido-tela-impermeable/p/MLM28013035?pdp_filters=item_id:MLM1998763275#is_advertising=true&searchVariation=MLM28013035&backend_model=search-backend&position=3&search_layout=grid&type=pad&tracking_id=725c8ced-6122-43e3-9b9e-de65d5d0231d&ad_domain=VQCATCORE_LST&ad_position=3&ad_click_id=NDg2ZWY1ZjYtODRkNy00N2NmLWFjMzktMGViOGM1NDk5ZmQ0",
            "productos_fk": producto_cortina_chocolate,
            "marca_fk": marca_easytao,
        },                
        {
            "nombre_producto": "Gimnasio Para Bebe KIDDOS Tapete Interactivo Didáctico Con 30 Pelotas Incluidas Personajes Marinos Tortuga Para Actividades Ayuda Con Desarrollo Cognitivo Y Sensorial",
            "precio": 0,
            "precio_tachado": 0,
            "url": "https://www.mercadolibre.com.mx/cortinas-blackout-nanwei-para-ventanassala-recamara2-paneles-270x215cmaislamiento-termico-y-reduccion-de-ruido-tela-impermeable/p/MLM28013035?pdp_filters=item_id:MLM1998763275#is_advertising=true&searchVariation=MLM28013035&backend_model=search-backend&position=3&search_layout=grid&type=pad&tracking_id=725c8ced-6122-43e3-9b9e-de65d5d0231d&ad_domain=VQCATCORE_LST&ad_position=3&ad_click_id=NDg2ZWY1ZjYtODRkNy00N2NmLWFjMzktMGViOGM1NDk5ZmQ0",
            "productos_fk": producto_cortina_taupe,
            "marca_fk": marca_easytao,
        },                
               
               
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
