import streamlit as st
from PIL import Image
import os
import pandas as pd

# 1. Configuración inicial
st.set_page_config(
    page_title="Portafolio de IA | Juan Pablo Orrego",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS Avanzado (Micro-interacciones y White-labeling)
st.markdown("""
    <style>
    /* Ocultar elementos por defecto de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Tema y degradados */
    [data-testid="stDecoration"] {
        background-image: linear-gradient(90deg, #00416A, #E4E5E6);
        background: linear-gradient(90deg, #0052D4, #4364F7, #6FB1FC);
    }
    
    /* Estilo de botones */
    .stLinkButton > a {
        border-color: #4364F7 !important;
        color: #0052D4 !important;
        transition: all 0.3s ease;
        border-radius: 8px !important;
    }
    .stLinkButton > a:hover {
        background-color: #0052D4 !important;
        color: white !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(0, 82, 212, 0.2);
    }
    
    /* Tarjetas de proyectos (Hover Effects) */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 12px !important;
        transition: all 0.3s ease-in-out;
        background-color: #ffffff;
        box-shadow: 0 2px 5px rgba(0,0,0,0.04);
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 20px rgba(67, 100, 247, 0.15);
        border-color: #4364F7 !important;
    }

    /* Etiquetas de habilidades */
    .skill-badge {
        display: inline-block;
        padding: 5px 12px;
        margin: 3px;
        background-color: #e0e7ff;
        color: #0052D4;
        border-radius: 20px;
        font-size: 0.85em;
        font-weight: 600;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Cabecera Fase 2 */
    .fase2-header {
        background: linear-gradient(90deg, #f8f9fa, #e9ecef);
        padding: 25px;
        border-radius: 12px;
        border-left: 6px solid #0052D4;
        margin-top: 50px;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Notificación de bienvenida
if 'bienvenida' not in st.session_state:
    st.toast("¡Bienvenido al Portafolio Interactivo de Juan Pablo!", icon="🚀")
    st.session_state.bienvenida = True

# 4. Bases de datos cacheadas (Buena práctica de rendimiento)
@st.cache_data
def obtener_aplicaciones():
    etapa1 = [
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
    
    etapa2 = [
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
    return etapa1, etapa2

APLICACIONES, NUEVAS_APLICACIONES = obtener_aplicaciones()

def cargar_imagen(ruta):
    try:
        if ruta.startswith("http"):
            st.image(ruta, use_container_width=True)
        elif os.path.exists(ruta):
            img = Image.open(ruta)
            st.image(img, use_container_width=True)
        else:
            st.info(f"🖼️ Pendiente: {ruta}")
    except Exception:
        st.error(f"Error en: {ruta}")

# --- BARRA LATERAL ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2111/2111432.png", width=60) # Icono decorativo
    st.title("Hub de IA")
    
    st.subheader("Búsqueda Rápida")
    busqueda = st.text_input("🔍 Escribe una tecnología o proyecto...")
    
    st.subheader("Filtrar por Área")
    categorias_unicas = ["Todas"] + list(set(app["categoria"] for app in APLICACIONES))
    categoria_seleccionada = st.selectbox("Categoría:", categorias_unicas)
    
    st.divider()
    
    st.markdown("**👨‍💻 Juan Pablo Orrego Hurtado**")
    st.caption("📍 Medellín, Colombia")
    st.caption("🎓 Diseño Interactivo | Universidad EAFIT")
    
    st.markdown("""
        <div style="margin-top: 15px; margin-bottom: 20px;">
            <span class="skill-badge">Python</span>
            <span class="skill-badge">Streamlit</span>
            <span class="skill-badge">OpenCV / OCR</span>
            <span class="skill-badge">TouchDesigner</span>
            <span class="skill-badge">Unity VR</span>
        </div>
    """, unsafe_allow_html=True)

# --- CONTENIDO PRINCIPAL: SECCIÓN HERO ---
# Diseño a dos columnas para la presentación
col_texto, col_img = st.columns([1.5, 1], gap="large")

with col_texto:
    st.title("Hub de Aplicaciones Inteligentes")
    st.markdown("##### Explorando la intersección entre el Diseño Interactivo y la Inteligencia Artificial.")
    st.write("Bienvenido a mi entorno de pruebas. Aquí desarrollo e integro modelos de Machine Learning, Visión Artificial y Procesamiento de Lenguaje Natural en interfaces web accesibles y centradas en el usuario.")
    
with col_img:
    cargar_imagen("a1.jpg") # Tu banner principal ahora flota a la derecha de tu texto

st.divider()

# --- PANEL DE MÉTRICAS ---
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
col_m1.metric("Proyectos Totales", len(APLICACIONES) + len(NUEVAS_APLICACIONES))
col_m2.metric("Áreas Exploradas", len(categorias_unicas) - 1)
col_m3.metric("Estado del Servidor", "Online 🟢")
col_m4.metric("Último Commit", "Hoy")

with st.expander("📊 Ver análisis de distribución tecnológica"):
    df_apps = pd.DataFrame(APLICACIONES)
    conteo_categorias = df_apps['categoria'].value_counts()
    st.bar_chart(conteo_categorias, color="#4364F7", height=200)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.info(f"📚 **Documentación Académica:** Para ver los diagramas de arquitectura y ejercicios prácticos, visita [mi sitio en Google Sites]({url_ia}).")

# --- LÓGICA DE FILTRADO (ETAPA 1) ---
apps_filtradas = APLICACIONES
if categoria_seleccionada != "Todas":
    apps_filtradas = [app for app in apps_filtradas if app["categoria"] == categoria_seleccionada]
if busqueda:
    apps_filtradas = [app for app in apps_filtradas if busqueda.lower() in app["titulo"].lower() or busqueda.lower() in app["modelo"].lower()]

# --- RENDERIZADO ETAPA 1 ---
st.markdown("### 🧩 Fase 1: Modelos Base y Procesamiento")
if not apps_filtradas:
    st.warning("No se encontraron coincidencias en la Fase 1.")
else:
    columnas = st.columns(3)
    for index, app in enumerate(apps_filtradas):
        col = columnas[index % 3]
        with col:
            with st.container(border=True, height=540):
                st.subheader(app["titulo"])
                st.caption(f"⚙️ {app['modelo']}")
                cargar_imagen(app["imagen"])
                st.write(app["descripcion"])
                st.link_button("Abrir aplicación ↗", app["url"], use_container_width=True)

# --- SEGUNDA ETAPA: Interfaces Multimodales e IoT ---
st.markdown("""
<div class="fase2-header">
    <h2 style="margin-bottom: 5px; color: #00416A;">🚀 Fase 2: IoT, Interacciones Multimodales y Creatividad</h2>
    <p style="margin-bottom: 0px; color: #495057;">Sistemas avanzados que combinan telemetría de sensores físicos, control por comandos de voz y algoritmos generativos en tiempo real.</p>
</div>
""", unsafe_allow_html=True)

# Filtro de búsqueda Fase 2
apps_fase2_filtradas = NUEVAS_APLICACIONES
if busqueda:
    apps_fase2_filtradas = [app for app in NUEVAS_APLICACIONES if busqueda.lower() in app["titulo"].lower() or busqueda.lower() in app["modelo"].lower()]

if not apps_fase2_filtradas:
    st.warning("No se encontraron coincidencias en la Fase 2.")
else:
    columnas_fase2 = st.columns(3)
    for index, app in enumerate(apps_fase2_filtradas):
        col = columnas_fase2[index % 3]
        with col:
            with st.container(border=True, height=540):
                st.subheader(app["titulo"])
                st.caption(f"💡 {app['modelo']}")
                cargar_imagen(app["imagen"])
                st.write(app["descripcion"])
                st.link_button("Probar Proyecto ↗", app["url"], use_container_width=True)

# --- SECCIÓN DE CONTACTO (FOOTER) ---
st.divider()
st.markdown("### 📬 ¿Tienes un proyecto en mente?")
st.write("Si te interesa el cruce entre diseño interactivo y tecnología, envíame un mensaje.")

with st.form("contacto_form", clear_on_submit=True):
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        nombre = st.text_input("Tu nombre")
    with col_f2:
        email = st.text_input("Tu correo electrónico")
    mensaje = st.text_area("Mensaje o consulta")
    submit = st.form_submit_button("🚀 Enviar Mensaje", use_container_width=True)
    
    if submit:
        st.success(f"¡Gracias {nombre}! He recibido tu mensaje. Te contactaré a la brevedad.")
