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
