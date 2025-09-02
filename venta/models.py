
from django.db import models

class TVentas(models.Model):
    id = models.BigAutoField(primary_key=True)
    publicacion_mlm_id = models.CharField(max_length=255)
    venta_id = models.BigIntegerField(null=True, blank=True)
    titulo = models.TextField()
    sku = models.CharField(max_length=255)
    fecha_venta = models.DateTimeField()
    marca = models.CharField(max_length=255)
    precio_unitario = models.FloatField(null=True, blank=True)
    unidades = models.BigIntegerField()
    total = models.FloatField()

    class Meta:
        db_table = 't_ventas'  # Especifica el nombre exacto de la tabla
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return f"{self.titulo} - {self.fecha_venta}"
    
    
class TProductos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    marca = models.CharField(max_length=255, null=True, blank=True)
    sku = models.CharField(max_length=255,null=True, blank=True)
    total_stock = models.BigIntegerField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    class Meta:
        db_table = 't_productos'  # Especifica el nombre exacto de la tabla
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f"{self.nombre} - {self.descripcion}"    
    
    
class TCompetencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.FloatField(null=True, blank=True)
    marca = models.CharField(max_length=255, null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    productos_id = models.ForeignKey(TProductos, on_delete=models.CASCADE)## Cardinalidad  1 . M 
    class Meta:
        db_table = 't_competencias'  # Especifica el nombre exacto de la tabla
        verbose_name = 'Competencia'
        verbose_name_plural = 'Competencias'

    def __str__(self):
        return f"{self.nombre} - {self.marca}"        
    