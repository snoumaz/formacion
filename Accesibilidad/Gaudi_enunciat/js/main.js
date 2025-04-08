import { initIdioma, setLanguage } from './idioma.js';

document.addEventListener('DOMContentLoaded', async () => {
    // Inicializar el sistema de idiomas
    initIdioma();
    
    // Cargar datos desde el JSON
    try {
        const response = await fetch('js/es.json');
        const data = await response.json();
        updateContent(data);
    } catch (error) {
        console.error('Error cargando el archivo JSON:', error);
    }

    // Opcional: cambiar idioma desde botones con clase .change-lang
    document.querySelectorAll('.change-lang').forEach(button => {
        button.addEventListener('click', (event) => {
            const lang = event.target.getAttribute('data-lang');
            if (lang) {
                setLanguage(lang);
            }
        });
    });
});

// Actualizar el contenido de la página con los datos del JSON
function updateContent(data) {
    // Actualizar elementos con atributo data-i18n
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (data[key]) {
            element.textContent = data[key];
        }
    });
    
    // Actualizar atributos alt de imágenes con data-i18n-alt
    document.querySelectorAll('[data-i18n-alt]').forEach(element => {
        const key = element.getAttribute('data-i18n-alt');
        if (data[key]) {
            element.setAttribute('alt', data[key]);
        }
    });
}

// Función para añadir un selector de idioma a la página
export function addLanguageSelector(containerId, languages) {
    const container = document.getElementById(containerId);
    if (!container) return;
    
    const select = document.createElement('select');
    select.id = 'languageSelect';
    select.className = 'language-selector';
    
    languages.forEach(lang => {
        const option = document.createElement('option');
        option.value = lang.code;
        option.textContent = lang.name;
        select.appendChild(option);
    });
    
    select.addEventListener('change', (e) => setLanguage(e.target.value));
    container.appendChild(select);
    
    // Establecer el valor inicial basado en el idioma actual
    const currentLang = document.documentElement.lang || 'es';
    select.value = currentLang;
}