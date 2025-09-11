from django.contrib import admin
from .models import TVentas, TProductos, TProductoCompetencias, TMarcas, TCategorias


@admin.register(TVentas)
class TVentasAdmin(admin.ModelAdmin):
    list_display   = ['id', 'titulo', 'sku', 'fecha_venta', 'marca', 'total']
    list_filter    = ['marca', 'fecha_venta']
    search_fields  = ['titulo', 'sku', 'publicacion_mlm_id']
    date_hierarchy = 'fecha_venta'
    ordering       = ['-fecha_venta']


@admin.register(TMarcas)
class TMarcaAdmin(admin.ModelAdmin):
    list_display  = ['id', 'nombre', 'descripcion']
    list_filter   = ['nombre', 'descripcion']
    search_fields = ['nombre']
    ordering      = ['-nombre']
    
@admin.register(TCategorias)
class TCategoriaAdmin(admin.ModelAdmin):
    list_display  = ['id', 'nombre', 'descripcion']
    list_filter   = ['nombre', 'descripcion']
    search_fields = ['nombre']
    ordering      = ['-nombre']    

@admin.register(TProductos)
class TProductosAdmin(admin.ModelAdmin):
    list_display  = ['id', 'nombre', 'sku', 'marca_fk']
    list_filter   = ['marca_fk', 'nombre', 'sku']
    search_fields = ['nombre', 'sku']
    ordering      = ['-nombre']
    
class TProductosInlineAdmin(admin.TabularInline):
    model = TProductos
    extra = 0

@admin.register(TProductoCompetencias)
class TProductoCompetenciaAdmin(admin.ModelAdmin):
    list_display  = ['id', 'nombre_producto']
    list_filter   = ['marca_fk', 'nombre_producto']
    search_fields = ['-nombre_producto']
    # inlines = [
    #     TProductosInlineAdmin
    # ]  ## Esto permite hacer el macth con los productos     