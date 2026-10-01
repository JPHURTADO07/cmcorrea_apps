import streamlit as st
from PIL import Image
import os

# 1. Configuración inicial de la página (Toque Pro para la pestaña del navegador y diseño)
st.set_page_config(
    page_title="Portafolio de IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Base de datos de aplicaciones (Estructura de datos limpia)
# Mantenemos intactos tus textos, enlaces y nombres de imágenes.
# Agregamos una "categoría" para la lógica de filtrado interactivo.
APLICACIONES = [
    {
        "titulo": "Detección de Objetos en Imágenes",
        "imagen": "txt_to_audio2.png",
        "descripcion": "En la siguiente enlace usaremos una de las aplicaciones de Detección de Objetos en Imágenes",
        "url": "https://yolov5-mr9nwahshc8eeaermea35t.streamlit.app/",
        "categoria": "Visión por Computadora"
    },
    {
        "titulo": "WordCloud Studio",
        "imagen": "txt_to_audio.png",
        "descripcion": "En la siguiente enlace usaremos una de las aplicaciones de WordCloud Studio.",
        "url": "https://wordcloud-dtkdpdkeljazdz2fuavsro.streamlit.app/",
        "categoria": "Procesamiento de Lenguaje"
    },
    {
        "titulo": "Traductor",
        "imagen": "OIG5.jpg",
        "descripcion": "En la siguiente enlace usaremos una de las aplicaciones de Traductor.",
        "url": "https://traductor-gehpghvr9q3edfajue3bwb.streamlit.app/",
        "categoria": "Procesamiento de Lenguaje"
    },
    {
        "titulo": "Demo TF-IDF en Español",
        "imagen": "OIG8.jpg",
        "descripcion": "En la siguiente veremos una aplicación que usa lDemo TF-IDF en Español.",
        "url": "https://tdfesp-xurouaqeyqepm4whrlpzwy.streamlit.app/",
        "categoria": "Procesamiento de Lenguaje"
    },
    {
        "titulo": "Análisis de Sentimiento",
        "imagen": "data_analisis.png",
        "descripcion": "En la siguiente enlace veremos como se pueden analizar Análisis de Sentimiento.",
        "url": "https://sentimenta-mcwscyx7txyocfmduonoe6.streamlit.app/",
        "categoria": "Procesamiento de Lenguaje"
    },
    {
        "titulo": "Traductor de Imágenes",
        "imagen": "OIG3.jpg",
        "descripcion": "En la siguiente enlace veremos como realizamos Traductor de Imágenes.",
        "url": "https://ocr-audio-33nfniq7a3tpyftdjgko4k.streamlit.app/",
        "categoria": "Visión por Computadora"
    },
    {
        "titulo": "Reconocimiento óptico de Caracteres",
        "imagen": "Chat_pdf.png",
        "descripcion": "En la siguiente veremos una aplicación que Reconocimiento óptico de Caracteres.",
        "url": "https://5bo3dkbndniywucgnecrzc.streamlit.app/",
        "categoria": "Visión por Computadora"
    },
    {
        "titulo": "Agente de IA",
        "imagen": "OIG4.jpg",
        "descripcion": "En la siguiente enlace veremos la Agente de IA.",
        "url": "https://juanitakush-xwdjdbylj9wl9nttmyc6gl.streamlit.app/",
        "categoria": "Asistentes Virtuales"
    },
    {
        "titulo": "Mi Primera App",
        "imagen": "OIG6.jpg",
        "descripcion": "En la siguiente enlace veremos la Mi Primera App.",
        "url": "https://ilydbjwqwuydndt4dyagxj.streamlit.app/",
        "categoria": "Otros"
    }
]

# Función de seguridad: Si la imagen no está en GitHub, la app no se bloquea
def cargar_imagen(ruta, ancho=200):
    try:
        if os.path.exists(ruta):
            img = Image.open(ruta)
            st.image(img, width=ancho)
        else:
            st.warning(f"Falta imagen: {ruta}")
    except Exception:
        st.error("Error visual.")

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.title("🤖 Explorador de IA")
    st.subheader("Aplicaciones con Inteligencia Artificial")
    
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    # st.info le da un cuadro de color agradable al texto
    st.info(parrafo)
    
    st.divider() # Línea visual separadora
    
    # LÓGICA AGREGADA: Filtro interactivo
    st.subheader("Filtra las aplicaciones:")
    categorias_unicas = ["Todas"] + list(set(app["categoria"] for app in APLICACIONES))
    categoria_seleccionada = st.selectbox("Selecciona una categoría para explorar:", categorias_unicas)

# --- CONTENIDO PRINCIPAL ---
st.title("🚀 Aplicaciones de Inteligencia Artificial")
st.markdown("Explora el potencial de la IA a través de estas herramientas interactivas.")

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

# st.success destaca tu enlace general para que no se pierda
st.success(f"📚 **Recurso destacado:** En el siguiente enlace puedes encontrar páginas y ejercicios prácticos. [Ir al sitio web]({url_ia})")
st.divider()

# --- RENDERIZADO LÓGICO Y DINÁMICO ---
# Filtramos la lista según lo que el usuario eligió en el sidebar
apps_filtradas = APLICACIONES
if categoria_seleccionada != "Todas":
    apps_filtradas = [app for app in APLICACIONES if app["categoria"] == categoria_seleccionada]

if not apps_filtradas:
    st.warning("No se encontraron aplicaciones en esta categoría.")
else:
    # Creamos las 3 columnas
    columnas = st.columns(3)
    
    # Repartimos las aplicaciones filtradas entre las 3 columnas automáticamente
    for index, app in enumerate(apps_filtradas):
        col = columnas[index % 3] # Lógica matemática para distribuir 0, 1, 2, 0, 1, 2...
        
        with col:
            with st.container(): # Contenedor para que visualmente actúe como una tarjeta
                st.subheader(app["titulo"])
                cargar_imagen(app["imagen"])
                st.write(app["descripcion"])
                # st.link_button crea un botón real en lugar de texto hipervinculado, se ve mucho mejor
                st.link_button(f"Abrir aplicación ↗", app["url"])
                st.markdown("---") # Separador inferior para cada app
