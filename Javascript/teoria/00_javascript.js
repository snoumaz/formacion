// Lenguaje nacido para las paginas web //
// Una de sus utilidades es que se ejecuten cosas en el lado cliente asi se evita trafico hacia el servidor //

/* Esto es un comentario multilinea
hasta que no finaliza > */
numero = 1 // variable no recomendado //
numero = 1; // variable recomendable //
// numero = 1; texto = "hola"; // El ; es un separador y gracias a el se pueden concatenar cosas //

// tipos de  variables //

var numero = 1 // var es una variable reservada que se puede invocar desde cualquier parte el codigo pero es un arma de doble filo //
// ya que como son globales y los nombres se pueden repetir //
let texto = "hola" // let es una variable con alcance y eso permite rehusables, ya que solo afectan a la ubicacion que se le da //
const PI = 3.1416  // const son para datos que van a ser fijos, es recomendable ponerlo en mayuscula pero no obligatorio. //

// PI = 6.28
console.log(PI)
console.log(typeof(numero))
console.log(typeof texto)

// Funciones de Ventana 
//alert("Soy un mensaje informativo") // sirve para informar
let respuesta = prompt("Le pregunta al usuario") // abre una ventana emergente para que el usuario meter un dato en una variable
alert("Me has dicho" + " " + respuesta) // de esta manera se puede concatenar.
alert(`Me has dicho ${respuesta}`) // `` = f" en python"
let respon = confirm("¿Está lloviendo?")
alert(respon) // los booleanos son true y false en miniscula