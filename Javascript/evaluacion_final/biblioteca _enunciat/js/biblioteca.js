// localStorage.removeItem("biblioteca")

// MINI BIBLIOTECA

// const biblioteca = JSON.parse(localStorage.getItem("biblioteca")) || [
const biblioteca = JSON.parse(localStorage.getItem("biblioteca")) || [
    { titulo: "Guerra y Paz", autor: "Lev Tolstoi", categoria: "drama", idioma: "español", epoca: "s.XIX" },
    { titulo: "Anna Karenina", autor: "Lev Tolstoi", categoria: "drama", idioma: "català", epoca: "s.XIX" },
    { titulo: "L'Odisea", autor: "Homero", categoria: "drama", idioma: "català", epoca: "clásica" },
    { titulo: "Antologia de la poesia medieval catalana", autor: "Diversos", categoria: "poesia", idioma: "català", epoca: "clásica" },
    { titulo: "La Ilíada", autor: "Homero", categoria: "drama", idioma: "español", epoca: "clásica" },
    { titulo: "Poema del Mio Cid", autor: "Anónimo", categoria: "poesia", idioma: "español", epoca: "clásica" },
    { titulo: "Veinte mil leguas de viaje submarino", autor: "Jules Verne", categoria: "aventuras", idioma: "español", epoca: "s.XIX" },
    { titulo: "De la Terra a la Lluna", autor: "Jules Verne", categoria: "aventuras", idioma: "català", epoca: "s.XIX" },
    { titulo: "Cinco semanas en globo", autor: "Jules Verne", categoria: "aventuras", idioma: "español", epoca: "s.XIX" },
    { titulo: "Robinson Crusoe", autor: "Daniel Defoe", categoria: "aventuras", idioma: "català", epoca: "clásica" },
    { titulo: "Germinal", autor: 'Émile Zola', categoria: "drama", idioma: "español", epoca: "s.XIX" },
    { titulo: "Notre Dame de Paris", autor: 'Victor Hugo', categoria: "drama", idioma: "català", epoca: "s.XIX" },
    { titulo: "Los Miserables", autor: 'Victor Hugo', categoria: "drama", idioma: "español", epoca: "s.XIX" },
    { titulo: "Yo, robot", autor: "Isaac Asimov", categoria: "ciencia-ficción", idioma: "español", epoca: "s.XX" },
    { titulo: "Fundació", autor: "Isaac Asimov", categoria: "ciencia-ficción", idioma: "català", epoca: "s.XX" },
    { titulo: "Ciberiada", autor: "Stanislaw Lem", categoria: "ciencia-ficción", idioma: "español", epoca: "s.XX" },
    { titulo: "Solaris", autor: "Stanislaw Lem", categoria: "ciencia-ficción", idioma: "català", epoca: "s.XX" },
    { titulo: "El hombre bicentenario", autor: "Isaac Asimov", categoria: "ciencia-ficción", idioma: "español", epoca: "s.XX" },
    { titulo: "Tokio Blues", autor: "Haruki Murakami", categoria: "drama", idioma: "español", epoca: "s.XX" },
    { titulo: "Romancero Gitano", autor: "Federico García Lorca", categoria: "poesia", idioma: "español", epoca: "s.XX" },
    { titulo: "Los aventuras de Sherlock Holmes", autor: 'Arthur Conan Doyle', categoria: "misterio", idioma: "español", epoca: "s.XIX" },
    { titulo: "Rebelió a la granja", autor: 'George Orwell', categoria: "drama", idioma: "català", epoca: "s.XX" },
    { titulo: "La Divina Comedia", autor: "Dante Alighieri", categoria: "drama", idioma: "español", epoca: "clásica" },
    { titulo: "Fahrenheit 451", autor: "Ray Bradbury", categoria: "ciencia-ficción", idioma: "català", epoca: "s.XX" },
    { titulo: "Cròniques Marcianes", autor: "Ray Bradbury", categoria: "ciencia-ficción", idioma: "català", epoca: "s.XX" },
]





// ==========================================================================================================
// EJERCICIO 1
// Libros disponibleS
// Mostrar la lista de obras alfabéticamente según el título, en forma de lista ordenada

// Llista del llibres
// const listaLibros = document.getElementById("listaLibros");

// Declaracion de la constante Ejercicio 1
const ejer1 = document.getElementById('ejer1')

biblioteca.sort((a, b) => { // Ordenar la biblioteca por el título del libro 
    return a.titulo.localeCompare(b.titulo, "es-ES", { numeric: true }); // Comparar los títulos de los libros
});
  
                                                            // Metodo 1
/* for (let i = 0; i < biblioteca.length; i++) { // Recorrer la biblioteca y mostrar los datos de los libros en el div ejer1 
  if (biblioteca[i].titulo) {  // Si el libro tiene título mostrar los datos del libro  
    let mensaje = `<p>Titulo: ${biblioteca[i].titulo}, Autor ${biblioteca[i].autor},
     Categoria ${biblioteca[i].categoria}, Idioma: ${biblioteca[i].idioma}, Epoca: ${biblioteca[i].epoca} <br></p>`; // Mensaje de los datos del libro que se van a mostrar 
    ejer1.innerHTML += mensaje;   
}
} */

                                                            // Metodo 2
// Crear una función que muestre la biblioteca
function mostrarBiblioteca(id){ // id es el div donde se mostrará la biblioteca
    let html = '<ul>' // Crear una lista ordenada para mostrar los libros de la biblioteca 
    biblioteca.forEach((libro)=>{ // Recorrer la biblioteca y por cada libro mostrar los datos del libro en una lista 
      html +=`<li> Titulo: ${libro.titulo}, Autor: ${libro.autor},
     Categoria: ${libro.categoria}, Idioma: ${libro.idioma}, Epoca: ${libro.epoca}</li>`  // Mensaje de los datos del libro que se van a mostrar 
    })
    html += "</ul>" // Cerrar la lista ordenada 
    id.innerHTML = html // Mostrar la lista ordenada en el div que se ha pasado como parámetro
    }
    mostrarBiblioteca(ejer1) // Llamar a la función mostrarBiblioteca y pasarle el div ejer1 como parámetro para mostrar la biblioteca en el div ejer1 


// ==========================================================================================================
// EJERCICIO 2
// Filtrar las obras según los criterios indicados en el formulario.
// Las obras que cumplan las condiciones se mostrarán dentro del div con id salidaFiltrada
// Las obras se mostrarán según aparece en la imagen modelo1.png
// Hay que aplicar algunos estilos que ya están definidos en el css

// Declaracion de las constantes Ejercicio 2
const form_filtrado = document.forms['form-filtrado'];
const ejer2 = document.getElementById('ejer2');

// Crear una función que muestre la biblioteca filtrada según los criterios del formulario 

form_filtrado.addEventListener('change', () => { // Añadir un evento change al formulario form_filtrado para que cuando cambie algún valor del formulario se ejecute la función 
    const categoria = form_filtrado.categoria.value; // Obtener el valor de la categoría seleccionada en el formulario 
    const idioma = form_filtrado.idioma.value; // Obtener el valor del idioma seleccionado en el formulario
    const epoca = form_filtrado.epoca.value; // Obtener el valor de la época seleccionada en el formulario
    
    mensajeEj2(ejer2, categoria, idioma, epoca); // Llamar a la función mensajeEj2 y pasarle los parámetros ejer2, categoria, idioma y epoca para mostrar la biblioteca filtrada en el div ejer2
});

function mensajeEj2(id, categoria, idioma, epoca) { // Crear una función mensajeEj2 que mostrará la biblioteca filtrada según los criterios del formulario 
    let html = "<ul>"; // Crear una lista no ordenada para mostrar los libros de la biblioteca que cumplen los criterios del formulario 
    let stockBiblioteca = 0; // Crear una variable stockBiblioteca que se inicializa a 0 para contar los libros que cumplen los criterios del formulario 
    
    biblioteca.forEach((libro) => {  // Recorrer la biblioteca y por cada libro comprobar si cumple los criterios del formulario
    if (libro.categoria === categoria && libro.idioma === idioma && libro.epoca === epoca) { // Si el libro cumple los criterios del formulario mostrar los datos del libro en una lista
        html += `<li> <span class="autor">${libro.autor}</span>: <span class="obra">${libro.titulo}</span> (<span class="#">${libro.categoria}</span>), ${libro.idioma}</li>`; // Mensaje de los datos del libro que se van a mostrar
        stockBiblioteca++; // Incrementar el contador de libros que cumplen los criterios del formulario
    }
    });

    html += '</ul>'; // Cerrar la lista no ordenada
    
    if (stockBiblioteca === 0) { // Si no hay ningún libro que cumpla los criterios del formulario mostrar un mensaje de que no hay libros que cumplan los criterios
    html = '<p>No hay ningun libro que cumpla las condiciones.</p>'; // Mensaje de que no hay libros que cumplan los criterios del formulario
    }

    id.innerHTML = html; // Mostrar la lista no ordenada en el div que se ha pasado como parámetro 
}


// ==========================================================================================================
// EJERCICIO 3
// Filtrar por autor
// Selección de obras según el nombre o parte del nombre de un autor.
// Al hacer clic sobre el botón buscar se mostrarán las obras cuyos autores cumplen los requisitos.
// La salida por pantalla será en este formato:
// Isaac Asimov : Yo, robot (ciencia-ficción, idioma : español, época : s.XX) 


// Filtrar por autor
// Selección de obras según el nombre o parte del nombre de un autor.
// Al hacer clic sobre el botón buscar se mostrarán las obras cuyos autores cumplen los requisitos.
// La salida por pantalla será en este formato:
// Isaac Asimov : Yo, robot (ciencia-ficción, idioma : español, época : s.XX) 

// Declaracion de constantes Ejercicio 3
const form_autor = document.forms['form-autor'];
const ejer3 = document.getElementById('ejer3');

// Creacion de una funcion segun el evento submit del formulario form_autor al buscar el autor
form_autor.addEventListener("submit", (e) => { // Añadir un evento submit al formulario form_autor para que cuando se envíe el formulario se ejecute la función 
  e.preventDefault(); // Prevenir el envío del formulario
  const autor = form_autor.autor.value.trim().toLowerCase(); // Obtener el valor del autor introducido en el formulario y convertirlo a minúsculas
  let html = "<ul>"; // Crear una lista no ordenada para mostrar los libros de la biblioteca que cumplen los criterios del formulario
  biblioteca.forEach((libro) => { // Recorrer la biblioteca y por cada libro comprobar si el autor cumple los criterios del formulario
    if (libro.autor.toLowerCase().includes(autor)) { // Compara por si se ingresa solo una parte del nombre del autor
      html += `<li>${libro.autor}: ${libro.titulo} (${libro.categoria}, idioma: ${libro.idioma}, época: ${libro.epoca}).</li>`; // Mensaje de los datos del libro que se van a mostrar
    }
  });
  html += "</ul>"; // Cerrar la lista no ordenada
  if (html === "<ul></ul>") { // Si el htlm esta igual a "<ul></ul>" mostrar un mensaje de que no se encontraron libros que coincidan con ese autor
    html = "<p>No se encontraron libros que coincidan con ese autor.</p>"; // Mensaje de que no se encontraron libros que coincidan con ese autor
  }
  ejer3.innerHTML = html; // Mostrar la lista no ordenada en el div ejer3
});

// ==========================================================================================================
// EJERCICIO 4
// Añadir obra a la biblioteca
// A partir del formulario, añadir obras a la biblioteca
// Conseguir permanencia con LocalStorage
// Actualizar automáticamente el listado de obras del ejercicio 1

// Obtener el formulario de inclusión de obra
const incluirObra = document.forms['incluirObra'];


// Evento para manejar la inclusión de una nueva obra
incluirObra.addEventListener('submit', (e) => {
    e.preventDefault();  // Prevenir el comportamiento por defecto del formulario
    // Obtenemos los valores de los campos del formulario usando sus IDs
    const autor = document.getElementById('incluir-autor').value.trim(); // Obtener el valor del autor introducido en el formulario y convertirlo a minúsculas
    const titulo = document.getElementById('incluir-titulo').value.trim(); // Obtener el valor del título introducido en el formulario y convertirlo a minúsculas
    const categoria = document.getElementById('incluir-categoria').value.trim(); // Obtener el valor de la categoría introducida en el formulario y convertirlo a minúsculas
    const idioma = document.getElementById('incluir-idioma').value.trim(); // Obtener el valor del idioma introducido en el formulario y convertirlo a minúsculas
    const epoca = document.getElementById('incluir-epoca').value.trim(); // Obtener el valor de la época introducida en el formulario y convertirlo a minúsculas
    if (autor && titulo && categoria && idioma && epoca) { // Comprobamos que todos los campos del formulario estén completos antes de enviar la obra a la biblioteca
        biblioteca.push({ titulo, autor, categoria, idioma, epoca }); // Agregamos la nueva obra al array de la biblioteca 
        localStorage.setItem('biblioteca', JSON.stringify(biblioteca)); // Actualizamos el LocalStorage con la nueva obra incluida en la biblioteca 
        mostrarBiblioteca(ejer1); // Mostramos la biblioteca actualizada en el div ejer1 
        incluirObra.reset(); // Reseteamos el formulario de inclusión de obra
        alert('Obra añadida correctamente.'); // Mostramos un mensaje de que la obra se ha añadido correctamente
    } else {
        alert('Por favor, complete todos los campos antes de enviar.'); // Si no se han completado todos los campos del formulario mostrar un mensaje de que se deben completar todos los campos antes de enviar
    }
});
mostrarBiblioteca(ejer1); // Mostrar la biblioteca en el div ejer1

// ==========================================================================================================
// EJERCICIO 5
// Quitar obras de la biblioteca. Crea en un formulario una etiqueta select con las obras de la biblioteca.
// Al seleccionar una obra y enviar el formulario, se eliminará la obra de la biblioteca.
// Actualizar automáticamente el listado de obras del ejercicio 1
// Actualizar el LocalStorage

// Declaracion de constantes Ejercicio 5
const formQuitarObra = document.forms['formQuitarObra'];
const selectQuitarObra = document.getElementById('selectQuitarObra');

// Función para cargar las obras en el select y ordenarlas alfabéticamente por título
function cargarSelectQuitarObra() {
    selectQuitarObra.innerHTML = ''; // Limpiar el select antes de llenarlo con las opciones
    const defaultOption = document.createElement('option');
    defaultOption.textContent = 'Selecciona una obra para eliminar';
    defaultOption.disabled = true;
    defaultOption.selected = true;
    selectQuitarObra.appendChild(defaultOption);
    const bibliotecaOrdenada = [...biblioteca].sort((a, b) => { // Ordenar la biblioteca por título alfabéticamente
        return a.titulo.localeCompare(b.titulo, "es-ES", { numeric: true }); // Comparar los títulos de los libros para ordenarlos 
    });
    bibliotecaOrdenada.forEach((libro, index) => { // Recorrer la biblioteca ordenada y agregar las opciones al select
        const option = document.createElement('option'); // Crear una opción para el select
        option.value = index; // Guardamos el índice de la obra como el valor
        option.textContent = `${libro.autor}: ${libro.titulo}`; // Mostrar el autor y el título de la obra
        selectQuitarObra.appendChild(option); // Añadir la opción al select
    });
}

// Evento para eliminar una obra seleccionada
formQuitarObra.addEventListener('submit', (e) => {
    e.preventDefault(); // Prevenir el comportamiento por defecto del formulario
    const index = selectQuitarObra.value; // Obtener el índice de la obra seleccionada
    if (index !== "") { // Comprobar si se ha seleccionado una obra
        biblioteca.splice(index, 1); // Eliminar la obra seleccionada de la biblioteca
        localStorage.setItem('biblioteca', JSON.stringify(biblioteca)); // Actualizar el LocalStorage con la nueva biblioteca
        cargarSelectQuitarObra(); // Recargar las opciones del select
        mostrarBiblioteca(ejer1); // Actualizar el listado de la biblioteca en el div ejer1
        alert('Obra eliminada correctamente.'); // Mostrar mensaje de éxito
    } else {
        alert('Por favor, selecciona una obra para eliminar.'); // Si no se seleccionó ninguna obra, mostrar un mensaje
    }
});
mostrarBiblioteca(ejer1);
cargarSelectQuitarObra();