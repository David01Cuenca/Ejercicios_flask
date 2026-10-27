from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Estado de la encuesta guardado en Python (se pierde al reiniciar)
LENGUAJES = ["Python", "JavaScript", "Java", "C"]
USOS = ["Web", "Datos", "IA", "Juegos"]

votos = {l: 0 for l in LENGUAJES}
usos_contados = {u: 0 for u in USOS}
comentarios = []


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/votar", methods=["POST"])
def votar():
    # Radio: un solo valor. Checkbox: varios valores -> getlist
    lenguaje = request.form.get("lenguaje")
    usos = request.form.getlist("uso")
    comentario = request.form.get("comentario", "").strip()

    # Validar en el servidor
    if lenguaje not in votos:
        return jsonify(error="Elige un lenguaje."), 400
    if len(comentario) > 280:
        return jsonify(error="Comentario demasiado largo."), 400

    # Sumar el voto
    votos[lenguaje] += 1
    for uso in usos:
        if uso in usos_contados:  # ignorar valores inventados
            usos_contados[uso] += 1
    if comentario:
        comentarios.append(comentario)

    return jsonify(mensaje="¡Gracias!")


@app.route("/resultados")
def resultados():
    return jsonify(
        votos=votos,
        total=sum(votos.values()),
        usos=usos_contados,
        comentarios=comentarios,
    )


if __name__ == "__main__":
    app.run(debug=True)
