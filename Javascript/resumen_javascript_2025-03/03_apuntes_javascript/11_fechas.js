// Fechas

const today = new Date()
console.log(today);

//Extraccion 
//año
console.log(today.getFullYear());

//Mes
console.log(today.getMonth());

//Dia
console.log(today.getDay()); //d dia de la semana
console.log(today.getDate());

//hora
console.log(today.getHours());

//time
console.log(today.getTime());

// Formateo de la fecha

console.log(today.toString());
console.log(today.toDateString());
console.log(today.toTimeString());
console.log(today.toLocaleString());
console.log(today.toLocaleDateString());
console.log(today.toLocaleTimeString());

const fechaFutura = new Date("2030-08-02")
console.log(fechaFutura);