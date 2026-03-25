# 1. Usamos una imagen de Python ligera
FROM python:3.11-slim

# 2. Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiamos el archivo de requisitos primero (para aprovechar la caché de Docker)
COPY requirements.txt .

# 4. Instalamos las librerías
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos el resto del código (tu main.py profesional)
COPY . .

# 6. Exponemos el puerto 8000 (el que espera FastAPI)
EXPOSE 8000

# 7. Comando para arrancar la web
# --host 0.0.0.0 es vital para que sea accesible desde fuera del contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
