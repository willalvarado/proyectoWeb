from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# Configura la conexión a la base de datos
conn = psycopg2.connect(
    host="localhost",
    database="proyectoWeb",
    user="postgres",
    password="1234"
)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Ruta para recibir los comentarios del formulario como JSON
@app.route('/guardar_comentario', methods=['POST'])
def guardar_comentario():
    if request.method == 'POST':
        try:
            # Obtener datos JSON del cuerpo de la solicitud
            data = request.get_json()

            nombre = data.get('nombre')
            email = data.get('email')
            area = data.get('area')
            comentarios = data.get('comentarios')

            cursor.execute("INSERT INTO contact (nombre, email, area, comentarios) VALUES (%s, %s, %s, %s)",
                           (nombre, email, area, comentarios))

            conn.commit()

            return jsonify({'status': 'Comentario guardado exitosamente'})

        except Exception as e:
            return jsonify({'error': f'Error al guardar el comentario: {str(e)}'})

# Manejar la solicitud POST para guardar las compras
@app.route('/guardar_compras', methods=['POST'])
def guardar_compras():
    try:
        data = request.json
        id_usuario = 999

        # Crear una nueva factura
        cursor.execute("INSERT INTO factura (id_usuario) VALUES (%s) RETURNING idFactura", (id_usuario,))
        id_factura = cursor.fetchone()[0]

        # Insertar las compras asociadas a la factura
        for compra in data:
            producto_id = int(compra['idProducto'])
            cantidad = int(compra['cantidad'])  
            precio = float(compra['precio'])
            subtotal = cantidad * precio

            cursor.execute("INSERT INTO compras (idFactura, usuario_id, producto_id, cantidad, precio, subtotal) VALUES (%s, %s, %s, %s, %s, %s)",
                        (id_factura, id_usuario, producto_id, cantidad, precio, subtotal))

        conn.commit()

        return jsonify({"mensaje": "Datos guardados exitosamente."})

    except Exception as e:
        return jsonify({"error": f"Error al guardar los datos de compras: {str(e)}"})


if __name__ == '__main__':
    app.run(debug=True)
