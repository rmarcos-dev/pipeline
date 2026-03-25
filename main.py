from flask import Flask

app = Flask(__name__)

# Al usar /pipeline/ en Nginx, Flask debe responder a la raíz interna
@app.route('/')
def home():
    return """
    <h1>¡Pipeline Automatizado de rafa!</h1>
    <p>Hola Rafael, este cambio se ha hecho mediante Git Push.</p>
    <hr>
    <small>Desplegado automáticamente por GitHub Actions y servido por Nginx.</small>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
