from django.contrib import admin
from .models import TVentas, TProductos, TCompetencia


@admin.register(TVentas)
class TVentasAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'sku', 'fecha_venta', 'marca', 'total']
    list_filter = ['marca', 'fecha_venta']
    search_fields = ['titulo', 'sku', 'publicacion_mlm_id']
    date_hierarchy = 'fecha_venta'
    ordering = ['-fecha_venta']

@admin.register(TProductos)
class TProductosAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'sku', 'marca']
    list_filter = ['marca', 'nombre', 'sku']
    search_fields = ['nombre', 'sku', 'marca']
    ordering = ['-nombre']
    
class TProductosInlineAdmin(admin.TabularInline):
    model = TProductos
    extra = 0

@admin.register(TCompetencia)
class TCompetenciaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'marca', 'precio', 'productos_id']
    list_filter = ['marca', 'nombre']
    search_fields = ['nombre', 'marca']
    # inlines = [
    #     TProductosInlineAdmin
    # ]  ## Esto permite hacer el macth con los productos     