import random
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
random_n = random.randint(1, 100)

@app.route("/")
def inicio():
    return render_template("index.html")

#Ejercicio 1
@app.route("/saludo", methods=['POST'])
def name():
    name_saludo = request.get_json()["name"]
    return {"name": name_saludo}, 200

@app.route("/guess", methods=['POST'])
def guess():
    message = {}
    print(request.get_json())
    guess_num = int(request.get_json()["number"])
    tries = int(request.get_json()["try"]) + 1
    if(guess_num==random_n):
        message = {"text": "¡Has acertado el número!", "try": tries, "status": True}
    else:
        if(guess_num < random_n):
            message = {"text": "El numero es mayor", "try": tries, "status": False}
        else:
            message = {"text": "El numero es menor", "try": tries, "status": False}
    
    return message


if __name__ == "__main__":
    app.run(debug=True)