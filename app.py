from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Bienvenido a nuestro micronegocio</h1>"

@app.route('/api/productos')
def productos():
    productos_list = [
        {"id": 1, "nombre": "Producto A", "precio": 10.99},
        {"id": 2, "nombre": "Producto B", "precio": 15.49},
        {"id": 3, "nombre": "Producto C", "precio": 7.99}
    ]
    return jsonify(productos_list)

if __name__ == '__main__':
    app.run(debug=True)
