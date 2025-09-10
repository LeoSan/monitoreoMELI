import os
import tempfile
import logging

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.conf import settings

from venta.models import TVentas, TProductos, TProductoCompetencia, TMarca

# Propios 
from .forms import CSVUploadForm
from .utils import procesar_csv_ventas_completo, updatePrecioCompetencia

logger = logging.getLogger(__name__)

@login_required
def dashboard_view(request):
    context = {
        'user': 'Leonard',
        'total_ventas': 1250,
        'productos_activos': 45,
        'ingresos_mes': 25000.50
    }    
    return render(request, 'venta/index.html')

@login_required
def subir_ventas(request):
    if request.method == 'POST' and request.FILES['archivo_csv']:
        archivo_subido = request.FILES['archivo_csv']

        # Guardar el archivo temporalmente
        fs = FileSystemStorage()
        nombre_archivo = fs.save(archivo_subido.name, archivo_subido)
        ruta_archivo = os.path.join(settings.MEDIA_ROOT, nombre_archivo)

        try:
            # Procesar el archivo con tu función
            mapeo_columnas = {
                    'MARCA': 'marca',
                    '# de venta': 'venta_id', 
                    'Fecha de venta': 'fecha_venta',
                    'SKU': 'sku',
                    '# de publicacion': 'publicacion_mlm_id',
                    'Titulo de la publicacion': 'titulo',
                    'Precio unitario de venta de la publicacion (MXN)': 'precio_unitario',
                    'Unidades': 'unidades',
                    'Total (MXN)': 'total'
            }
            resultado = procesar_csv_ventas_completo(ruta_archivo, mapeo_columnas)

            # Usar mensajes de Django para mostrar el resultado
            if resultado['exito']:
                messages.success(request, f"Procesamiento exitoso. Filas cargadas: {resultado['resultado_carga']['exitosos']}")
            else:
                messages.error(request, f"Procesamiento con errores. Filas exitosas: {resultado['resultado_carga']['exitosos']}, Filas con errores: {len(resultado['errores_validacion'])}")
                # Aquí puedes manejar los errores de validación y mostrarlos al usuario
                request.session['errores_detalle'] = resultado['errores_validacion']

        except Exception as e:
            messages.error(request, f"Ocurrió un error en el procesamiento: {str(e)}")

        finally:
            # Eliminar el archivo temporalmente
            if os.path.exists(ruta_archivo):
                os.remove(ruta_archivo)

    return render(request, 'venta/subir_ventas.html')

@login_required
def cargar_csv_ventas(request):
    """
    Vista para mostrar el formulario y procesar la carga de CSV
    """
    
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            archivo_csv = request.FILES['archivo_csv']
            
            try:
                # Crear archivo temporal
                with tempfile.NamedTemporaryFile(mode='wb', suffix='.csv', delete=False) as temp_file:
                    # Escribir contenido del archivo subido al temporal
                    for chunk in archivo_csv.chunks():
                        temp_file.write(chunk)
                    temp_file_path = temp_file.name
                
                logger.info(f"Procesando archivo CSV: {archivo_csv.name}")
                
                # Procesar el CSV usando utils.py
                mapeo_columnas = {
                        'MARCA': 'marca',
                        '# de venta': 'venta_id', 
                        'Fecha de venta': 'fecha_venta',
                        'SKU': 'sku',
                        '# de publicacion': 'publicacion_mlm_id',
                        'Titulo de la publicacion': 'titulo',
                        'Precio unitario de venta de la publicacion (MXN)': 'precio_unitario',
                        'Unidades': 'unidades',
                        'Total (MXN)': 'total'
                }                
                resultado = procesar_csv_ventas_completo(temp_file_path, mapeo_columnas, mostrar_progreso=True)
                
                # Limpiar archivo temporal
                os.unlink(temp_file_path)
                
                # Preparar mensaje de resultado
                if resultado['exito']:
                    messages.success(
                        request, 
                        f"✅ CSV procesado exitosamente! "
                        f"Se cargaron {resultado['resultado_carga']['exitosos']} registros."
                    )
                else:
                    messages.warning(
                        request,
                        f"⚠️ CSV procesado con advertencias. "
                        f"Exitosos: {resultado['resultado_carga']['exitosos']}, "
                        f"Errores: {resultado['resultado_carga']['errores'] + len(resultado['errores_validacion'])}"
                    )
                
                # Pasar resultado detallado al template
                context = {
                    'form': CSVUploadForm(),  # Nuevo formulario limpio
                    'resultado': resultado,
                    'mostrar_resultado': True
                }
                
                return render(request, 'venta/cargar_csv.html', context)
                
            except Exception as e:
                # Limpiar archivo temporal si existe
                if 'temp_file_path' in locals() and os.path.exists(temp_file_path):
                    os.unlink(temp_file_path)
                
                logger.error(f"Error procesando CSV: {str(e)}")
                messages.error(
                    request, 
                    f"❌ Error procesando el archivo: {str(e)}"
                )
        else:
            messages.error(request, "❌ Por favor corrige los errores en el formulario.")
    
    else:
        form = CSVUploadForm()
    
    context = {
        'form': form,
        'mostrar_resultado': False
    }
    
    return render(request, 'venta/cargar_csv.html', context)

def estado_carga_csv(request):
    """
    Vista AJAX para obtener estado de la carga (opcional para futuras mejoras)
    """
    # Esta función la podrías usar después para mostrar progreso en tiempo real
    return JsonResponse({'status': 'completed'})

@login_required
def mapa_calor(request):
    try:
        # Obtener parámetros de los tres filtros
        marca_filtro = request.GET.get('marca', '')
        producto_filtro = request.GET.get('producto', '')
        publicacion_filtro = request.GET.get('publicacion_mlm', '')
        
        # Obtener todas las opciones para los combobox
        
        # Productos disponibles (títulos únicos)
        productos_disponibles = TVentas.objects.values('titulo').distinct().order_by('titulo')
        
        # Publicaciones disponibles (IDs únicos)
        publicaciones_disponibles = TVentas.objects.values('publicacion_mlm_id').distinct().order_by('publicacion_mlm_id')
        
        # Construir la consulta base
        queryset = TVentas.objects.all()
        
        # Aplicar filtros según lo seleccionado
        if marca_filtro:
            queryset = queryset.filter(marca=marca_filtro)
            
        if producto_filtro:
            queryset = queryset.filter(titulo=producto_filtro)
            
        if publicacion_filtro:
            queryset = queryset.filter(publicacion_mlm_id=publicacion_filtro)
        
        # Si no hay ningún filtro, mostrar NUBE por defecto
        if not marca_filtro and not producto_filtro and not publicacion_filtro:
            queryset = queryset.filter(marca='NUBE')
            marca_filtro = 'NUBE'
        
        # Obtener productos únicos con los filtros aplicados
        productos_resultado = queryset.values(
            'titulo', 'publicacion_mlm_id'
        ).distinct().order_by('titulo')
        
        # Convertir a lista
        productos_lista = list(productos_resultado)
        
        context = {
            'productos': productos_lista,
            'total_productos': len(productos_lista),
            
            # Opciones para los combobox
            'productos_disponibles': productos_disponibles,
            'publicaciones_disponibles': publicaciones_disponibles,
            
            # Valores seleccionados para mantener estado
            'marca_seleccionada': marca_filtro,
            'producto_seleccionado': producto_filtro,
            'publicacion_seleccionada': publicacion_filtro,
        }
        
    except Exception as e:
        context = {
            'productos': [],
            'total_productos': 0,
            'productos_disponibles': [],
            'publicaciones_disponibles': [],
            'marca_seleccionada': '',
            'producto_seleccionado': '',
            'publicacion_seleccionada': '',
            'error': str(e)
        }
    
    return render(request, 'venta/mapa_calor.html', context)

@login_required
def obtenerAnalisisProducto(request):
    try:
        boton_scraping  = request.GET.get('scraping')
        marca_filtro    = request.GET.get('marca')
        producto_filtro = request.GET.get('producto')
        val_filtro_producto = None
        competencia = []
        
       # Obtener todas las opciones para los combobox
        marcas_disponibles = TMarca.objects.values('id', 'nombre').distinct().order_by('nombre')

        # Construir la consulta base
        query_set = TProductos.objects.all()
        
        # Aplicar filtros según lo seleccionado
        if marca_filtro and marca_filtro != '0' and marca_filtro != '[Seleccione]' and marca_filtro != 'None' and marca_filtro != '' :
            query_set = query_set.filter(marca_fk_id=marca_filtro)

        if producto_filtro and producto_filtro != '0' and producto_filtro != '[Seleccione]' and producto_filtro != 'None' and producto_filtro != '' :
            val_filtro_producto = True
            query_set = query_set.filter(id=producto_filtro)

        productos_disponibles = query_set.values(
            'id', 'nombre', 'sku', 'precio_techo'
        ).distinct().order_by('nombre')

        if boton_scraping == 'true' or val_filtro_producto is not None:
            logger.info(f"Ejecutando scraping para el producto ID: {producto_filtro}")
            competencia = updatePrecioCompetencia(producto_filtro)
            logger.info(f"Scraping completado. Registros obtenidos: {len(competencia)}")
            messages.success(
                request, 
                "✅ Scraping completado y precios actualizados exitosamente!"
            )
            
        context = {
            'combo_select_marcas': {'lista':list(marcas_disponibles),'marca_seleccionada': marca_filtro},
            'combo_productos': {'lista':list(productos_disponibles),'producto_seleccionado': producto_filtro},
            'competencia': {'lista':list(competencia),'producto_seleccionado': producto_filtro},
        }         
        
    except Exception as e:
        context = {
            'combo_select_marcas': {'lista':list(marcas_disponibles),'marca_seleccionada': marca_filtro},
            'combo_productos': {'lista':list(productos_disponibles),'producto_seleccionado': producto_filtro},
            'competencia': {'lista':list(competencia),'producto_seleccionado': producto_filtro},
            'error': str(e)
        }
        logger.error(f"Error en obtenerAnalisisProducto: {str(e)}")        
    return render(request, 'venta/check_producto.html', context)

@login_required
def generarCloudWord(request):
    return render(request, 'venta/cloud_word.html') 
