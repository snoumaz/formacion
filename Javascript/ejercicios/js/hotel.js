// Control del nombre y apellido del cliente
const nombreform = document.querySelector('#nombre')
const apellidoform = document.querySelector('#apellido')

nombreform.addEventListener("change", ()=>{
    let nombreRevisado = nombreform.value.trim()
    const errorNombre = document.querySelector('#errorNombre')
    errorNombre.textContent = ""
    if (nombreRevisado.length < 2){
        errorNombre.textContent = "El nombre debe tener al menos dos caracteres"
        nombreform.focus()
    }
})
apellidoform.addEventListener("change", ()=>{
    let apellidoRevisado = apellidoform.value.trim()
    const errorApellido = document.querySelector('#errorApellido')
    errorApellido.textContent = ""
    if (apellidoRevisado.length < 2){
        errorApellido.textContent = "El apellido debe tener al menos dos caracteres"
        apellidoform.focus()
    }
})
// Control de la Fecha
let entrada = document.getElementById('entrada')
let salida = document.getElementById('salida')
let today = new Date()
let tomorrow = new Date(today)
tomorrow.setDate(tomorrow.getDate() + 1)
today=today.toISOString().split('T')[0]
tomorrow = tomorrow.toISOString().split('T')[0]

entrada.setAttribute("min", today)
entrada.setAttribute("value",today)
salida.setAttribute("min",tomorrow)
salida.setAttribute("value",tomorrow)

entrada.addEventListener('change', ()=>{
    salida = new Date(entrada.value)
    salida.setDate(salida.getDate() + 1)
    salida = salida.toISOString().split('T')[0]

    let fechaSalida = document.querySelector('#salida')
    fechaSalida.setAttribute("min", salida)
    fechaSalida.setAttribute('value', salida)
})
// Ventana emergente
const dialog = document.querySelector('#resumen')
const cierraVentana = document.querySelector('#cierraVentana')

cierraVentana.addEventListener('click',()=>{
    dialog.closest()
})

// Obtener los datos del formulario
const formReserva = document.forms['formReserva']

formReserva.addEventListener('submit',(e)=>{
    e.preventDefault()
    console.log(formReserva['nombre'].value);
    console.log(formReserva['apellido'].value);
    console.log(formReserva['adulto'].value);
    console.log(formReserva['nino'].value);
    console.log(formReserva['']);
    console.log(formReserva['estancia'].value);
    let resumenReserva = `<p>Reserva realizada a nombre de <span class="textoPrincipal">${formReserva['nombre'].value} ${formReserva['apellido'].value}</span></p>`
    const textoResumen = document.querySelector('#textoResumen')
    textoResumen.innerHTML = resumenReserva
    dialog.showModal()
    formReserva.reset()
})