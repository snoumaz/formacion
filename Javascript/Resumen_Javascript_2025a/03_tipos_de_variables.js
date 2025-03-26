/*
TIPOS DE VARIABLES
Hay muchísimos,. El programador puede crear los suyos propios.

Para saber de que tipo es una variable podemos usar la función typeof
console.log(typeof(laVariable))

Vamos a empezar por los tipos primitivos.
*/

// números
let precio = 3.5 // <-- number 
let unidades = 3 // <-- number 
// Javascript no es preciso con los decimales
console.log(3.01 + 2.1 );

// string o cadenas de texto
let texto1 = "Soy un texto"
let texto2 = 'Soy un texto'
let texto3 = "I'm the best"
let texto4 = 'Ella me dijo "buenos días"'
console.log(texto4);
let texto5 = `hoy es viernes` // <-- template literal o template string
let resultado = `Precio: ${precio}, total ${precio * unidades}`
let saludo1 = "Buenos"
let saludo2 = "días"
let saludoCompleto = saludo1 + saludo2 // concatenación con +
let prueba = saludoCompleto - saludo2 // no se pueden restar directamente los strings 
console.log(prueba);

// boolean (verdadero --> true || falso --> false)
let condicion1 = true
let condicion2 = false

// Las condiciones se obtienen de operadores de comparación o de funciones específicas
// Por ejemplo, ¿3 es igual a 5?
// == para obtener la igualdad
console.log(3 == 5);

// NaN --> Not A Number 
// operaciones que no pueden devolver un resultado

// Infinity --> se obtiene al dividir por 0

// Undefined
let diaSemana
console.log(typeof(diaSemana));




