// idioma.js (módulo ES)
// Función para cargar las traducciones desde un archivo JSON
async function loadTranslations(lang) {
    try {
        const response = await fetch(`js/${lang}.json`);
        if (!response.ok) throw new Error('No se pudo cargar el archivo de traducción');
        const translations = await response.json();
        return translations;
    } catch (error) {
        console.error('Error al cargar las traducciones:', error);
        // Si no se puede cargar el idioma solicitado, intentar cargar español como fallback
        if (lang !== 'es') {
            try {
                const fallbackResponse = await fetch('js/es.json');
                if (fallbackResponse.ok) {
                    return await fallbackResponse.json();
                }
            } catch (e) {
                console.error('Error al cargar el idioma de respaldo:', e);
            }
        }
        return {};
    }
}

// Función para actualizar los textos de la página con las traducciones
async function updateTexts(lang) {
    try {
        const translations = await loadTranslations(lang);
        if (Object.keys(translations).length === 0) throw new Error('Traducciones no encontradas');

        // Actualizar elementos con atributo data-i18n
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (!key) return;
            const translation = translations[key];
            if (translation) {
                // Si existe una función de sanitización, usarla
                if (window.seguridad?.sanitize?.text) {
                    el.textContent = window.seguridad.sanitize.text(translation);
                } else {
                    el.textContent = translation;
                }
            }
        });

        // Actualizar atributos alt de imágenes con data-i18n-alt
        document.querySelectorAll('[data-i18n-alt]').forEach(el => {
            const key = el.getAttribute('data-i18n-alt');
            if (!key) return;
            const translation = translations[key];
            if (translation) {
                el.setAttribute('alt', translation);
            }
        });

        // Manejar grupos de idiomas (si existen)
        document.querySelectorAll('[data-i18n-group]').forEach(group => {
            ['es', 'en', 'ca'].forEach(l => {
                const el = group.querySelector(`[data-i18n="${group.getAttribute('data-i18n-group')}.${l}"]`);
                if (el) el.style.display = (l === lang ? 'block' : 'none');
            });
        });
    } catch (error) {
        console.error('Error al actualizar textos:', error);
    }
}

// Función para cambiar el idioma de la página
async function setLanguage(lang) {
    try {
        // Validar que el idioma sea uno de los soportados
        if (!['es', 'en', 'ca'].includes(lang)) {
            console.warn(`Idioma no soportado: ${lang}. Usando español como predeterminado.`);
            lang = 'es';
        }
        
        // Actualizar el atributo lang del documento
        document.documentElement.lang = lang;

        // Guardar el idioma seleccionado en localStorage o en seguridad.storage
        if (window.seguridad?.storage?.set) {
            window.seguridad.storage.set('language', lang);
        } else {
            localStorage.setItem('language', lang);
        }

        // Actualizar clases active en elementos con data-lang
        document.querySelectorAll('[data-lang]').forEach(el => {
            el.classList.remove('active', 'active-inline');
            if (el.getAttribute('data-lang') === lang) {
                el.classList.add((el.tagName === 'A' || el.tagName === 'SPAN') ? 'active-inline' : 'active');
            }
        });

        // Actualizar atributos aria-pressed en botones de idioma
        document.querySelectorAll('.language-switch').forEach(btn => {
            const isSelected = btn.getAttribute('data-lang-switch') === lang;
            btn.setAttribute('aria-pressed', isSelected.toString());
        });

        // Actualizar los textos con el idioma seleccionado
        await updateTexts(lang);
        
        // Anunciar el cambio de idioma para lectores de pantalla
        const announcement = document.createElement('div');
        announcement.setAttribute('aria-live', 'polite');
        announcement.setAttribute('role', 'status');
        announcement.className = 'sr-only';
        
        let langName = '';
        switch(lang) {
            case 'es': langName = 'Español'; break;
            case 'en': langName = 'Inglés'; break;
            case 'ca': langName = 'Catalán'; break;
        }
        
        announcement.textContent = `Idioma cambiado a ${langName}`;
        document.body.appendChild(announcement);
        
        // Eliminar el anuncio después de unos segundos
        setTimeout(() => {
            document.body.removeChild(announcement);
        }, 3000);
        
        // Disparar un evento personalizado para notificar que el idioma ha cambiado
        document.dispatchEvent(new CustomEvent('languageChanged', { detail: { language: lang } }));
    } catch (err) {
        console.error('Error al establecer idioma:', err);
    }
}

// Función para inicializar el sistema de idiomas
function initIdioma() {
    // Obtener el idioma guardado o usar español como predeterminado
    const saved = window.seguridad?.storage?.get?.('language') ?? localStorage.getItem('language') ?? 'es';
    const lang = ['es', 'en', 'ca'].includes(saved) ? saved : 'es';
    
    // Establecer el idioma inicial
    setLanguage(lang);

    // Añadir event listeners a botones de cambio de idioma
    document.querySelectorAll('.language-switch').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const lang = btn.getAttribute('data-lang-switch');
            setLanguage(lang);
        });
        
        // Asegurar que los botones sean accesibles con teclado
        btn.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                const lang = btn.getAttribute('data-lang-switch');
                setLanguage(lang);
            }
        });
    });

    // Configurar selector de idioma si existe
    const select = document.getElementById('languageSelect');
    if (select) {
        select.value = lang;
        select.addEventListener('change', (e) => setLanguage(e.target.value));
    }
    
    // Añadir clase sr-only para elementos solo para lectores de pantalla
    const style = document.createElement('style');
    style.textContent = `
        .sr-only {
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip: rect(0, 0, 0, 0);
            white-space: nowrap;
            border: 0;
        }
    `;
    document.head.appendChild(style);
}

// Exportar las funciones que se usarán en otros módulos
export { initIdioma, setLanguage, loadTranslations };
