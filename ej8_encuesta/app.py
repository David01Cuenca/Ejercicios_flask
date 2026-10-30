from datetime import datetime
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

mensajes = []

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/mensajes", methods=["GET"])      
def listar():
    return jsonify(mensajes=mensajes)

@app.route("/mensajes", methods=["POST"])     
def publicar():
    datos = request.get_json(silent=True) or {}
    autor = str(datos.get("autor", "")).strip()
    texto = str(datos.get("texto", "")).strip()

    if autor == "" or texto == "":
        return jsonify(error="El autor y el mensaje son obligatorios"), 400
    if len(autor) > 30:
        return jsonify(error="El autor no puede superar 30 caracteres"), 400
    if len(texto) > 280:
        return jsonify(error="El mensaje no puede superar 280 caracteres"), 400

    mensajes.append({
        "autor": autor,
        "texto": texto,
        "hora": datetime.now().strftime("%H:%M")
    })
    return jsonify(mensajes=mensajes)

if __name__ == "__main__":
    app.run(debug=True)
