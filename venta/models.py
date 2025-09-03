
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
    
    @classmethod
    def productos_por_marca(cls, marca='NUBE'):
        """
        Obtiene productos únicos por marca ordenados por título
        """
        return cls.objects.filter(
            marca=marca
        ).values(
            'titulo', 'publicacion_mlm_id'
        ).distinct().order_by('titulo')


    # Alternativa usando SQL raw si prefieres mantener la consulta exacta
    @classmethod
    def productos_por_marca_raw(cls, marca):
        """
        Obtiene productos únicos por marca usando SQL raw
        """
        from django.db import connection
        
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT tv.titulo, tv.publicacion_mlm_id
                FROM public.t_ventas as tv 
                WHERE tv.marca = %s
                GROUP BY tv.titulo, tv.publicacion_mlm_id
                ORDER BY tv.titulo ASC
            """, [marca])
            
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]      
    
    
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
    
    
    
