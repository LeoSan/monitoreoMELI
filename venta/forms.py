# venta/forms.py
from django import forms
import os

class CSVUploadForm(forms.Form):
    archivo_csv = forms.FileField(
        label='Seleccionar archivo CSV',
        help_text='Selecciona el archivo CSV de ventas para cargar',
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.csv',
            'id': 'archivo_csv'
        })
    )
    
    def clean_archivo_csv(self):
        archivo = self.cleaned_data.get('archivo_csv')
        
        if archivo:
            # Validar extensión
            nombre_archivo = archivo.name.lower()
            if not nombre_archivo.endswith('.csv'):
                raise forms.ValidationError('El archivo debe tener extensión .csv')
            
            # Validar tamaño (máximo 50MB)
            if archivo.size > 50 * 1024 * 1024:  # 50MB en bytes
                raise forms.ValidationError('El archivo no puede ser mayor a 50MB')
            
            # Resetear puntero del archivo
            archivo.seek(0)
        
        return archivo