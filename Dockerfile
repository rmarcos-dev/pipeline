# 1. Usamos una imagen ligera de Python
FROM python:3.11-slim

# 2. Instalamos curl para que el Healthcheck funcione
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# 3. Directorio de trabajo
WORKDIR /app

# 4. CAPA DE DEPENDENCIAS (No cambiará si no tocas requirements.txt)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. CAPA DE CÓDIGO (Lo que cambiarás en cada push)
COPY . .

# 6. SEGURO DE VIDA (Healthcheck)
# Docker vigila que la app responda. Si falla, el contenedor se marca como "unhealthy"
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/ || exit 1

# 7. Ejecución
EXPOSE 8000
CMD ["python", "main.py"]
