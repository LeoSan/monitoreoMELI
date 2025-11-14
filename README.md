## **Informe Técnico: Sistema de Análisis de Ventas con Integración de Datos Excel y Monitoreo Competitivo**

### **1. RESUMEN EJECUTIVO**

El proyecto consiste en el desarrollo de una solución de inteligencia de negocio que procese datos de ventas existentes almacenados en archivos Excel, los migre a una base de datos PostgreSQL, y complemente esta información con datos de precios de la competencia obtenidos mediante web scraping selectivo. El sistema generará dashboards analíticos para la toma de decisiones comerciales estratégicas.

### **2. ALCANCE DEL PROYECTO**

#### **2.1 Funcionalidades Incluidas**
- Migración automatizada de datos desde archivos Excel a PostgreSQL
- Procesamiento y normalización de datos históricos de ventas
- Web scraping dirigido para extracción de precios competitivos
- Dashboard interactivo con métricas de rendimiento por producto
- Sistema de reportes comparativos de precios vs. competencia
- Análisis de tendencias de ventas y comportamiento del mercado

#### **2.2 Limitaciones del Alcance**
- Scraping limitado únicamente a precios de competidores específicos
- No incluye extracción masiva de datos de mercado
- Procesamiento batch de datos (no tiempo real)

### **3. ARQUITECTURA DE SISTEMA**

#### **3.1 Patrón Arquitectónico: Arquitectura por Capas (Layered Architecture)**

**Justificación:** Dada la naturaleza del proyecto con procesamiento de datos estructurados y operaciones bien definidas, una arquitectura por capas ofrece:
- Separación clara de responsabilidades
- Facilidad de mantenimiento y testing
- Escalabilidad incremental
- Bajo acoplamiento entre componentes

#### **3.2 Estructura de Capas**

**Capa de Presentación (Presentation Layer)**
- Dashboards web desarrollados en Django
- Interfaces de carga de archivos Excel
- Reportes y visualizaciones interactivas
- Panel de administración del sistema

**Capa de Lógica de Negocio (Business Logic Layer)**
- Módulo de procesamiento de datos Excel
- Motor de análisis de tendencias y KPIs
- Sistema de validación y limpieza de datos
- Generador de reportes comparativos

**Capa de Servicios (Service Layer)**
- Servicio de migración de datos (Excel → PostgreSQL)
- Servicio de web scraping para precios competitivos
- Servicio de cálculo de métricas de negocio
- Servicio de generación de alertas básicas

**Capa de Acceso a Datos (Data Access Layer)**
- ORM de Django para operaciones CRUD
- Repositorios especializados para consultas analíticas
- Gestión de conexiones y transacciones de base de datos

### **4. DISEÑO DE BASE DE DATOS**

#### **4.1 Modelo de Datos Relacional**

- por definir 

### **5. COMPONENTES DEL SISTEMA**

#### **5.1 Módulo de Migración de Datos (ETL Simplificado)**

**Patrón de Diseño:** Strategy Pattern para diferentes formatos de Excel

**Responsabilidades:**
- Validación de estructura de archivos Excel
- Transformación y normalización de datos
- Detección y manejo de duplicados
- Carga incremental vs. carga completa



#### **5.2 Motor de Web Scraping Selectivo**

**Patrón de Diseño:** Template Method para diferentes sitios de competidores
- por definir

#### **5.3 Engine de Analytics**

**Patrón de Diseño:** Observer Pattern para cálculo de métricas dependientes

**Métricas Calculadas:**
- Tendencia de ventas por producto (crecimiento/decrecimiento)
- Análisis de estacionalidad
- Comparativa de precios vs. competencia
- Identificación de productos con mayor/menor performance
- Cálculo de market share relativo

### **7. CONSIDERACIONES TÉCNICAS**

#### **7.1 Gestión de Calidad de Datos**
- Validación de integridad en múltiples niveles
- Detección automática de anomalías en datos de ventas
- Sistema de flags para datos sospechosos o incompletos

#### **7.2 Optimización de Performance**
- Cache de consultas frecuentes en Redis
- Precálculo de métricas en tareas programadas
- Paginación eficiente para grandes volúmenes de datos

#### **7.3 Escalabilidad**
- Diseño preparado para crecimiento de productos monitoreados
- Arquitectura que permite agregar nuevos competidores fácilmente
- Base de datos optimizada para consultas analíticas



### **9. RIESGOS Y MITIGACIONES**

**Riesgos Técnicos:**
- Cambios en estructura de sitios web → Scraping modular y configurable
- Bloqueo por parte de sitios web → Rotación de proxies y user agents
- Corrupción de datos Excel → Validaciones exhaustivas pre-migración

**Riesgos de Negocio:**
- Datos históricos inconsistentes → Sistema de flags y validación manual
- Competidores modifican estructura web → Alertas automáticas de fallos

### **10. CONCLUSIONES**

El diseño propuesto ofrece una solución robusta y escalable que aprovecha los datos existentes en Excel mientras incorpora inteligencia competitiva mediante scraping selectivo. La arquitectura por capas garantiza mantenibilidad y permite evolución gradual del sistema hacia funcionalidades más avanzadas en el futuro.

La implementación de este sistema proporcionará una ventaja competitiva significativa al permitir decisiones basadas en datos tanto internos como del mercado, optimizando la estrategia de precios y identificando oportunidades de crecimiento.


## **Lista de Software e Instalaciones para Windows**

### **1. HERRAMIENTAS BASE**
- Python 3.11+
- Git for Windows
- Visual Studio Code
- PostgreSQL 15+
- pgAdmin 4

### **2. EXTENSIONES DE VISUAL STUDIO CODE**
- Python
- Django
- PostgreSQL
- Excel Viewer
- GitLens

### **3. LIBRERÍAS PYTHON PRINCIPALES**
- Django
- djangorestframework
- django-cors-headers
- psycopg2-binary
- django-extensions

### **4. PROCESAMIENTO DE DATOS**
- pandas
- openpyxl
- xlrd
- numpy

### **5. WEB SCRAPING**
- requests
- beautifulsoup4
- selenium
- lxml

### **6. TAREAS ASÍNCRONAS**
- celery
- django-celery-beat
- redis (opcional)

### **7. FRONTEND Y VISUALIZACIÓN**
- django-bootstrap4
- django-crispy-forms

### **8. DESARROLLO Y TESTING**
- pytest
- pytest-django
- coverage
- flake8
- black
- django-debug-toolbar
- python-dotenv

### **9. NAVEGADORES Y DRIVERS**
- ChromeDriver
- GeckoDriver (Firefox)


## Desarrollo 

## Instalación
- Paso 1: Instalamos los software necesarios
    - python3 -> no olvidemos variables de entorno
    - PostgreSQL motor y su pgAdmin4 ->
    - nodejs   

- Paso 2: siempre tenemos que tener activo el entorno python 
    - Para organización del proyecto creamos en C:/ una carpeta llamada  [ProyectosDev] y se crea para esa carpeta su entorno 
    - Creamos Entorno => ´python -m venv entornoDev´  "Esto solo se ejecuta una vez"
    - Activamos => C:\proyectosDev> ´entornoDev\Scripts\activate.bat´ [Windows]
        
- Paso 3: Creamos proyecto Django con los siguientes comandos
    - Nota:  esto no funciona si no activamos en el entorno 
    - Instalamos LIB    => ´pip install Django´
    - Creamos Proyecto  => ´django-admin startproject dashBoard´
    - Validamos         => ´django-admin --help´ -> Nos debe Listar comandos usados en Django 
    - Corremos Proyecto => ´python manage.py runserver´ Se ejeucta en LocalHost -> DENTRO DEL DIR operacion que es el master 

- Paso 4: Recuerda Django es un poco diferente creamos Proyecto pero dentro del proyecto creamos App. para nuestra jerga php modulos 
    - Nota => En Pocas Palabras vamos creando a medidas que vamos necesitando para este caso si se desea Usuarios, Productos, Ventas, Marcas etc. habra que ejecutar este comando cada vez [User, Product, Marcas, Ventas]
    - Creamos App => (entornoDev) C:\proyectosDev\MonitoreoMELI>  ´python manage.py startapp venta
    - Cada vez que se ejecute debemos añadirlo al setting.py General para que se pueda comunicar entre si. 

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'operacion',#<---- aqui
]

``` 

## Base De Datos
- Paso : Como estamos en windows debemos crear variables de entorno en el Path crear 'C:\Program Files\PostgreSQL\17\bin' claro antes debemos tener instalado postgresql y debemos tenerlo corriendo
- Paso : Instalamos LIB -> ´pip install psycopg2-binary´ 
- Paso : Instalamos LIB para manejar variables entorno python -> ´pip install python-dotenv´    
    - Luego Creamos nuestro archivo ´.env´ *ojo* debe ir a la raiz de manage.py 
    - creamos nuestras variables de entorno
```env

DB_NAME=tu1_madre
DB_USER=tu1_madre
DB_PASSWORD=tu1_madre
DB_HOST=localhost
DB_PORT=5432

``` 

- Paso : Ubicamos en nuestra app principal para este caso es operacion el archivo setting.py y anexamos nuestra configuración no olvidemos importar antes las variables de entorno. 

```python

import os
from dotenv import load_dotenv

load_dotenv()

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

```
- Paso : Validamos con el siguiente comando si la conexion funciona -> ´python manage.py dbshell´ *Si nos muestra la consola estamos bien*
- GENERAR SEEDER 
    - python manage.py makemigrations nombre_de_tu_app --empty --name seed_productos
    - python manage.py migrate

## Modo Admin Django 
- Paso : ejecutamos comando migrate ´python manage.py migrate´
    - Podemos tambien ver las migraciones que faltan con este comando ´python manage.py showmigrations´

- Paso : Para iniciar el modo admin de Django debemos ejecutar este comando solo se hace una sola vez  ´python manage.py createsuperuser´
    - nos pedira crear un usuario y contraseña guardala ya que esto es importante 

- Paso : Configuramos ´operacion/urls.py´ debe verse así 

```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
]
```

- Paso : Validamos nuestro ´setting.py´ que este añadida las app correspondientes 

- Paso : Ejecutamos los migrate siempre que se realice alguna modificación de BASEDATOS
    - python manage.py makemigrations -> Genera la migration
    - python manage.py migrate         -> ejecuta la migracion 

## Ejecutamos ADMIN 
- Paso : Debemos crear la carpeta stactic en operacion y buscar 'operacion/setting.py' y anexar el código

```python
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/5.2/howto/static-files/

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # Para desarrollo
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
```

-   Paso : Para ver los cambios aplicamos este comando ´python manage.py runserver´
    - Entramos Modo Admin => ´http://127.0.0.1:8000/admin/´  







## CONFIGURACION FRONT 

- Paso 1: Instalamos LIB 
    - Ejecutamos => ´npm install -D tailwindcss´


- Paso 2: debemos crear la configuración del directorio de la siguiente manera 

operacion/
├── templates/
│   ├── base.html
│   ├── dashboard/
│   │   ├── index.html
│   │   └── partials/
│   │       ├── header.html
│   │       └── sidebar.html
└── static/
    ├── css/
    ├── js/
    └── img/

- Paso 3: Configuramos templates 

```python

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            # ... resto de configuración
        },
    ]
```
    - Ejecutamos => ´npx tailwindcss init´


## Validamos los requirements 
- Paso 1: pip freeze > requirements.txt
- Paso 2: pip install -r requirements.txt 



## Bitacora 
- Desarrollo de arquitectura 
- Desarrollo de Base de Datos
- Desarrollo de UploadCsv  


## Comandos MAC  
- docker compose down -v
- docker compose up --build -d

## Aplicar migraciones de Django
- docker compose exec django python manage.py makemigrations
- docker compose exec django python manage.py migrate

##  Verificar migraciones aplicadas
- docker compose exec django python manage.py showmigrations

# Crear Superusuario
- docker compose exec django python manage.py createsuperuser
- docker compose logs -f django



// SCROLL https://github.com/urian121/scroll-infinito-con-django-htmx-y-mysql 
