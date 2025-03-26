// como meter una funcion dentro de un objeto

let cliente = {
    nombre: "Marcos",
    apellido: "García",
    nombreCompleto: function () {
        return `${this.nombre} ${this.apellido}`;
    },

}
console.log(cliente.nombreCompleto());
console.log(cliente.nombre);
console.log(cliente.apellido);
console.log(cliente["nombre"]);
console.log(cliente["apellido"]);
console.log(cliente["nombreCompleto"]());
