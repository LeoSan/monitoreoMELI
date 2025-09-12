from django.urls import path
from . import views  # Importar las vistas

app_name = 'ventas'

urlpatterns = [
    path("dashboard/", views.dashboard_view, name="venta_dashboard"),
    path('upload/', views.subir_ventas, name='subir_ventas'),
    path('upload-csv/', views.cargar_csv_ventas, name='cargar_csv_ventas'),
    path('mapa-calor/', views.mapa_calor, name='mapa_calor'),
    path('check-producto/', views.obtenerAnalisisProducto, name='check_producto'),
    path('check-list-competencia/', views.obtenerListadoAnalisisProductoCompetencia, name='check_list_producto_competencia'),
    path('cloud-word/', views.generarCloudWord, name='cloud_word'),
]