// alert('ok') comprobacion

// Obtener el nodo, con ide CABRIOLET
// const cabriolet = document.getElementById('cabriolet') // recorre el html hasta encontrar el id, solo se ejecutara en el primero
// const cabriolet = document.querySelector('#cabriolet') // hace lo mismo que el anterior
const alquiler = document.querySelector('#alquiler')
const importe = document.querySelector('main section:nth-child(2)')


// cabriolet.addEventListener('click', ()=>{
//     let dias = prompt('¿Días de Alquiler?')
//     let precio = cabriolet.querySelector('ul li:last-child').textContent
//     precio = precio.split('€')[0]
//     // alert(precio)
//     importe.style.display = "block"
//     let alquilerTotal = parseFloat(precio) * parseInt(dias)
//     // let mensajeUsuario = `${dias} dias de alquiler x ${precio}€/dia = ${alquilerTotal.toFixed(2)}€`
//     // alquiler.textContent = mensajeUsuario  
//     let mensajeUsuario = `${dias} dias de alquiler x ${precio}€/dia = <span class="bold">${alquilerTotal.toFixed(2)}</span>€`
//     alquiler.innerHTML = mensajeUsuario
// })
// function alquilarVehiculo(precioDia){
//     let dias = prompt('¿Días de Alquiler?')
//     importe.style.display = "block"
//     let alquilerTotal = parseFloat(precioDia) * parseInt(dias)
//     // let mensajeUsuario = `${dias} dias de alquiler x ${precio}€/dia = ${alquilerTotal.toFixed(2)}€`
//     // alquiler.textContent = mensajeUsuario  
//     let mensajeUsuario = `${dias} dias de alquiler x ${precioDia}€/dia = <span class="bold">${alquilerTotal.toFixed(2)}</span>€`
//     alquiler.innerHTML = mensajeUsuario
// }
var mensajeUsuario = ""
var toralMultiple = 0
function alquilarVehiculo(precioDia){
        let dias = prompt('¿Días de Alquiler?')
        importe.style.display = "block"
        let alquilerTotal = parseFloat(precioDia)*parseInt(dias)
        toralMultiple +=alquilerTotal
        mensajeUsuario += `<p>${dias} dias de alquiler x ${precioDia}€/dia = <span class="bold">${alquilerTotal.toFixed(2)}</span>€</p>`
        mensajeTotal = `<p>Facturación = <span class="bold">${toralMultiple.toFixed(2)}</span>€`
        alquiler.innerHTML = mensajeUsuario + mensajeTotal
}