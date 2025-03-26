// ACCESO AL DOM

// obtener acceso al elemento
const h1 = document.querySelector("h1");

// obtener la información a partir del acceso
console.log(h1.textContent);

// Cómo cambiar el contenido del texto
h1.textContent = "Título principal cambiado";

function cambiaH1() {
  alert("Has hecho clic en el h1");
}

// Sistema 2
const h2 = document.querySelector("h2");

h2.onclick = () => {
  h2.style.color = "red";
};
h2.ondblclick = () => {
  h2.style.fontSize = "64px";
};

// Sistema 3
const h3 = document.querySelector("h3");

h3.addEventListener("click", () => {
  h3.style.backgroundColor = "darkgreen";
  alert(h3.textContent);
  h3.style.color = "white";
});

// Selección múltiple
const parrafos = document.querySelectorAll("p");
console.log(`Hay ${parrafos.length} nodos p`);

let ponteAzul = true;
for (let i = 0; i < parrafos.length; i++) {
  parrafos[i].addEventListener("click", () => {
    if (ponteAzul) {
      parrafos[i].style.backgroundColor = "steelblue";
      parrafos[i].style.color = "white";
      ponteAzul = false
    } else {
      parrafos[i].style.backgroundColor = "white";
      parrafos[i].style.color = "black";
      ponteAzul = true
    }
  });
}

const div = document.querySelector("div")

div.addEventListener("click", () => {
    div.innerHTML = "<h2>Soy un h2 nuevo</h2>"
})

// Otros eventos
// Cuando el cursor se pone encima del elemento seleccionado
h1.addEventListener("mouseover", () => {
    h1.style.backgroundColor = "tomato"
    h1.style.color = "white" 
})
// Cuando el cursor se pone fuera del elemento seleccionado
h1.addEventListener("mouseout", () => {
    h1.style.backgroundColor = "black"
    h1.style.color = "white" 
})