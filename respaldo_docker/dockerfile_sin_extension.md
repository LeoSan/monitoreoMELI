# Usamos la imagen oficial de Python basada en Alpine Linux
FROM python:3.11-alpine

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo
WORKDIR /app

# ---- PASO 1: INSTALAR DEPENDENCIAS DE CONSTRUCCIÓN ----
# Se necesitan para compilar numpy, pandas y otras librerías científicas.
RUN apk add --no-cache \
    build-base \
    python3-dev \
    gfortran

# ---- PASO 2: INSTALAR DEPENDENCIAS DE SELENIUM ----
# Se necesitan para que el navegador Chrome pueda ejecutarse.
RUN apk add --no-cache \
    chromium \
    chromium-chromedriver \
    udev \
    nss

# ---- PASO 3: INSTALAR DEPENDENCIAS DE PYTHON ----
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Puerto de exposición
EXPOSE 8000

# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]