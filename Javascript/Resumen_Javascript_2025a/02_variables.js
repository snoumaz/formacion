// VARIABLES
// Se crean con una palabra reservada:
// var
// let
// const

// var
var variable1 = 12
// con var la variable será global
var variable1 = "eertyt"

// let --> las variables tienen un ámbito o alcance (scope) de aplicación
let fruta = "naranja"
if (true) {
    let fruta = "pera"
}
console.log(fruta);

// const --> para valores que no queremos que se modifiquen durante el código
const PI = 3.1416
// PI = 5.67 <-- esto no se puede hacer

// no poner ninguna palabra reservada
bebida = "leche" // TOTALMENTE DESACONSEJADO