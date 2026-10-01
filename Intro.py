import streamlit as st
from PIL import Image
import os

# 1. Configuración inicial de la página
st.set_page_config(
    page_title="Portafolio de IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inyección de CSS para quitar el arcoíris y usar tema Azul
st.markdown("""
    <style>
    /* Cambiar la barra superior de Streamlit (arcoíris) a un gradiente azul moderno */
    [data-testid="stDecoration"] {
        background-image: linear-gradient(90deg, #00416A, #E4E5E6);
        background: linear-gradient(90deg, #0052D4, #4364F7, #6FB1FC);
    }
    /* Hacer que todas las líneas separadoras sean de color azul */
    hr {
        border-bottom: 2px solid #4364F7 !important;
    }
    /* Estilizar sutilmente los botones de enlace */
    .stLinkButton > a {
        border-color: #4364F7 !important;
        color: #0052D4 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Base de datos con descripciones extendidas y coherentes
APLICACIONES = [
    {
        "titulo": "Detección de Objetos",
        "imagen": "a01.jpg",
        "descripcion": "Esta aplicación utiliza redes neuronales convolucionales para identificar y localizar múltiples objetos dentro de una imagen en tiempo real, trazando cajas delimitadoras con sus respectivas etiquetas y niveles de confianza.",
        "url": "https://yolov5-mr9nwahshc8eeaermea35t.streamlit.app/",
        "categoria": "Visión por Computadora",
        "modelo": "Computer Vision / YOLO"
    },
    {
        "titulo": "WordCloud Studio",
        "imagen": "a02.jpg",
        "descripcion": "Genera nubes de palabras dinámicas a partir de textos extensos. Esta herramienta de procesamiento de lenguaje natural resalta los términos más frecuentes, facilitando el análisis visual rápido de grandes volúmenes de datos textuales.",
        "url": "https://wordcloud-dtkdpdkeljazdz2fuavsro.streamlit.app/",
        "categoria": "Procesamiento de Lenguaje",
        "modelo": "NLP / Data Viz"
    },
    {
        "titulo": "Traductor Neuronal",
        "imagen": "a03.jpg",
        "descripcion": "Rompe las barreras del idioma con esta herramienta de traducción automática. Capaz de interpretar y convertir texto entre múltiples idiomas con alta precisión, conservando el contexto y la semántica original de las oraciones.",
        "url": "https://traductor-gehpghvr9q3edfajue3bwb.streamlit.app/",
        "categoria": "Procesamiento de Lenguaje",
        "modelo": "Sequence-to-Sequence"
    },
    {
        "titulo": "Demo TF-IDF en Español",
        "imagen": "a04.jpg",
        "descripcion": "Descubre la relevancia de las palabras en tus documentos. Esta aplicación implementa el algoritmo TF-IDF para extraer conceptos clave y analizar la importancia relativa de los términos en un corpus específico de textos en español.",
        "url": "https://tdfesp-xurouaqeyqepm4whrlpzwy.streamlit.app/",
        "categoria": "Procesamiento de Lenguaje",
        "modelo": "Information Retrieval"
    },
    {
        "titulo": "Análisis de Sentimiento",
        "imagen": "a05.jpg",
        "descripcion": "Evalúa el tono emocional detrás de las palabras. Esta herramienta clasifica textos según su polaridad (positiva, negativa o neutral), siendo ideal para analizar opiniones de usuarios o interacciones masivas en redes sociales.",
        "url": "https://sentimenta-mcwscyx7txyocfmduonoe6.streamlit.app/",
        "categoria": "Procesamiento de Lenguaje",
        "modelo": "Clasificación de Texto"
    },
    {
        "titulo": "Traductor de Imágenes",
        "imagen": "a06.jpg",
        "descripcion": "Combina tecnología OCR con modelos de traducción automática. Al subir una imagen que contenga texto en otro idioma, la aplicación extrae los caracteres procesables y los traduce instantáneamente a tu idioma de preferencia.",
        "url": "https://ocr-audio-33nfniq7a3tpyftdjgko4k.streamlit.app/",
        "categoria": "Visión por Computadora",
        "modelo": "OCR + Translation"
    },
    {
        "titulo": "Reconocimiento Óptico (OCR)",
        "imagen": "a07.jpg",
        "descripcion": "Digitaliza texto impreso o escrito con facilidad. Esta herramienta extrae la información contenida en imágenes o documentos escaneados, transformándolos en texto completamente editable mediante algoritmos de visión artificial.",
        "url": "https://5bo3dkbndniywucgnecrzc.streamlit.app/",
        "categoria": "Visión por Computadora",
        "modelo": "Optical Character Recognition"
    },
    {
        "titulo": "Agente de IA",
        "imagen": "a08.jpg",
        "descripcion": "Interactúa con un asistente virtual impulsado por modelos de lenguaje grande (LLM). Este agente está diseñado para comprender intenciones, mantener el contexto de la conversación y resolver consultas complejas de manera natural.",
        "url": "https://juanitakush-xwdjdbylj9wl9nttmyc6gl.streamlit.app/",
        "categoria": "Asistentes Virtuales",
        "modelo": "LLM / Conversational"
    },
    {
        "titulo": "Mi Primera App IA",
        "imagen": "a09.jpg",
        "descripcion": "Un espacio de experimentación y prueba de conceptos básicos. Aquí se exploran integraciones iniciales de modelos de machine learning y estructuras de interfaz, sentando las bases para aplicaciones interactivas más robustas.",
        "url": "https://ilydbjwqwuydndt4dyagxj.streamlit.app/",
        "categoria": "Otros",
        "modelo": "Prototipo Base"
    }
]

# Función para cargar imágenes de forma segura
def cargar_imagen(ruta):
    try:
        if os.path.exists(ruta):
            img = Image.open(ruta)
            # use_container_width hace que la imagen se adapte perfectamente al ancho de la caja
            st.image(img, use_container_width=True)
        else:
            st.info(f"🖼️ Espacio para imagen: {ruta}")
    except Exception:
        st.error("Error al cargar la imagen.")

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("🤖 Explorador de IA")
    
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real."
    )
    st.info(parrafo)
    
    st.divider()
    
    st.subheader("Filtros de Búsqueda")
    categorias_unicas = ["Todas"] + list(set(app["categoria"] for app in APLICACIONES))
    categoria_seleccionada = st.selectbox("Selecciona una categoría:", categorias_unicas)

# --- CONTENIDO PRINCIPAL ---
# 1. Banner Superior (Usa una imagen existente, luego la puedes cambiar)
cargar_imagen("a1.jpg")

st.title("Hub de Aplicaciones Inteligentes")
st.markdown("Explora el potencial del Machine Learning a través de estas herramientas interactivas.")

# 2. Panel de Métricas (Le da un aspecto muy pro/dashboard)
col_m1, col_m2, col_m3 = st.columns(3)
col_m1.metric("Aplicaciones Activas", len(APLICACIONES))
col_m2.metric("Estado del Sistema", "Online 🟢")
col_m3.metric("Última Actualización", "Hoy")

st.divider()

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.success(f"📚 **Recurso destacado:** En el siguiente enlace puedes encontrar más documentación y ejercicios prácticos. [Ir al sitio web]({url_ia})")

# --- RENDERIZADO DE LAS TARJETAS (CUADROS UNIFORMES) ---
apps_filtradas = APLICACIONES
if categoria_seleccionada != "Todas":
    apps_filtradas = [app for app in APLICACIONES if app["categoria"] == categoria_seleccionada]

if not apps_filtradas:
    st.warning("No se encontraron aplicaciones en esta categoría.")
else:
    # Agrupamos en pestañas para mayor orden (opcional, pero se ve muy bien)
    tab1, tab2 = st.tabs(["Vista de Cuadrícula", "Vista de Lista"])
    
    with tab1:
        columnas = st.columns(3)
        for index, app in enumerate(apps_filtradas):
            col = columnas[index % 3]
            
            with col:
                # height=530 asegura que todas las cajas midan exactamente lo mismo
                # Si el texto es más largo, Streamlit pone un scroll interno muy sutil
                with st.container(border=True, height=530):
                    st.subheader(app["titulo"])
                    st.caption(f"⚙️ {app['modelo']}") # Agrega la etiqueta técnica
                    cargar_imagen(app["imagen"])
                    st.write(app["descripcion"])
                    st.link_button("Abrir aplicación ↗", app["url"], use_container_width=True)
                    
    with tab2:
        # Una vista alternativa simple por si el usuario prefiere leer en lista
        for app in apps_filtradas:
            with st.container(border=True):
                st.markdown(f"### {app['titulo']} - `{app['modelo']}`")
                st.write(app["descripcion"])
                st.link_button("Acceder ↗", app["url"])
