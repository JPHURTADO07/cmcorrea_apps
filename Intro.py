import streamlit as st
from PIL import Image
import os

# 1. Configuración de página (Debe ser la primera línea)
st.set_page_config(
    page_title="Hub de Inteligencia Artificial",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Base de datos de aplicaciones ampliada con metadatos técnicos (Lógica IA)
APLICACIONES = [
    {
        "titulo": "Detección de Objetos",
        "imagen": "txt_to_audio2.png",
        "descripcion": "En el siguiente enlace usaremos una de las aplicaciones de Detección de Objetos en Imágenes.",
        "url": "https://yolov5-mr9nwahshc8eeaermea35t.streamlit.app/",
        "categoria": "Visión por Computadora",
        "modelo": "YOLOv5",
        "estado": "En línea 🟢"
    },
    {
        "titulo": "WordCloud Studio",
        "imagen": "txt_to_audio.png",
        "descripcion": "En el siguiente enlace usaremos una de las aplicaciones de WordCloud Studio.",
        "url": "https://wordcloud-dtkdpdkeljazdz2fuavsro.streamlit.app/",
        "categoria": "Procesamiento de Lenguaje",
        "modelo": "NLP Clásico",
        "estado": "En línea 🟢"
    },
    {
        "titulo": "Traductor",
        "imagen": "OIG5.jpg",
        "descripcion": "En el siguiente enlace usaremos una de las aplicaciones de Traductor.",
        "url": "https://traductor-gehpghvr9q3edfajue3bwb.streamlit.app/",
        "categoria": "Procesamiento de Lenguaje",
        "modelo": "Transformer",
        "estado": "En línea 🟢"
    },
    {
        "titulo": "Demo TF-IDF Español",
        "imagen": "OIG8.jpg",
        "descripcion": "En la siguiente veremos una aplicación que usa la Demo TF-IDF en Español.",
        "url": "https://tdfesp-xurouaqeyqepm4whrlpzwy.streamlit.app/",
        "categoria": "Procesamiento de Lenguaje",
        "modelo": "Scikit-Learn",
        "estado": "En línea 🟢"
    },
    {
        "titulo": "Análisis de Sentimiento",
        "imagen": "data_analisis.png",
        "descripcion": "En el siguiente enlace veremos como se puede hacer Análisis de Sentimiento.",
        "url": "https://sentimenta-mcwscyx7txyocfmduonoe6.streamlit.app/",
        "categoria": "Procesamiento de Lenguaje",
        "modelo": "VADER / BERT",
        "estado": "En línea 🟢"
    },
    {
        "titulo": "Traductor de Imágenes",
        "imagen": "OIG3.jpg",
        "descripcion": "En el siguiente enlace veremos como realizamos el Traductor de Imágenes.",
        "url": "https://ocr-audio-33nfniq7a3tpyftdjgko4k.streamlit.app/",
        "categoria": "Visión por Computadora",
        "modelo": "OCR + NLP",
        "estado": "En línea 🟢"
    },
    {
        "titulo": "Reconocimiento Óptico",
        "imagen": "Chat_pdf.png",
        "descripcion": "En la siguiente veremos una aplicación de Reconocimiento óptico de Caracteres.",
        "url": "https://5bo3dkbndniywucgnecrzc.streamlit.app/",
        "categoria": "Visión por Computadora",
        "modelo": "Tesseract",
        "estado": "En línea 🟢"
    },
    {
        "titulo": "Agente de IA",
        "imagen": "OIG4.jpg",
        "descripcion": "En el siguiente enlace veremos al Agente de IA en acción.",
        "url": "https://juanitakush-xwdjdbylj9wl9nttmyc6gl.streamlit.app/",
        "categoria": "Asistentes Virtuales",
        "modelo": "LLM Generativo",
        "estado": "En línea 🟢"
    },
    {
        "titulo": "Mi Primera App",
        "imagen": "OIG6.jpg",
        "descripcion": "En el siguiente enlace veremos Mi Primera App.",
        "url": "https://ilydbjwqwuydndt4dyagxj.streamlit.app/",
        "categoria": "Otros",
        "modelo": "Básico",
        "estado": "Mantenimiento 🟡"
    }
]

# Función robusta para cargar imágenes
def cargar_imagen(ruta, usar_ancho_completo=False):
    try:
        if os.path.exists(ruta):
            img = Image.open(ruta)
            st.image(img, use_container_width=usar_ancho_completo)
        else:
            # Placeholder si no encuentra la imagen
            st.info(f"🖼️️ Imagen pendiente: {ruta}")
    except Exception:
        st.error("Error al cargar la imagen.")

# --- 1. BANNER SUPERIOR ---
# Usamos 'OIG8.jpg' temporalmente como portada. Ajustado al ancho completo.
cargar_imagen('OIG8.jpg', usar_ancho_completo=True)

# --- 2. ENCABEZADO Y PANEL DE MÉTRICAS (Lógica de Dashboard IA) ---
st.title("🤖 Hub Central de Modelos de Inteligencia Artificial")
st.markdown("*Plataforma integral para explorar, analizar y ejecutar modelos de Machine Learning interactivos.*")

# Métricas que dan un aspecto muy profesional y analítico
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
col_m1.metric(label="Modelos Desplegados", value=f"{len(APLICACIONES)}", delta="Operativos")
col_m2.metric(label="Visión por Computadora", value="3", delta="GPUs Activas")
col_m3.metric(label="Procesamiento de Lenguaje", value="4", delta="Latencia < 50ms")
col_m4.metric(label="Estado del Servidor", value="Óptimo", delta="AWS US-East", delta_color="normal")

st.divider()

# --- 3. BARRA LATERAL (FILTROS Y CONTEXTO) ---
with st.sidebar:
    st.title("⚙️ Panel de Control")
    st.info(
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real."
    )
    
    st.divider()
    st.subheader("Búsqueda Avanzada")
    
    # Campo de texto para buscar
    busqueda_texto = st.text_input("🔍 Buscar por nombre:", "").lower()
    
    # Selector de categorías
    categorias_unicas = ["Todas"] + list(set(app["categoria"] for app in APLICACIONES))
    categoria_seleccionada = st.selectbox("📌 Filtrar por arquitectura:", categorias_unicas)

# --- 4. ORGANIZACIÓN EN PESTAÑAS (TABS) ---
tab_apps, tab_docs, tab_recursos = st.tabs(["🚀 Explorar Modelos", "🧠 Arquitectura de IA", "📚 Enlaces Externos"])

# PESTAÑA PRINCIPAL: LAS TARJETAS UNIFORMES
with tab_apps:
    # Lógica de filtrado combinada (Texto + Categoría)
    apps_filtradas = APLICACIONES
    if categoria_seleccionada != "Todas":
        apps_filtradas = [app for app in apps_filtradas if app["categoria"] == categoria_seleccionada]
    if busqueda_texto:
        apps_filtradas = [app for app in apps_filtradas if busqueda_texto in app["titulo"].lower()]

    if not apps_filtradas:
        st.warning("Ningún modelo coincide con los parámetros de búsqueda.")
    else:
        columnas = st.columns(3)
        for index, app in enumerate(apps_filtradas):
            col = columnas[index % 3] 
            with col:
                # SOLUCIÓN DE TAMAÑO: height=450 fuerza a que todos los cuadros midan exactamente lo mismo
                with st.container(border=True, height=460):
                    st.subheader(app["titulo"], divider="rainbow")
                    
                    # Imagen ajustada al contenedor para mantener proporciones
                    cargar_imagen(app["imagen"], usar_ancho_completo=True)
                    
                    # Badges técnicos
                    st.caption(f"⚙️ **{app['modelo']}** | {app['estado']}")
                    
                    # Descripción
                    st.write(app["descripcion"])
                    
                    # Botón en la parte inferior de la tarjeta
                    st.link_button(f"Ejecutar Modelo ↗", app["url"], use_container_width=True)

# PESTAÑA DE DOCUMENTACIÓN (Lógica Educativa)
with tab_docs:
    st.header("Diccionario de Tecnologías Aplicadas")
    colA, colB = st.columns(2)
    with colA:
        with st.expander("👁️ Visión por Computadora (CV)", expanded=True):
            st.write("Disciplina que permite a las computadoras extraer información de imágenes y videos. Usamos modelos como **YOLO** (You Only Look Once) para detección de objetos en tiempo real y **Tesseract OCR** para extraer texto de imágenes.")
    with colB:
        with st.expander("🗣️ Procesamiento de Lenguaje Natural (NLP)", expanded=True):
            st.write("Rama que permite a las máquinas entender el lenguaje humano. Utilizamos técnicas de vectorización como **TF-IDF** y modelos basados en **Transformers** para traducir textos y analizar sentimientos en fracciones de segundo.")

# PESTAÑA DE RECURSOS (Tu enlace original)
with tab_recursos:
    st.header("Plataforma Principal de Aprendizaje")
    url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
    
    st.info("💡 En nuestro portal principal encontrarás teoría profunda, tutoriales paso a paso y más ejercicios prácticos diseñados para reforzar tus conocimientos de IA.")
    st.link_button("🌐 Visitar la Página Web y Ejercicios", url_ia, type="primary")

# --- FOOTER ---
st.markdown("<br><hr><center><p style='color:gray;'>Sistema Centralizado de Despliegue de IA • 2024</p></center>", unsafe_allow_html=True)
