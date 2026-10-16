import json

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

#Ejercicio 1
@app.route("/saludo", methods=['POST'])
def name():
    name_saludo = request.get_json()["name"]
    return {"name": name_saludo}, 200

if __name__ == "__main__":
    app.run(debug=True)