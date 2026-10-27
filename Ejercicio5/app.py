from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

inscritos = []


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/registro", methods=["POST"])
def registro():
    nombre = request.form.get("nombre", "").strip()
    correo = request.form.get("correo", "").strip()
    edad = request.form.get("edad", "").strip()
    curso = request.form.get("curso", "")
    normas = request.form.get("normas")  # None si no está marcado

    errores = []
    if not nombre:
        errores.append("Falta el nombre")
    if "@" not in correo:
        errores.append("Correo no válido")
    elif any(i["correo"].lower() == correo.lower() for i in inscritos):
        errores.append("Correo repetido")
    if not edad.isdigit() or not 16 <= int(edad) <= 99:
        errores.append("Edad: de 16 a 99")
    if curso not in ["1", "2", "3", "4"]:
        errores.append("Curso no válido")
    if not normas:
        errores.append("Acepta las normas")

    if errores:
        return jsonify(errores=errores), 400

    inscritos.append({"nombre": nombre, "correo": correo, "edad": int(edad), "curso": curso})
    return jsonify(mensaje=f"Inscripción completada. Ya sois {len(inscritos)}.")


@app.route("/inscritos")
def listar_inscritos():
    return jsonify(inscritos=[{"nombre": i["nombre"], "curso": i["curso"]} for i in inscritos])


if __name__ == "__main__":
    app.run(debug=True)
