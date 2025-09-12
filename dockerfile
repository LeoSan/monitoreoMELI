# Usamos la imagen oficial de Python basada en Alpine Linux
FROM python:3.11-alpine

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema operativo (usando apk) y el navegador Chrome
# --no-cache evita guardar el índice de paquetes, manteniendo la imagen ligera
RUN apk add --no-cache \
    chromium \
    chromium-chromedriver \
    udev \
    nss

# Instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Puerto de exposición
EXPOSE 8000

# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]