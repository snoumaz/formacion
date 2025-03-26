let num = 2;
let saludo = "hola";
console.log(saludo + num);
console.log(num + saludo);
let palabraConcatenada = "         " + "con" + "ca" + "te" + "nar";
let numString = "5";
console.log(numString - num);

console.log(palabraConcatenada);
palabraConcatenada[0] = "C";
console.log(palabraConcatenada);

// Estructura del for:
// for (inicio; final; paso) { bloque de código a utilizar }
for (let i = 0; i < palabraConcatenada.length; i++) {
  console.log(`${i}. ${palabraConcatenada[i]}`);
}

console.log(palabraConcatenada.toLocaleUpperCase());
console.log(palabraConcatenada.toLocaleLowerCase());
console.log("La variable palabraConcatenda mide", palabraConcatenada.length);
palabraConcatenada = palabraConcatenada.trim();
console.log("La variable palabraConcatenda mide", palabraConcatenada.length);
let inicial = palabraConcatenada.at(0);
console.log(inicial);

let lista = [1, "w", [4, "t", palabraConcatenada], false];

for (let i = 0; i < lista.length; i++) {
  console.log(typeof lista[i]);
}

let texto = "Hoy es lunes".split(" ");
console.log(texto);

console.log(palabraConcatenada.slice(1, 3));

let nombre = "    mArIA De LoS angELes     "; // Maria de los Angeles
// nombre = "     jOsE mArIA de los saNTOs peREz                   "

nombre = nombre.trim();
console.log(nombre);
nombre = nombre.split(" ");
console.log(nombre);

let nombreCorregido = "";
let listaPalabrasNombre = [];

for (let i = 0; i < nombre.length; i++) {
  // Obtener la inicial y pasarla a mayúsculas
  let inicial = nombre[i].at(0).toLocaleUpperCase();
  console.log(inicial);
  // Obtenemos el resto de las letras
  let restoNombre = nombre[i].slice(1).toLocaleLowerCase();
  console.log(restoNombre);
  // Reconstruir el nombre
  let nombreFinal = inicial + restoNombre;
  console.log(nombreFinal);
  if (
    nombreFinal == "De" ||
    nombreFinal == "Los" ||
    nombreFinal == "La" ||
    nombreFinal == "El" ||
    nombreFinal == "Las"
  ) {
    nombreFinal = nombreFinal.toLocaleLowerCase();
  }
  console.log(nombreFinal);

  listaPalabrasNombre.push(nombreFinal);
  console.log(listaPalabrasNombre);

  // acumular las palabras
  //   nombreCorregido += nombreFinal + " "
}
nombreCorregido = listaPalabrasNombre.join(" ");
// nombreCorregido = listaPalabrasNombre.toString().replaceAll(",", " ")
console.log(nombreCorregido);

// nombreCorregido = nombreCorregido.trim()
// console.log(nombreCorregido);

let fecha = "9/3/2025"; // "2025-03-10" "AAAA-MM-DD"

// Separar los valores
fecha = fecha.split("/");
console.log(fecha);

for (let i = 0; i <= 1; i++) {
  if (fecha[i].length == 1) {
    fecha[i] = "0" + fecha[i];
  }
}
console.log(fecha);
fecha = fecha[2] + "-" + fecha[1] + "-" + fecha[0];
console.log(fecha);
