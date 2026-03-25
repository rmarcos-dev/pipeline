from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>¡App Desplegada con Éxito!</h1><p>Hola Rafael, esta web corre dentro de Docker.</p>"

if __name__ == "__main__":
    # 0.0.0.0 es vital para que sea accesible desde fuera del contenedor
    app.run(host='0.0.0.0', port=8000)
