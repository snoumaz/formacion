/* Vamos a trabajar para un comercio que vende toda clase de articulos,
desde los mas caros a los mas baratos. El cambio se va a devolver en metalico,
segun las siguientes reglas:
- Tienen que ser de modo exacto (en metalico)
- Tienen que ser usando la minima cantidad de billetes y monedas posibles*/
 
let cambio = 457.28;

const moneyEuros = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01];
const resultado = {};

for (let i = 0; i < moneyEuros.length; i++) {
    let money = moneyEuros[i];
    if (cambio >= money) {
        let temp = parseInt(cambio / money);
        resultado[money] = temp;
        cambio = (cambio - (temp * money)).toFixed(2);
        cambio = parseFloat(cambio); // Convertir de nuevo a número
    }
}

console.log("Cambio devuelto:");
for (let i = 0; i < moneyEuros.length; i++) {
    let money = moneyEuros[i];
    if (resultado[money]) {
        console.log(resultado[money] + " x " + money + "€");
    }
}