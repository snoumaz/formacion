/*
Hay que programar un carrito de compra de fruta.

El cliente eligirá que fruta quiere haciendo click sobre la imagen.
Un mensaje emergente le preguntará qué cantidad quiere.

Esta información se mostrará a la derecha, bajo "Total carrito", 
en <p id="carrito"></p>, de esta forma:
 Kiwi 2 kg x 4,20€/kg = 8,40 €

El total se actualizará con cada compra
 Total Compra: 8,40€
 
Se dará la opción de añadir o no más productos que se mostrarán
a continuación de los anteriores, y se sumará todo en el total. 
Por ejemplo:  
 Kiwi 2 kg x 4, 20€/kg = 8, 40€
 Pomelo 1 kg x 2,50€/kg = 2,50€
 Total Compra: 10,90€

Puedes modificar el código facilitado si ello te ayuda con el ejercicio,
pero deberás justificarlo.

Recuerda la importancia comentar con detalle el código.

 Lo importante es el cálculo, no los estilos css
 */

// const productos = document.getElementById('productos')

// let precio = document.getElementById('precio')
// let carrito = document.getElementById('carrito')
// let mensajeTotal = ""
// let totalMultiple = 0
// let mensajeUsuario = ""
// let nombre = []


// function precioFrutas(nombre,precioFruta){
//         let cantidad = prompt(`¿Que cantidad de ${nombre} desea?`)
//         let frutaTotal = parseFloat(precioFruta)*parseInt(cantidad)
//         totalMultiple +=frutaTotal
//         mensajeUsuario += `<p>${nombre} ${cantidad} x ${precioFruta}€ = ${frutaTotal.toFixed(2)}</p>`
//         mensajeTotal = `<span>Total Compra: ${totalMultiple.toFixed(2)}€</span>`
//         document.getElementById('carrito').innerHTML = mensajeUsuario + mensajeTotal

// }
let totalCompra = 0;
let carritoContenido = [];
let carritoHTML = "";

// Función que se ejecutará al hacer click sobre una fruta que en el div que las contiene esta definido el onclick
function precioFrutas(nombre, precio) {
  let cantidad = prompt(`¿Que cantidad de ${nombre} desea?`); // Pedir al usuario la cantidad que desea comprar de la fruta que ha clicado
  // Control de errores a la hora de introducir la cantidad
  if (cantidad === null) { // Si el usuario pulsa "Cancelar" en el prompt de cantidad
    return; // Salir de la función si el usuario cancela
  }
  if (isNaN(cantidad) || cantidad <= 0) { // Verificar que el dato introducido es un numero mayor que 0 y no es cualquier otro tipo de dato
    alert("Por favor, ingrese una cantidad válida."); // Si no muetra esta alerta
    return; // Salir de la función si la cantidad no es válida
  }
  let totalFruta = parseFloat(precio) * parseFloat(cantidad); // Calcular el total para la fruta seleccionada
  carritoContenido.push({ nombre, cantidad, precio, totalFruta }); // Guardar los detalles del producto en el array carritoContenido
  // Crear una línea en el carrito con un botón de eliminar (icono de papelera)
  let productoHTML = `<p id="${nombre}_${carritoContenido.length - 1}"><button id="borrar" onclick="eliminarProducto(${carritoContenido.length - 1}, ${totalFruta})">
                          <i class="fas fa-trash"></i> 
                        </button>
                        ${nombre} ${cantidad} x ${precio}€/kg = ${totalFruta.toFixed(2)}€
                      </p>`; // esta variable se añade al carritoHTML y crea una línea en el carrito con un botón de eliminar (icono de papelera)
  carritoHTML += productoHTML; // Añadir el detalle de la fruta al HTML del carrito
  totalCompra += totalFruta; // Sumar al total general de la compra
  // Actualizar el carrito y el total
  document.getElementById('carrito').innerHTML = carritoHTML;
  document.getElementById('total').innerHTML = `Total Compra: <span>${totalCompra.toFixed(2)}€</span>`;
}

function eliminarProducto(index, totalFruta) {
    carritoContenido.splice(index, 1); // Eliminar el producto del array carritoContenido
    totalCompra -= totalFruta; // Restar el total de ese producto al total general
    carritoHTML = ""; // Vaciar el HTML del carrito
    // Para cada producto en el carrito, crear una línea en el carrito con un botón de eliminar (icono de papelera) y actualizar el total de la compra general 
    for (let i = 0; i < carritoContenido.length; i++) {
      let producto = carritoContenido[i];
      carritoHTML += `<p id="${producto.nombre}_${i}"><button id="borrar" onclick="eliminarProducto(${i}, ${producto.totalFruta})">
                          <i class="fas fa-trash"></i> 
                        </button>
                        ${producto.nombre} ${producto.cantidad} x ${producto.precio}€/kg = ${producto.totalFruta.toFixed(2)}€
                      </p>`;
    }
    // Actualizar el carrito y el total
    document.getElementById('carrito').innerHTML = carritoHTML;
    document.getElementById('total').innerHTML = `Total Compra: <span>${totalCompra.toFixed(2)}€</span>`;
  }