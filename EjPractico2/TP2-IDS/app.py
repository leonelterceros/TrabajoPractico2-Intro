from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message
from datetime import datetime

app = Flask(__name__)
app.secret_key = "DAUE1239"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'leonelterceros28@gmail.com'
app.config['MAIL_PASSWORD'] = 'fdgy aviu jxfu mpdy'
app.config['MAIL_DEFAULT_SENDER'] = 'leonelterceros28@gmail.com'

mail = Mail(app)

@app.route("/")
def index():
    info_evento = {

        1: {
            "nombre": "Rally MTB 2025",

            "organizador": "Club Social y Deportivo Unidos por el Deporte",
            
            "descripcion": "Carrera de MTB rural en dos modalidades 30km y 80km",
            
            "fecha": "24 de Octubre de 2025",
            
            "horario": "8am",
            
            "lugar": "Tandil, Buenos Aires",
            
            "tipo_carrera": "MTB Rural",
            
            "modalidad_costo": {
                1: {
                    "nombre": "30km",
                    "valor": "$40.000"
                },
                
                2: {
                    "nombre": "80km",
                    "valor": "$100.000"
                }
            },
            "auspiciantes": ["ausp1", "auspN"]
        }
    }
    return render_template("index.html", info_evento=info_evento)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Tomar datos
        name = request.form['name']
        surname = request.form['surname']
        telefono = request.form['telefono']
        dni = request.form['dni']
        email = request.form['email']
        categoria = request.form['categoria-carrera']

        msg = Message(
            subject=f"Nueva inscripción: {name} {surname}",
            recipients=["leonel-terceros@hotmail.com"],  # a dónde se envía
            body=f"""
            Nueva inscripción recibida:

            Nombre: {name}
            Apellido: {surname}
            Telefono: {telefono}
            documento: {dni}
            Email: {email}
            Categoría: {categoria}
            """
        )

        try:
            mail.send(msg)
            flash("✅ Inscripción enviada correctamente por correo.")
        except Exception as e:
            flash(f"❌ Error al enviar el correo: {e}")

        return redirect(url_for('register'))
    
    return render_template("registration.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5001", debug=True)

