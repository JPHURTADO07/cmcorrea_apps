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
    /* Estilo para la cabecera de la Fase 2 */
    .fase2-header {
        background: linear-gradient(90deg, #E4E5E6, #f3f4f6);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0052D4;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Mensaje de bienvenida (solo se muestra una vez por sesión)
if 'bienvenida' not in st.session_state:
    st.toast("¡Bienvenido al Portafolio Interactivo de Juan Pablo!", icon="🚀")
    st.session_state.bienvenida = True

# 4. Bases de datos de aplicaciones
# --- ETAPA 1 ---
APLICACIONES = [
    {"titulo": "Detección de Objetos", "imagen": "a01.jpg", "descripcion": "Esta aplicación utiliza redes neuronales convolucionales para identificar y localizar múltiples objetos dentro de una imagen en tiempo real, trazando cajas delimitadoras con sus respectivas etiquetas y niveles de confianza.", "url": "https://yolov5-mr9nwahshc8eeaermea35t.streamlit.app/", "categoria": "Visión por Computadora", "modelo": "Computer Vision / YOLO"},
    {"titulo": "WordCloud Studio", "imagen": "a02.jpg", "descripcion": "Genera nubes de palabras dinámicas a partir de textos extensos. Esta herramienta de procesamiento de lenguaje natural resalta los términos más frecuentes, facilitando el análisis visual rápido de grandes volúmenes de datos textuales.", "url": "https://wordcloud-dtkdpdkeljazdz2fuavsro.streamlit.app/", "categoria": "Procesamiento de Lenguaje", "modelo": "NLP / Data Viz"},
    {"titulo": "Traductor Neuronal", "imagen": "a03.jpg", "descripcion": "Rompe las barreras del idioma con esta herramienta de traducción automática. Capaz de interpretar y convertir texto entre múltiples idiomas con alta precisión, conservando el contexto y la semántica original de las oraciones.", "url": "https://traductor-gehpghvr9q3edfajue3bwb.streamlit.app/", "categoria": "Procesamiento de Lenguaje", "modelo": "Sequence-to-Sequence"},
    {"titulo": "Demo TF-IDF en Español", "imagen": "a04.jpg", "descripcion": "Descubre la relevancia de las palabras en tus documentos. Esta aplicación implementa el algoritmo TF-IDF para extraer conceptos clave y analizar la importancia relativa de los términos en un corpus específico de textos en español.", "url": "https://tdfesp-xurouaqeyqepm4whrlpzwy.streamlit.app/", "categoria": "Procesamiento de Lenguaje", "modelo": "Information Retrieval"},
    {"titulo": "Análisis de Sentimiento", "imagen": "a05.jpg", "descripcion": "Evalúa el tono emocional detrás de las palabras. Esta herramienta clasifica textos según su polaridad (positiva, negativa o neutral), ideal para analizar opiniones de usuarios o interacciones masivas en redes sociales.", "url": "https://sentimenta-mcwscyx7txyocfmduonoe6.streamlit.app/", "categoria": "Procesamiento de Lenguaje", "modelo": "Clasificación de Texto"},
    {"titulo": "Traductor de Imágenes", "imagen": "a06.jpg", "descripcion": "Combina tecnología OCR con modelos de traducción automática. Al subir una imagen que contenga texto en otro idioma, la aplicación extrae los caracteres procesables y los traduce instantáneamente a tu idioma de preferencia.", "url": "https://ocr-audio-33nfniq7a3tpyftdjgko4k.streamlit.app/", "categoria": "Visión por Computadora", "modelo": "OCR + Translation"},
    {"titulo": "Reconocimiento Óptico (OCR)", "imagen": "a07.jpg", "descripcion": "Digitaliza texto impreso o escrito con facilidad. Esta herramienta extrae la información contenida en imágenes o documentos escaneados, transformándolos en texto completamente editable mediante algoritmos de visión artificial.", "url": "https://5bo3dkbndniywucgnecrzc.streamlit.app/", "categoria": "Visión por Computadora", "modelo": "Optical Character Recognition"},
    {"titulo": "Agente de IA", "imagen": "a08.jpg", "descripcion": "Interactúa con un asistente virtual impulsado por modelos de lenguaje grande (LLM). Este agente está diseñado para comprender intenciones, mantener el contexto de la conversación y resolver consultas complejas de manera natural.", "url": "https://juanitakush-xwdjdbylj9wl9nttmyc6gl.streamlit.app/", "categoria": "Asistentes Virtuales", "modelo": "LLM / Conversational"},
    {"titulo": "Mi Primera App IA", "imagen": "a09.jpg", "descripcion": "Un espacio de experimentación y prueba de conceptos básicos. Aquí se exploran integraciones iniciales de modelos de machine learning y estructuras de interfaz, sentando las bases para aplicaciones interactivas más robustas.", "url": "https://ilydbjwqwuydndt4dyagxj.streamlit.app/", "categoria": "Otros", "modelo": "Prototipo Base"}
]

# --- FASE 2: Nuevas Aplicaciones ---
NUEVAS_APLICACIONES = [
    {"titulo": "Lector de Sensor MQTT", "imagen": "img01.jpg", "descripcion": "Visualiza y monitorea en tiempo real los datos provenientes de sensores conectados a través del protocolo MQTT, ideal para proyectos de IoT e instalaciones interactivas.", "url": "https://recepmqtt-hcxbmvryempp4dfeik8mht.streamlit.app/", "modelo": "IoT / Data Stream"},
    {"titulo": "Interfaces Control por Voz", "imagen": "img02.jpg", "descripcion": "Controla aplicaciones utilizando comandos de voz. Este sistema multimodal permite interactuar con plataformas sin necesidad de contacto físico (hands-free).", "url": "https://ctrlvoice-ghqlc7cjicvoxnltwecxlx.streamlit.app/", "modelo": "Speech-to-Text / Multimodal"},
    {"titulo": "MQTT Control", "imagen": "img03.jpg", "descripcion": "Panel interactivo para el envío de comandos y control de hardware a distancia utilizando la mensajería ligera del protocolo MQTT.", "url": "https://sendcmqtt-fgebaqgmgss8nfwcmpmbzp.streamlit.app/", "modelo": "IoT / Control Dashboard"},
    {"titulo": "Análisis de Imagen", "imagen": "img04.jpg", "descripcion": "Sube tus imágenes y permite que los algoritmos de visión extraigan datos, identifiquen patrones visuales y generen conclusiones descriptivas del contenido.", "url": "https://visionapp-n9t4tuy5ji64mjfqnfzcnm.streamlit.app/", "modelo": "Computer Vision / Analysis"},
    {"titulo": "Descubre el Arte del Buen Comer", "imagen": "img05.jpg", "descripcion": "Asistente culinario basado en IA que analiza documentos (ChatPDF) para extraer recetas, técnicas y conocimientos de la tradición gastronómica.", "url": "https://chatpdf-tpyrd2q5na79ehnvrczjfl.streamlit.app/", "modelo": "RAG / ChatPDF"},
    {"titulo": "Tablero para Dibujo", "imagen": "img06.jpg", "descripcion": "Lienzo digital interactivo donde puedes realizar trazos libres, ideal como módulo de entrada para posteriores modelos de reconocimiento visual.", "url": "https://tableropropio-8h7spabo2dpnc7pkmzrf32.streamlit.app/", "modelo": "UI Canvas / Interacción"},
    {"titulo": "Tablero Inteligente", "imagen": "img07.jpg", "descripcion": "Lienzo de dibujo potenciado con IA, capaz de capturar tus trazos en tiempo real para que los modelos de machine learning interpreten tus bocetos.", "url": "https://drawrecog-8dmelrpjrnneydubuhsqih.streamlit.app/", "modelo": "Sketch Recognition"},
    {"titulo": "Detección de Dígitos a Mano", "imagen": "img08.jpg", "descripcion": "Dibuja un número y deja que la red neuronal lo clasifique. Utiliza el clásico dataset MNIST para demostrar la precisión de la detección en tiempo real.", "url": "https://mnistpred-93wuranhxyualbnjkppjdr.streamlit.app/", "modelo": "CNN / MNIST"},
    {"titulo": "Cuentos Mágicos: Dibuja tu Historia", "imagen": "img09.jpg", "descripcion": "Transforma tus bocetos en narrativas. La inteligencia artificial interpreta lo que dibujas para generar un cuento infantil original y creativo.", "url": "https://drawrecog-5efmiswovqrw78sawxtkpp.streamlit.app/", "modelo": "Vision + LLM Generative"}
]

def cargar_imagen(ruta):
    try:
        if ruta.startswith("http"):
            st.image(ruta, use_container_width=True)
        elif os.path.exists(ruta):
            img = Image.open(ruta)
            st.image(img, use_container_width=True)
        else:
            st.info(f"🖼️ Espacio reservado para imagen: {ruta}")
    except Exception:
        st.error(f"Error al cargar la imagen: {ruta}")

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("🤖 Explorador de IA")
    
    st.subheader("Búsqueda Rápida")
    busqueda = st.text_input("🔍 Escribe el nombre o tecnología...")
    
    st.subheader("Filtros (Etapa 1)")
    categorias_unicas = ["Todas"] + list(set(app["categoria"] for app in APLICACIONES))
    categoria_seleccionada = st.selectbox("Selecciona una categoría:", categorias_unicas)
    
    st.divider()
    
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

# --- CONTENIDO PRINCIPAL: ETAPA 1 ---
cargar_imagen("a1.jpg") # Banner principal superior

st.title("Hub de Aplicaciones Inteligentes")
st.markdown("Explora el potencial del Machine Learning, la Visión Artificial y el Procesamiento de Lenguaje Natural a través de estas herramientas interactivas.")

col_m1, col_m2, col_m3 = st.columns(3)
col_m1.metric("Aplicaciones Desplegadas", len(APLICACIONES) + len(NUEVAS_APLICACIONES))
col_m2.metric("Estado del Servidor", "Online 🟢")
col_m3.metric("Última Actualización", "Reciente")

with st.expander("📊 Ver análisis del portafolio (Etapa 1)"):
    df_apps = pd.DataFrame(APLICACIONES)
    conteo_categorias = df_apps['categoria'].value_counts()
    st.bar_chart(conteo_categorias, color="#4364F7")

st.divider()

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.success(f"📚 **Recurso destacado:** Visita mi documentación extendida y ejercicios prácticos. [Ir al sitio web]({url_ia})")

# Filtros Etapa 1
apps_filtradas = APLICACIONES
if categoria_seleccionada != "Todas":
    apps_filtradas = [app for app in apps_filtradas if app["categoria"] == categoria_seleccionada]
if busqueda:
    apps_filtradas = [app for app in apps_filtradas if busqueda.lower() in app["titulo"].lower() or busqueda.lower() in app["modelo"].lower()]

# Renderizado Etapa 1
if not apps_filtradas:
    st.warning("No se encontraron aplicaciones que coincidan con tu búsqueda en la Etapa 1.")
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


# --- SEGUNDA ETAPA: Interfaces Multimodales e IoT ---
st.markdown("""
<div class="fase2-header">
    <h2 style="margin-bottom: 5px; color: #00416A;">🚀 Fase 2: IoT, Interfaces Multimodales y Creatividad</h2>
    <p style="margin-bottom: 0px; color: #333;">Nuevos módulos enfocados en telemetría, interacción mediante voz y reconocimiento de bocetos en tiempo real.</p>
</div>
""", unsafe_allow_html=True)

# Filtro de búsqueda también aplicable a la Etapa 2
apps_fase2_filtradas = NUEVAS_APLICACIONES
if busqueda:
    apps_fase2_filtradas = [app for app in NUEVAS_APLICACIONES if busqueda.lower() in app["titulo"].lower() or busqueda.lower() in app["modelo"].lower()]

if not apps_fase2_filtradas:
    st.info("Ningún proyecto de la Fase 2 coincide con tu búsqueda.")
else:
    columnas_fase2 = st.columns(3)
    for index, app in enumerate(apps_fase2_filtradas):
        col = columnas_fase2[index % 3]
        with col:
            with st.container(border=True, height=520):
                st.subheader(app["titulo"])
                st.caption(f"💡 {app['modelo']}")
                cargar_imagen(app["imagen"])
                st.write(app["descripcion"])
                st.link_button("Probar Proyecto ↗", app["url"], use_container_width=True)


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
        st.success(f"¡Gracias {nombre}! Tu mensaje ha sido registrado exitosamente. Te contactaré pronto.")
