import key from './appikey.js';

console.log(key);
const api = key;
const form = document.getElementById('weatherForm');
const divDatos = document.getElementById('divDatos');

form.addEventListener('submit', (event) => {
    event.preventDefault();

    const ciudad = document.getElementById('city').value.trim();
    const idioma = document.getElementById('language').value;

    // Validación de entrada
    if (!ciudad) {
        divDatos.innerHTML = `<p>Error: Por favor, ingrese una ciudad válida.</p>`;
        return;
    }

    // Limpiar contenido previo
    divDatos.innerHTML = `<p>Cargando datos...</p>`;

    const url = `https://api.openweathermap.org/data/2.5/weather?appid=${api}&units=metric&lang=${idioma}&q=${ciudad}`;
    const url2 = `https://api.openweathermap.org/data/2.5/forecast?appid=${api}&units=metric&lang=${idioma}&q=${ciudad}`;

    // Fetch para datos actuales
    fetch(url)
        .then((response) => {
            if (!response.ok) {
                throw new Error('No se pudo obtener los datos del clima actual. Verifique la ciudad ingresada.');
            }
            return response.json();
        })
        .then((data) => {
            divDatos.innerHTML = `
                <p>Ciudad: ${data.name}</p>
                <p>Temperatura actual: ${data.main.temp} °C</p>
                <p>Descripción: ${data.weather[0].description}</p>
                <div>
                    <img src="https://www.imelcf.gob.pa/wp-content/plugins/location-weather/assets/images/icons/weather-icons/${data.weather[0].icon}.svg" alt="Icono del clima" width=10%>
                </div>
            `;
        })
        .catch((error) => {
            divDatos.innerHTML = `<p>Error: ${error.message}</p>`;
        });

    // Fetch para pronóstico
    fetch(url2)
        .then((response) => {
            if (!response.ok) {
                throw new Error('No se pudo obtener los datos del pronóstico. Verifique la ciudad ingresada.');
            }
            return response.json();
        })
        .then((data) => {
            let forecastHTML = '<h3>Pronóstico extendido:</h3>';
            
            // Agrupar pronósticos por día
            const dailyForecasts = {};
            data.list.forEach(forecast => {
                const fecha = new Date(forecast.dt * 1000);
                const dia = fecha.toLocaleDateString();
                
                if (!dailyForecasts[dia]) {
                    dailyForecasts[dia] = forecast;
                }
            });

            // Mostrar solo los primeros 7 días
            Object.values(dailyForecasts).slice(0, 7).forEach(forecast => {
                const fecha = new Date(forecast.dt * 1000);
                forecastHTML += `
                    <div class="forecast-day">
                        <p>Fecha: ${fecha.toLocaleDateString()}</p>
                        <p>Temperatura: ${forecast.main.temp} °C</p>
                        <p>Descripción: ${forecast.weather[0].description}</p>
                        <img src="https://www.imelcf.gob.pa/wp-content/plugins/location-weather/assets/images/icons/weather-icons/${forecast.weather[0].icon}.svg" alt="Icono del clima" width=10%>
                    </div>
                `;
            });
            divDatos.innerHTML += forecastHTML;
        })
        .catch((error) => {
            divDatos.innerHTML += `<p>Error: ${error.message}</p>`;
        });
});