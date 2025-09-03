from django.urls import path
from . import views  # Importar las vistas

urlpatterns = [
    path("dashboard", views.dashboard_view, name="venta_dashboard"),
    path('upload', views.subir_ventas, name='subir_ventas'),
    path('upload-csv', views.cargar_csv_ventas, name='cargar_csv_ventas'),
    path('mapa-calor', views.mapa_calor, name='mapa_calor'),
]