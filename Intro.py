import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Detección de Objetos en Imágenes")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace usaremos una de las aplicaciones de Detección de Objetos en Imágenes") 
 url = "https://yolov5-mr9nwahshc8eeaermea35t.streamlit.app/"
 st.write(f"Detección de Objetos en Imágenes: [Enlace]({url})")

 st.subheader("WordCloud Studio")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace usaremos una de las aplicaciones de WordCloud Studio.") 
 url = "https://wordcloud-dtkdpdkeljazdz2fuavsro.streamlit.app/"
 st.write(f"WordCloud Studio: [Enlace]({url})")

 st.subheader("Traductor")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace usaremos una de las aplicaciones de Traductor.") 
 url = "https://traductor-gehpghvr9q3edfajue3bwb.streamlit.app/"
 st.write(f"Traductor: [Enlace]({url})")

with col2: 
 st.subheader("Demo TF-IDF en Español")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa lDemo TF-IDF en Español.") 
 url = "https://tdfesp-xurouaqeyqepm4whrlpzwy.streamlit.app/"
 st.write(f"Demo TF-IDF en Español: [Enlace]({url})")

 st.subheader("Análisis de Sentimiento")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar Análisis de Sentimiento.") 
 url = "https://sentimenta-mcwscyx7txyocfmduonoe6.streamlit.app/"
 st.write(f"Análisis de Sentimiento: [Enlace]({url})")

 st.subheader("Traductor de Imágenes")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos Traductor de Imágenes.") 
 url = "https://ocr-audio-33nfniq7a3tpyftdjgko4k.streamlit.app/"
 st.write(f"Traductor de Imágenes: [Enlace]({url})")


with col3: 
 st.subheader("Reconocimiento óptico de Caracteres")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que Reconocimiento óptico de Caracteres.") 
 url = "https://5bo3dkbndniywucgnecrzc.streamlit.app/"
 st.write(f"Reconocimiento óptico de Caracteres: [Enlace]({url})")

 st.subheader("Agente de IA")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la Agente de IA.") 
 url = "https://juanitakush-xwdjdbylj9wl9nttmyc6gl.streamlit.app/"
 st.write(f"Agente de IA: [Enlace]({url})")
 
 st.subheader("Mi Primera App")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la Mi Primera App.") 
 url = "https://ilydbjwqwuydndt4dyagxj.streamlit.app/"
 st.write(f"Mi Primera App: [Enlace]({url})")
  

with col4: 
 st.subheader("Reconocimiento óptico de Caracteres")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que Reconocimiento óptico de Caracteres.") 
 url = "https://5bo3dkbndniywucgnecrzc.streamlit.app/"
 st.write(f"Reconocimiento óptico de Caracteres: [Enlace]({url})")

 st.subheader("Agente de IA")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la Agente de IA.") 
 url = "https://juanitakush-xwdjdbylj9wl9nttmyc6gl.streamlit.app/"
 st.write(f"Agente de IA: [Enlace]({url})")
 
 st.subheader("Mi Primera App")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la Mi Primera App.") 
 url = "https://ilydbjwqwuydndt4dyagxj.streamlit.app/"
 st.write(f"Mi Primera App: [Enlace]({url})")


