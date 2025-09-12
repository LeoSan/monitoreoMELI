import pandas as pd
import os
from datetime import datetime
import logging
import re
import os


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException # Importar la excepción de Timeout


from dotenv import load_dotenv

from .models import TVentas, TProductoCompetencias

# Configuracions
load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def leer_csv_ventas(ruta_archivo, mapeo_columnas=None):
    """
    Paso 1: Lee el archivo CSV de ventas y retorna un DataFrame con mapeo de columnas
    
    Args:
        ruta_archivo (str): Ruta al archivo CSV
        mapeo_columnas (dict): Diccionario que mapea columnas CSV a campos del modelo
    
    Returns:
        tuple: (pandas.DataFrame, dict) - DataFrame con los datos y columnas mapeadas
    """
    
    # Mapeo por defecto de columnas CSV a campos del modelo TVentas
    if mapeo_columnas is None:
        mapeo_columnas = {
            'MARCA': 'marca',
            '# de venta': 'venta_id', 
            'Fecha de venta': 'fecha_venta',
            'SKU': 'sku',
            '# de publicacion': 'publicacion_mlm_id',
            'titulo de la publicación': 'titulo',
            'Precio unitario de venta de la publicación (MXN)': 'precio_unitario',
            'Unidades': 'unidades',
            'Total (MXN)': 'total'
        }
    
    # Verificar que el archivo existe
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"El archivo {ruta_archivo} no existe")
    
    try:
        # Leer el CSV con separador punto y coma
        df = pd.read_csv(
            ruta_archivo,
            encoding='utf-8',
            sep=';',
            na_values=['', 'NA', 'N/A', 'null', 'NULL'],
            dtype=str  # Leer todo como string inicialmente
        )
        
        logger.info(f"Archivo CSV leído exitosamente: {len(df)} filas")
        
        # Limpiar nombres de columnas (remover espacios extra)
        df.columns = df.columns.str.strip()
        
        # Verificar qué columnas del mapeo existen en el CSV
        columnas_existentes = {}
        columnas_faltantes = []
        
        for col_csv, col_modelo in mapeo_columnas.items():
            if col_csv in df.columns:
                columnas_existentes[col_csv] = col_modelo
            else:
                columnas_faltantes.append(col_csv)
        
        if columnas_faltantes:
            logger.warning(f"Columnas no encontradas en el CSV: {columnas_faltantes}")
        
        logger.info(f"Columnas mapeadas: {list(columnas_existentes.values())}")
        
        return df, columnas_existentes
        
    except Exception as e:
        logger.error(f"Error al leer el archivo CSV: {str(e)}")
        raise

def parsear_fecha_venta(fecha_str):
    """
    Convierte fecha del formato '27 de agosto de 2025 23:56 hs.' a datetime
    
    Args:
        fecha_str (str): Fecha en formato español del CSV
        
    Returns:
        datetime: Objeto datetime parseado o None si hay error
    """
    if pd.isna(fecha_str) or fecha_str == '' or fecha_str is None:
        return None
        
    try:
        # Remover 'hs.' del final
        fecha_clean = str(fecha_str).replace(' hs.', '').strip()
        
        # Diccionario de meses en español
        meses = {
            'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4,
            'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
            'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
        }
        
        # Patrón para capturar: día de mes de año hora:minuto
        patron = r'(\d{1,2}) de (\w+) de (\d{4}) (\d{1,2}):(\d{2})'
        match = re.match(patron, fecha_clean)
        
        if match:
            dia, mes_nombre, año, hora, minuto = match.groups()
            mes_numero = meses.get(mes_nombre.lower())
            
            if mes_numero:
                return datetime(
                    year=int(año),
                    month=mes_numero,
                    day=int(dia),
                    hour=int(hora),
                    minute=int(minuto)
                )
        
        logger.warning(f"No se pudo parsear la fecha: {fecha_str}")
        return None
        
    except Exception as e:
        logger.error(f"Error parseando fecha '{fecha_str}': {str(e)}")
        return None

def validar_datos_ventas(df, columnas_mapeadas):
    """
    Paso 2: Valida los datos del DataFrame antes de cargar a la BD
    
    Args:
        df (pandas.DataFrame): DataFrame con los datos del CSV
        columnas_mapeadas (dict): Diccionario de columnas mapeadas
        
    Returns:
        tuple: (pandas.DataFrame, list) - DataFrame limpio y lista de errores
    """
    
    errores = []
    df_limpio = df.copy()
    
    logger.info("Iniciando validación de datos...")
    
    # Crear DataFrame solo con las columnas que necesitamos
    columnas_csv = list(columnas_mapeadas.keys())
    df_filtrado = df_limpio[columnas_csv].copy()
    
    # Renombrar columnas según el mapeo
    df_filtrado.rename(columns=columnas_mapeadas, inplace=True)
    
    total_filas = len(df_filtrado)
    filas_validas = 0
    
    for index, row in df_filtrado.iterrows():
        fila_errores = []
        
        # Validar campos obligatorios
        campos_obligatorios = ['marca', 'sku', 'titulo', 'unidades', 'total']
        for campo in campos_obligatorios:
            if campo in row and (pd.isna(row[campo]) or str(row[campo]).strip() == ''):
                fila_errores.append(f"Campo obligatorio '{campo}' vacío")
        
        # Validar fecha_venta
        if 'fecha_venta' in row:
            fecha_parseada = parsear_fecha_venta(row['fecha_venta'])
            if fecha_parseada is None and not pd.isna(row['fecha_venta']):
                fila_errores.append(f"Fecha inválida: {row['fecha_venta']}")
            else:
                df_filtrado.at[index, 'fecha_venta'] = fecha_parseada
        
        # Validar campos numéricos
        campos_numericos = ['venta_id', 'unidades', 'precio_unitario', 'total']
        for campo in campos_numericos:
            if campo in row and not pd.isna(row[campo]):
                try:
                    if campo == 'venta_id' or campo == 'unidades':
                        # Campos enteros
                        valor = int(float(str(row[campo])))
                        df_filtrado.at[index, campo] = valor
                    else:
                        # Campos float (precios)
                        valor = float(str(row[campo]))
                        df_filtrado.at[index, campo] = valor
                        
                    # Validar rangos
                    if campo in ['unidades'] and valor <= 0:
                        fila_errores.append(f"'{campo}' debe ser mayor a 0: {valor}")
                        
                except (ValueError, TypeError):
                    fila_errores.append(f"'{campo}' no es un número válido: {row[campo]}")
        
        # Validar longitud de campos de texto
        campos_texto = {
            'publicacion_mlm_id': 255,
            'sku': 255,
            'marca': 255
        }
        
        for campo, max_length in campos_texto.items():
            if campo in row and not pd.isna(row[campo]):
                if len(str(row[campo])) > max_length:
                    fila_errores.append(f"'{campo}' excede {max_length} caracteres")
        
        # Si hay errores en esta fila, registrarlos
        if fila_errores:
            errores.append({
                'fila': index + 2,  # +2 porque pandas index empieza en 0 y CSV tiene header
                'errores': fila_errores,
                'datos': row.to_dict()
            })
        else:
            filas_validas += 1
    
    logger.info(f"Validación completada: {filas_validas}/{total_filas} filas válidas")
    
    if errores:
        logger.warning(f"Se encontraron {len(errores)} filas con errores")
        
    return df_filtrado, errores

def cargar_ventas_bd(df_validado, mostrar_progreso=True):
    """
    Paso 3: Carga los datos validados a la base de datos
    
    Args:
        df_validado (pandas.DataFrame): DataFrame con datos validados
        mostrar_progreso (bool): Si mostrar progreso de la carga
        
    Returns:
        dict: Resultado de la carga (exitosos, errores, etc.)
    """
    
    logger.info("Iniciando carga a base de datos...")
    
    resultado = {
        'total_filas': len(df_validado),
        'exitosos': 0,
        'errores': 0,
        'errores_detalle': []
    }
    
    print(df_validado)
        
    for index, row in df_validado.iterrows():
        try:
            # Crear instancia del modelo TVentas
            venta = TVentas()
            
            # Asignar campos del modelo
            if 'publicacion_mlm_id' in row and not pd.isna(row['publicacion_mlm_id']):
                venta.publicacion_mlm_id = str(row['publicacion_mlm_id'])
            
            if 'venta_id' in row and not pd.isna(row['venta_id']):
                venta.venta_id = int(row['venta_id'])
            
            if 'titulo' in row and not pd.isna(row['titulo']):
                venta.titulo = str(row['titulo'])
            
            if 'sku' in row and not pd.isna(row['sku']):
                venta.sku = str(row['sku'])
            
            if 'fecha_venta' in row and row['fecha_venta'] is not None:
                venta.fecha_venta = row['fecha_venta']
            
            if 'marca' in row and not pd.isna(row['marca']):
                venta.marca = str(row['marca'])
            
            if 'precio_unitario' in row and not pd.isna(row['precio_unitario']):
                venta.precio_unitario = float(row['precio_unitario'])
            
            if 'unidades' in row and not pd.isna(row['unidades']):
                venta.unidades = int(row['unidades'])
            
            if 'total' in row and not pd.isna(row['total']):
                venta.total = float(row['total'])
            
            # Validar el modelo antes de guardar
            venta.full_clean()
            
            # Guardar en la base de datos
            venta.save()
            
            resultado['exitosos'] += 1
            
            if mostrar_progreso and (resultado['exitosos'] % 100 == 0):
                logger.info(f"Procesadas {resultado['exitosos']} filas...")
                
        except Exception as e:
            resultado['errores'] += 1
            error_detalle = {
                'fila': index + 2,
                'error': str(e),
                'datos': row.to_dict()
            }
            resultado['errores_detalle'].append(error_detalle)
            logger.error(f"Error en fila {index + 2}: {str(e)}")
    
    #logger.info(f"Carga completada: {resultado['exitosos']} exitosos, {resultado['errores']} errores")
    
    return resultado

def procesar_csv_ventas_completo(ruta_archivo, mapeo_columnas=None, mostrar_progreso=True):
    """
    Función principal que ejecuta todo el proceso: leer, validar y cargar
    
    Args:
        ruta_archivo (str): Ruta al archivo CSV
        mapeo_columnas (dict): Mapeo personalizado de columnas (opcional)
        mostrar_progreso (bool): Si mostrar progreso
        
    Returns:
        dict: Resultado completo del proceso
    """
    
    try:
        logger.info(f"=== INICIANDO PROCESAMIENTO DE {ruta_archivo} ===")
        
        # Paso 1: Leer CSV
        df, columnas_mapeadas = leer_csv_ventas(ruta_archivo, mapeo_columnas)
        
        # Paso 2: Validar datos
        df_validado, errores_validacion = validar_datos_ventas(df, columnas_mapeadas)
        
        if errores_validacion:
            logger.warning("Se encontraron errores de validación. Revisar antes de continuar.")
            # Puedes decidir si continuar o no con las filas válidas
        
        # Paso 3: Cargar a BD (solo filas sin errores)
        df_sin_errores = df_validado.drop([e['fila']-2 for e in errores_validacion], errors='ignore')
        resultado_carga = cargar_ventas_bd(df_sin_errores, mostrar_progreso)
        
        resultado_final = {
            'archivo': ruta_archivo,
            'filas_leidas': len(df),
            'columnas_mapeadas': list(columnas_mapeadas.values()),
            'errores_validacion': errores_validacion,
            'resultado_carga': resultado_carga,
            'exito': resultado_carga['errores'] == 0 and len(errores_validacion) == 0
        }
        
        logger.info("=== PROCESAMIENTO COMPLETADO ===")
        return resultado_final
        
    except Exception as e:
        logger.error(f"Error general en procesamiento: {str(e)}")
        raise

def iniciar_driver():
    """Inicializa y configura el driver de Selenium."""
    logger.info("Inicializando el WebDriver de Chrome...")
    opts = Options()
    # Todas tus opciones están perfectas, no las cambies
    opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.7258.115 Safari/537.36")
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1920,1080")

    # --- CAMBIO PRINCIPAL ---
    # Ya no usamos ChromeDriverManager. Selenium encontrará automáticamente
    # el chromedriver que instalamos con "apk" en el Dockerfile.
    try:
        driver = webdriver.Chrome(options=opts)
        logger.info("WebDriver inicializado correctamente.")
        return driver
    except Exception as e:
        logger.error(f"Error al inicializar el driver: {e}")
        return None
    
def generarScrapingPorProducto(url:str):
    """
    Función de validación para confirmar que el elemento es encontrado.
    """
    precio_final = 0.0
    precio_original = 0.0
    driver = None
    
    try:
        driver = iniciar_driver()
        if not driver:
            raise Exception("El WebDriver no se pudo inicializar.")

        driver.get(url)
        wait = WebDriverWait(driver, 15)
        
       # ---> Bloque para extraer el PRECIO oferta
        try:
            #logger.info("Buscando el elemento <meta> con itemprop='price'...")
            precio_element = wait.until(
                EC.presence_of_element_located((
                    By.XPATH, 
                    '//meta[@itemprop="price"]'
                ))
            )
            
            # Si el código llega aquí, ¡el elemento fue encontrado!
            logger.info("¡ÉXITO! El elemento fue encontrado.")
            
            # Ahora vamos a inspeccionar lo que encontramos para validarlo
            tag_name = precio_element.tag_name
            content_value = precio_element.get_attribute('content')
            
           # logger.info(f"   -> Tipo de etiqueta: {tag_name}")
           # logger.info(f"   -> Valor del atributo 'content': {content_value}")
            
            # Intentamos la conversión para ver si el valor es numérico
            precio_final = float(content_value)
            #logger.info(f"   -> Conversión a número exitosa: {precio_final}")

        except TimeoutException:
            # Si después de 15 segundos no lo encuentra, el código entrará aquí
            logger.error("VALIDACIÓN FALLIDA: El elemento con XPath '//meta[@itemprop=\"price\"]' NO FUE ENCONTRADO en la página.")
        
        # ---> Bloque para extraer el PRECIO ORIGINAL
        try:
            logger.info("Buscando el precio original (tachado)...")
            precio_original_element = wait.until(
                EC.presence_of_element_located((
                    By.XPATH,
                    # Usamos el XPath específico que construimos
                    "//s[contains(@class, 'ui-pdp-price__original-value')]//span[@class='andes-money-amount__fraction']"
                ))
            )
            # Obtenemos el texto del elemento y lo convertimos a número
            precio_original_texto = precio_original_element.text
            precio_original = float(precio_original_texto.replace(',', '')) # Se añade replace por si hay miles
            #logger.info(f"ÉXITO: Precio original encontrado: {precio_original}")

        except TimeoutException:
            # Esto es normal si el producto no tiene descuento. No es un error crítico.
            logger.warning("AVISO: No se encontró un precio original. Es posible que el producto no tenga descuento.")
            precio_original = 0.0 # O puedes asignarle el mismo valor que precio_final

        # ---> Añadimos el nuevo dato al resultado        
        resultado_final = {
            'precio': precio_final,
            'precio_original': precio_original,
            'error': None
        }

    except Exception as e:
        logger.error(f"Error durante el proceso de validación: {str(e)}")
        resultado_final = {
            'precio': precio_final,
            'precio_original': precio_original,
            'error': str(e)
        }
    finally:
        if driver:
            driver.quit()
            logger.info("=== VALIDACIÓN COMPLETADA (DRIVER CERRADO) ===")

    return resultado_final

def updatePrecioCompetencia(producto_filtro):
    # Lista de Competencias 
    competencia_para_scrapear = TProductoCompetencias.objects.obtener_por_producto(producto_filtro)
    
    for comp in competencia_para_scrapear:
        # Obtenemos el nuevo precio desde el scraping
        list_competencia_scraping = generarScrapingPorProducto(comp['url'])
        # Actualizamos el registro en la base de datos
        TProductoCompetencias.objects.filter(id=comp['id']).update(precio=list_competencia_scraping['precio'], precio_tachado=list_competencia_scraping['precio_original'])
        if list_competencia_scraping['error'] != None:
            logger.error(f"Error En el ScrapinG {comp['id']}: {list_competencia_scraping['error']}")
            
    # Volvemos a llamar a nuestro método para obtener los datos ya actualizados
    competencia_actualizada = TProductoCompetencias.objects.obtener_por_producto(producto_filtro)
    resultado =  {'lista':competencia_actualizada,'error': list_competencia_scraping['error']}
    return resultado