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