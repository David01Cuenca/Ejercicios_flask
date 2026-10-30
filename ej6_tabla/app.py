from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

ALUMNOS = [
    {"nombre": "Ana",    "curso": 1, "nota": 7.5},
    {"nombre": "Bruno",  "curso": 1, "nota": 4.2},
    {"nombre": "Carla",  "curso": 2, "nota": 9.1},
    {"nombre": "David",  "curso": 2, "nota": 5.0},
    {"nombre": "Elena",  "curso": 1, "nota": 6.8},
    {"nombre": "Fran",   "curso": 2, "nota": 3.9},
    {"nombre": "Gema",   "curso": 1, "nota": 8.4},
    {"nombre": "Hugo",   "curso": 2, "nota": 6.1},
]

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/alumnos")
def alumnos():
    curso = request.args.get("curso", "todos")
    orden = request.args.get("orden", "nombre")

    if curso == "todos":
        lista = ALUMNOS
    else:
        lista = [a for a in ALUMNOS if str(a["curso"]) == curso]

    # Ampliación: ordenar y calcular la media
    if orden == "nota":
        lista = sorted(lista, key=lambda a: a["nota"], reverse=True)
    else:
        lista = sorted(lista, key=lambda a: a["nombre"])

    media = round(sum(a["nota"] for a in lista) / len(lista), 2) if lista else None
    return jsonify(alumnos=lista, media=media)

if __name__ == "__main__":
    app.run(debug=True)
