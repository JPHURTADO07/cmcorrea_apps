import streamlit as st
from PIL import Image
import os
import pandas as pd

# 1. Configuración inicial de la página
st.set_page_config(
    page_title="Portafolio de IA | Juan Pablo Orrego",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inyección de CSS Avanzado
st.markdown("""
    <style>
    /* Tema Azul Moderno */
    [data-testid="stDecoration"] {
        background-image: linear-gradient(90deg, #00416A, #E4E5E6);
        background: linear-gradient(90deg, #0052D4, #4364F7, #6FB1FC);
    }
    hr {
        border-bottom: 2px solid #4364F7 !important;
    }
    .stLinkButton > a {
        border-color: #4364F7 !important;
        color: #0052D4 !important;
        transition: all 0.3s ease;
    }
    .stLinkButton > a:hover {
        background-color: #0052D4 !important;
        color: white !important;
        transform: translateY(-2px);
    }
    /* Estilo para las etiquetas de habilidades */
    .skill-badge {
        display: inline-block;
        padding: 4px 10px;
        margin: 2px;
        background-color: #e0e7ff;
        color: #0052D4;
        border-radius: 15px;
        font-size: 0.85em;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Mensaje de bienvenida (solo se muestra una vez por sesión)
if 'bienvenida' not in st.session_state:
    st.toast("¡Bienvenido al Portafolio Interactivo de Juan Pablo!", icon="🚀")
    st.session_state.bienvenida = True

# 4. Base de datos de aplicaciones
APLICACIONES = [
    {"titulo": "Detección de Objetos", "imagen": "a01.jpg", "descripcion": "Esta aplicación utiliza redes neuronales convolucionales para identificar y localizar múltiples objetos dentro de una imagen en tiempo real, trazando cajas delimitadoras con sus respectivas etiquetas y niveles de confianza.", "url": "https://yolov5-mr9nwahshc8eeaermea35t.streamlit.app/", "categoria": "Visión por Computadora", "modelo": "Computer Vision / YOLO"},
    {"titulo": "WordCloud Studio", "imagen": "a02.jpg", "descripcion": "Genera nubes de palabras dinámicas a partir de textos extensos. Esta herramienta de procesamiento de lenguaje natural resalta los términos más frecuentes, facilitando el análisis visual rápido de grandes volúmenes de datos textuales.", "url": "https://wordcloud-dtkdpdkeljazdz2fuavsro.streamlit.app/", "categoria": "Procesamiento de Lenguaje", "modelo": "NLP / Data Viz"},
    {"titulo": "Traductor Neuronal", "imagen": "a03.jpg", "descripcion": "Rompe las barreras del idioma con esta herramienta de traducción automática. Capaz de interpretar y convertir texto entre múltiples idiomas con alta precisión, conservando el contexto y la semántica original de las oraciones.", "url": "https://traductor-gehpghvr9q3edfajue3bwb.streamlit.app/", "categoria": "Procesamiento de Lenguaje", "modelo": "Sequence-to-Sequence"},
    {"titulo": "Demo TF-IDF en Español", "imagen": "a04.jpg", "descripcion": "Descubre la relevancia de las palabras en tus documentos. Esta aplicación implementa el algoritmo TF-IDF para extraer conceptos clave y analizar la importancia relativa de los términos en un corpus específico de textos en español.", "url": "https://tdfesp-xurouaqeyqepm4whrlpzwy.streamlit.app/", "categoria": "Procesamiento de Lenguaje", "modelo": "Information Retrieval"},
    {"titulo": "Análisis de Sentimiento", "imagen": "a05.jpg", "descripcion": "Evalúa el tono emocional detrás de las palabras. Esta herramienta clasifica textos según su polaridad (positiva, negativa o neutral), siendo ideal para analizar opiniones de usuarios o interacciones masivas en redes sociales.", "url": "https://sentimenta-mcwscyx7txyocfmduonoe6.streamlit.app/", "categoria": "Procesamiento de Lenguaje", "modelo": "Clasificación de Texto"},
    {"titulo": "Traductor de Imágenes", "imagen": "a06.jpg", "descripcion": "Combina tecnología OCR con modelos de traducción automática. Al subir una imagen que contenga texto en otro idioma, la aplicación extrae los caracteres procesables y los traduce instantáneamente a tu idioma de preferencia.", "url": "https://ocr-audio-33nfniq7a3tpyftdjgko4k.streamlit.app/", "categoria": "Visión por Computadora", "modelo": "OCR + Translation"},
    {"titulo": "Reconocimiento Óptico (OCR)", "imagen": "a07.jpg", "descripcion": "Digitaliza texto impreso o escrito con facilidad. Esta herramienta extrae la información contenida en imágenes o documentos escaneados, transformándolos en texto completamente editable mediante algoritmos de visión artificial.", "url": "https://5bo3dkbndniywucgnecrzc.streamlit.app/", "categoria": "Visión por Computadora", "modelo": "Optical Character Recognition"},
    {"titulo": "Agente de IA", "imagen": "a08.jpg", "descripcion": "Interactúa con un asistente virtual impulsado por modelos de lenguaje grande (LLM). Este agente está diseñado para comprender intenciones, mantener el contexto de la conversación y resolver consultas complejas de manera natural.", "url": "https://juanitakush-xwdjdbylj9wl9nttmyc6gl.streamlit.app/", "categoria": "Asistentes Virtuales", "modelo": "LLM / Conversational"},
    {"titulo": "Mi Primera App IA", "imagen": "a09.jpg", "descripcion": "Un espacio de experimentación y prueba de conceptos básicos. Aquí se exploran integraciones iniciales de modelos de machine learning y estructuras de interfaz, sentando las bases para aplicaciones interactivas más robustas.", "url": "https://ilydbjwqwuydndt4dyagxj.streamlit.app/", "categoria": "Otros", "modelo": "Prototipo Base"}
]

def cargar_imagen(ruta):
    try:
        if os.path.exists(ruta):
            img = Image.open(ruta)
            st.image(img, use_container_width=True)
        else:
            st.info(f"🖼️ Espacio para imagen: {ruta}")
    except Exception:
        st.error("Error al cargar la imagen.")

# --- BARRA LATERAL (Con tu perfil profesional) ---
with st.sidebar:
    st.title("🤖 Explorador de IA")
    
    # Buscador en vivo
    st.subheader("Búsqueda Rápida")
    busqueda = st.text_input("🔍 Escribe el nombre o tecnología...")
    
    st.subheader("Filtros")
    categorias_unicas = ["Todas"] + list(set(app["categoria"] for app in APLICACIONES))
    categoria_seleccionada = st.selectbox("Selecciona una categoría:", categorias_unicas)
    
    st.divider()
    
    # Perfil del Desarrollador Súper Pro
    st.subheader("👨‍💻 Desarrollador")
    st.markdown("**Juan Pablo Orrego Hurtado**")
    st.caption("📍 Medellín, Colombia")
    st.caption("🎓 Diseño Interactivo | Universidad EAFIT")
    
    st.markdown("""
        <div style="margin-top: 10px; margin-bottom: 20px;">
            <span class="skill-badge">Python</span>
            <span class="skill-badge">Streamlit</span>
            <span class="skill-badge">OpenCV / OCR</span>
            <span class="skill-badge">TouchDesigner</span>
            <span class="skill-badge">Unity VR</span>
        </div>
    """, unsafe_allow_html=True)

# --- CONTENIDO PRINCIPAL ---
cargar_imagen("a1.jpg")

st.title("Hub de Aplicaciones Inteligentes")
st.markdown("Explora el potencial del Machine Learning, la Visión Artificial y el Procesamiento de Lenguaje Natural a través de estas herramientas interactivas.")

# --- Panel de Métricas y Gráfico (Dashboard) ---
col_m1, col_m2, col_m3 = st.columns(3)
col_m1.metric("Aplicaciones Desplegadas", len(APLICACIONES))
col_m2.metric("Estado del Servidor", "Online 🟢")
col_m3.metric("Última Actualización", "Reciente")

with st.expander("📊 Ver análisis del portafolio"):
    # Genera un gráfico interactivo nativo de Streamlit basado en las categorías
    df_apps = pd.DataFrame(APLICACIONES)
    conteo_categorias = df_apps['categoria'].value_counts()
    st.bar_chart(conteo_categorias, color="#4364F7")

st.divider()

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.success(f"📚 **Recurso destacado:** Visita mi documentación extendida y ejercicios prácticos. [Ir al sitio web]({url_ia})")

# --- LÓGICA DE BÚSQUEDA Y FILTRADO ---
apps_filtradas = APLICACIONES

# Aplicar filtro de categoría
if categoria_seleccionada != "Todas":
    apps_filtradas = [app for app in apps_filtradas if app["categoria"] == categoria_seleccionada]

# Aplicar filtro de texto (Buscador en vivo)
if busqueda:
    apps_filtradas = [app for app in apps_filtradas if busqueda.lower() in app["titulo"].lower() or busqueda.lower() in app["modelo"].lower()]

# --- RENDERIZADO DE LAS TARJETAS ---
if not apps_filtradas:
    st.warning("No se encontraron aplicaciones que coincidan con tu búsqueda.")
else:
    tab1, tab2 = st.tabs(["🔲 Vista de Cuadrícula", "📋 Vista de Lista"])
    
    with tab1:
        columnas = st.columns(3)
        for index, app in enumerate(apps_filtradas):
            col = columnas[index % 3]
            
            with col:
                with st.container(border=True, height=530):
                    st.subheader(app["titulo"])
                    st.caption(f"⚙️ {app['modelo']}")
                    cargar_imagen(app["imagen"])
                    st.write(app["descripcion"])
                    st.link_button("Abrir aplicación ↗", app["url"], use_container_width=True)
                    
    with tab2:
        for app in apps_filtradas:
            with st.container(border=True):
                st.markdown(f"### {app['titulo']} - `{app['modelo']}`")
                st.write(app["descripcion"])
                st.link_button("Acceder ↗", app["url"])

# --- SECCIÓN DE CONTACTO (FOOTER) ---
st.divider()
st.subheader("📬 ¿Tienes un proyecto en mente?")
with st.form("contacto_form", clear_on_submit=True):
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        nombre = st.text_input("Tu nombre")
    with col_f2:
        email = st.text_input("Tu correo electrónico")
    mensaje = st.text_area("Mensaje")
    submit = st.form_submit_button("Enviar Mensaje", use_container_width=True)
    if submit:
        st.success("¡Gracias por contactarme! El sistema de envío está en desarrollo, pero pronto estará activo.")
