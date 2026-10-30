from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


tareas = []

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/tareas", methods=["GET"])      
def listar():
    return jsonify(tareas=tareas)

@app.route("/tareas", methods=["POST"])    
def anadir():
    datos = request.get_json()
    texto = datos.get("texto", "").strip()
    if texto == "":
        return jsonify(error="La tarea no puede estar vacía"), 400
    tareas.append(texto)
    return jsonify(tareas=tareas)


@app.route("/tareas/<int:indice>", methods=["DELETE"])
def borrar(indice):
    if indice < 0 or indice >= len(tareas):
        return jsonify(error="La tarea no existe"), 404
    tareas.pop(indice)
    return jsonify(tareas=tareas)

if __name__ == "__main__":
    app.run(debug=True)