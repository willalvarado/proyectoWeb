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

# Manejar la solicitud POST para guardar las compras
@app.route('/guardar_compras', methods=['POST'])
def guardar_compras():
    try:
        data = request.json
        cursor = conn.cursor()
       @app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get the form data
        name = request.form['nombre']
        email = request.form['email']
        area = request.form['area']
        comment = request.form['comentarios']

        # Insert the data into the database
        cur.execute("INSERT INTO contact (nombre, email, area, comentarios) VALUES (%s, %s, %s, %s)", (name, email, area, comment))
        conn.commit()
        cursor.close()

        return jsonify({"mensaje": "Datos guardados exitosamente."})

    except Exception as e:
        return jsonify({"error": f"Error al guardar los datos: {str(e)}"})


if __name__ == '__main__':
    app.run(debug=True)
