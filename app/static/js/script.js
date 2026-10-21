//Ejercicio 1
let tries = 0;
async function pedir() {
    const name_data = document.getElementById("name").value;   
    const response = await fetch("/saludo", {
        method: "POST",
        headers: {
            "Content-Type":
                "application/json"
        },
        body: JSON.stringify({ "name": name_data })
    })
    const datos = await response.json();
    document.getElementById("respuesta")
        .textContent = "Hola señor/a " + datos.name
}

async function guess_number() {
    const number_data = document.getElementById("number_guess").value;
    const response = await fetch("/guess", {
        method: "POST",
        headers: {
            "Content-type":
                "application/json"
        },
        body: JSON.stringify({number:number_data, try: tries})
    })
    let data = await response.json();
    if(data.status){
        document.getElementById("guess_text")
            .textContent= data.text + '\n' +"Número de intentos: " + data.try
    } else {
        document.getElementById("guess_text")
        .textContent= data.text
        tries=data.try
    }
    
}