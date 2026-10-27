import math
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

historial = []

OPERACIONES = {
    "sumar": "+",
    "restar": "-",
    "multiplicar": "×",
    "dividir": "÷",
    "potencia": "^",
}


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/calcular")
def calcular():
    a = request.args.get("a")
    b = request.args.get("b")
    op = request.args.get("op")

    try:
        a = float(a)
        b = float(b)
    except (TypeError, ValueError):
        return jsonify(error="a y b deben ser números"), 400

    if not (math.isfinite(a) and math.isfinite(b)):
        return jsonify(error="a y b deben ser números finitos"), 400

    if op == "sumar":
        resultado = a + b
    elif op == "restar":
        resultado = a - b
    elif op == "multiplicar":
        resultado = a * b
    elif op == "dividir":
        if b == 0:
            return jsonify(error="No se puede dividir entre 0"), 400
        resultado = a / b
    elif op == "potencia":
        try:
            resultado = math.pow(a, b)
        except (ValueError, OverflowError):
            return jsonify(error="Potencia no válida o demasiado grande"), 400
    else:
        return jsonify(error="Operación desconocida"), 400

    if resultado.is_integer():
        resultado = int(resultado)

    def limpio(n):
        return int(n) if n.is_integer() else n

    historial.append(f"{limpio(a)} {OPERACIONES[op]} {limpio(b)} = {resultado}")

    return jsonify(resultado=resultado, historial=historial)


if __name__ == "__main__":
    app.run(debug=True)
