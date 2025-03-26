// Datos de trabajo

const flores = JSON.parse(localStorage.getItem('flores')) || [
  { nombre: "rosa", color: "rojo", floracion: "primavera", stock: true },
  { nombre: "rosa", color: "blanco", floracion: "verano", stock: true },
  { nombre: "jazmín", color: "blanco", floracion: "verano", stock: false },
  { nombre: "crisantemo", color: "blanco", floracion: "otoño", stock: false },
  { nombre: "cerezo", color: "blanco", floracion: "primavera", stock: false },
  { nombre: "clavel", color: "rojo", floracion: "verano", stock: true },
];

flores.sort((a, b) => {
  return a.nombre.localeCompare(b.nombre, "es-ES", { numeric: true });
});


// ==============================================================================
// EJERCICIO 1

// console.log(flores);

// Tiene que mostrarse en el HTML los datos de las flores como lista
// Flor: rosa, de color rojo, florece en primavera y tenemos stock
// Se mostrará el resultado en #ejercicio1

// for clásico
// const ejercicio1 = document.querySelector("#ejercicio1");
const ejercicio1 = document.getElementById("ejercicio1");
// for (let i = 0; i < flores.length; i++) {
//   if (flores[i].stock) { 
//     let mensaje = `<p>Flor: ${flores[i].nombre}, de color ${flores[i].color},
//      florece en ${flores[i].floracion}, hay stock</p>`;
//     document.getElementById('ejercicio1').innerHTML += mensaje;   
// }else{
//   let mensaje = `<p>Flor: ${flores[i].nombre}, de color ${flores[i].color},
//    florece en ${flores[i].floracion}, no hay stock</p>`;
//   document.getElementById('ejercicio1').innerHTML += mensaje;
// }
// }

function mostrarFlores(id){
let html = '<ul>'
flores.forEach((flor)=>{
  let stock = ""
  if (!flor.stock){
    stock = "no"
  }
  html +=`<li> Flor: ${flor.nombre}, color: ${flor.color}, floracion: ${flor.floracion} y ${stock} tenemos stock.</li>   `
})
html += "</ul>"
id.innerHTML = html
}
mostrarFlores(ejercicio1)

// ==============================================================================
// EJERCICIO 2
// Listar las flores de color blanco que florecen en verano
// Modelo de mensaje de salida:
// Flor: rosa, de color blanco, florece en verano y tenemos stock
// Se mostrará el resultado en #ejercicio2

const ejercicio2 = document.getElementById("ejercicio2");
// for (let i = 0; i < flores.length; i++) {
//   if (flores[i].color === 'blanco'&& flores[i].floracion === 'verano' && flores[i].stock === true){
//     let mensaje = `<p>Flor: ${flores[i].nombre}, de color ${flores[i].color},
//      florece en ${flores[i].floracion} y hay stock</p>`;
//      document.getElementById('ejercicio2').innerHTML += mensaje;
// }else{
//   let mensaje = `<p>Flor: ${flores[i].nombre}, de color ${flores[i].color},
//      florece en ${flores[i].floracion} y no hay stock</p>`;
//   document.getElementById('ejercicio2').innerHTML += mensaje;
// }
// }

// function mostrarEjercicio2(id){
//   let html = '<ul>'
//   flores.forEach((flor)=>{
//     if (flor.color == "blanco" && flor.floracion == "verano" && flor.stock === true  && flor.stock === form3.stock.value){
//       html +=`<li> Flor: ${flor.nombre}, color: ${flor.color}, floracion: ${flor.floracion}.</li>` 
//     }
//   })
//   html += "</ul>"

// }
// mostrarEjercicio2(ejercicio2)
// ==============================================================================
// EJERCICIO 3

// A partir del formulario incluido, hay que mostrar que datos
// corresponden a la selección realizada.
// Se mostrarán en forma de lista como los modelos anteriores.
// Si no hay ninguna flor que cumpla las condiciones, se mostrará este mensaje:
// "No hay flor que cumpla las condiciones"
// Se mostrará el resultado en #ejercicio3

const form3 = document.forms['formEj3'];
const ejercicio3 = document.getElementById('ejercicio3');

// function mostrarEjercicio3(id) {
//   form3.addEventListener('change', () => {
//     let html = '<ul>';
//     let found = false; 
//     flores.forEach((flor) => {
//       if (
//         form3.color.value === flor.color && 
//         form3.floracion.value === flor.floracion && 
//         form3.stock.value == flor.stock 
//       ) {
//         html += `<li>Color: ${flor.color}, Floración: ${flor.floracion}, Stock: ${flor.stock}</li>`;
//         found = true;
//       }
//     });
//     if (!found) {
//       html = '<ul><li>No hay flor que cumpla las condiciones</li></ul>';
//     } else {
//       html += '</ul>';
//     }
//     id.innerHTML = html;
//   });
// }

// mostrarEjercicio3(ejercicio3);

// form3.addEventListener('change', () => {
//   const color = form3.color.value;
//   const floracion = form3.floracion.value;
//   const stock = form3.stock.value;
  
//   mensajeEj3(ejercicio3, color, floracion, stock);
// });

// function mensajeEj3(id, color, floracion, stock) {
//   let html = "<ul>";
//   let contadorFlores = 0;
  
//   flores.forEach((flor) => {
//     let textostock = flor.stock ? flor.stock : "No"; 
//     if (flor.color === color && flor.floracion === floracion && String(flor.stock) === stock) {
//       textostock = "Si"
//       html += `<li>Color: ${flor.color}, Floración: ${flor.floracion}, Stock: ${textostock}</li>`;
//       contadorFlores++;
//     }
//   });

//   html += '</ul>';
  
//   if (contadorFlores === 0) {
//     html = '<p>No hay flor que cumpla las condiciones</p>';
//   }

//   id.innerHTML = html;
// }


// ==============================================================================
// EJERCICIO 4

// Hacer un formulario para obtener una flor del array por su nombre.
// Se mostrará el resultado en #ejercicio4

// const formEj4 = document.forms['formEj4']
// const ejercicio4 = document.getElementById('ejercicio4')

// formEj4.addEventListener("submit", (e)=>{
//   e.preventDefault()
//   const nombre = formEj4.nombre.value;
//   let html = "<ul>"
//   flores.forEach((flor)=>{
//     if(flor.nombre == nombre.trim().toLocaleLowerCase()){
//       let textoStock = "";
//       if (!flor.stock){
//         textoStock = "no"
//       }

//       html += `<li> Flor: ${flor.nombre}, color: ${flor.color}, floracion: ${flor.floracion}.</li>`
//     }
//     html += "</ul>"
//   });
  
//   ejercicio4.innerHTML = html
// })


// ==============================================================================
// EJERCICIO 5

// Crea y programa un formulario para añadir flores al array.
// Por ejemplo:
// flor: cyclamen, color:rosa, floracion: invierno, stock:true
// Tiene que actualizarse automáticamente la lista del ejercicio 1

// const formEj5 = document.forms['formEj5']
// const ejercicio5 = document.getElementById('ejercicio5')
// formEj5.addEventListener('submit',(e)=>{
// e.preventDefault()
// const nombre = formEj5.nombre.value
// const color = formEj5.color.value
// const floracion = formEj5.floracion.value
// const stock = formEj5['stock'].value
// flores.push({nombre,color,floracion,stock})
// mostrarFlores(ejercicio5)
// localStorage.setItem('flores',JSON.stringify(flores))


// })

// ============================================================================== 
/* E X T R A S */

// ==============================================================================
// EJERCICIO 6

// Crea y programa un formulario para añadir precios a las flores:
// rosa roja : 8.00€
// rosa blanca : 10.00€
// jazmin: 12.00€
// crisantemo: 5.00€
// cerezo: 25.00€
// cyclamen: 4.50€
// Tiene que actualizarse automáticamente la lista del ejercicio 1

// ==============================================================================
// EJERCICIO 7

// Crea la forma de eliminar elementos del array
// Tiene que actualizarse automáticamente la lista del ejercicio 1

// ==============================================================================
// EJERCICIO 8

// Crea la forma de editar elementos del array de flores
// Todas las propiedades deben poder ser editadas: nombre, color, floración, stock  y precio
// Tiene que actualizarse automáticamente la lista del ejercicio 1
