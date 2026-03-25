# 1. Imagen base ligera de Python
FROM python:3.11-slim

# 2. Evita que Python genere archivos .pyc y permite ver logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Instalamos dependencias del sistema (opcional, por si usas git o curl)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5. Copiamos el archivo de dependencias (si ya tienes uno)
# Si no lo tienes, comenta esta línea por ahora
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# 6. Copiamos el resto del código del pipeline
COPY . .

# 7. Comando por defecto (ajústalo al nombre de tu script principal)
CMD ["python", "main.py"]
