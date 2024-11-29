import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Entrenador para Placa ESP32",
    page_icon="🔌",
    layout="wide"
)

# Estilo CSS para el fondo azul oscuro
st.markdown("""
<style>
    .reportview-container {
        background: #001f3f;  /* Color de fondo azul oscuro */
    }
    .sidebar .sidebar-content {
        background: #001f3f;  /* Color de fondo de la barra lateral */
    }
    .stApp {
        background-color: #001f3f;  /* Color de fondo de la aplicación */
        color: #FFFFFF;  /* Color del texto */
    }
    h1 {
        text-align: center;  /* Centrar el título */
        font-size: 4em;  /* Aumentar el tamaño del título */
        color: #FFD700;  /* Color dorado para el título */
    }
    h2 {
        color: #FF0000;  /* Color rojo para subtítulos de metodología */
        text-align: center;  /* Centrar subtítulos */
    }
    h3 {
        color: #FFD700;  /* Color dorado para otros títulos */
        text-align: center;  /* Centrar otros títulos */
    }
    .section-divider {
        border-bottom: 2px solid #FFFFFF;  /* Línea divisoria blanca */
        margin: 20px 0;  /* Margen superior e inferior */
    }
</style>
""", unsafe_allow_html=True)

# Menú lateral
st.sidebar.title("Menú")
menu_options = ["Inicio", "Metodología", "Resultados", "Conclusiones", "Contacto"]
selection = st.sidebar.radio("Selecciona una sección:", menu_options)

# Contenido según la selección del menú
if selection == "Inicio":
    st.title("Entrenador para Placa ESP32 🔌")
    st.write("Este proyecto consiste en el diseño y creación de un PCB (Placa de Circuito Impreso) que permite la conexión de un microcontrolador ESP32 con dos sensores: un sensor DHT11 para medir la temperatura y la humedad, y un sensor de luminosidad. El objetivo es monitorear y controlar las condiciones ambientales en tiempo real, mostrando los datos en una pantalla OLED y en ThinkSpeak.")

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.write("**👥 Integrantes:**")
        st.write("Julián David Granados Gómez")
        st.write("Natalia Serrano Ardila")
        st.write("Angie Tatiana Silva Higuera")

    with col2:
        st.write("**👨‍🏫 Docente:**")
        st.write("Yuli Andrea Alvarez Pizarro")
        st.write("**📚 Espacio Académico:** Electrónica Digital 2024-2")

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    st.header("Componentes Electrónicos 🛠️")
    st.write("""
    - **ESP32**
    - **Sensor DHT11** (Temperatura y Humedad)
    - **Pantalla OLED 0.96"**
    - **Fotorresistencia (LDR)**
    - **Resistencias**
    """)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Ver Imagen Componentes Electrónicos"):
            if 'show_image' not in st.session_state:
                st.session_state.show_image = False
            st.session_state.show_image = not st.session_state.show_image
            if st.session_state.show_image:
                st.image("componentes electronicos.png", caption="Componentes Electrónicos", use_container_width=True)

    with col2:
        st.write("**Herramientas de Software 💻**")
        st.write("""
        - **Arduino IDE**: Para programar el ESP32.
        - **EasyEDA**: Para diseñar el PCB.
        - **Streamlit**: Para crear la interfaz web.
        - **ThingSpeak**: Para visualización de datos en la nube.
        """)

elif selection == "Metodología":
    st.header("Metodología 📚")
    
    st.markdown('<h2 style="color: #FFD700; text-align: center;">Diagrama del Circuito 📷</h2>', unsafe_allow_html=True)
    
    st.write("**Objetivo:** Validar el funcionamiento del circuito y la correcta conexión de los componentes.")
    
    if st.button("Ver Imagen del Diagrama"):
        if 'show_diagram' not in st.session_state:
            st.session_state.show_diagram = False
        st.session_state.show_diagram = not st.session_state.show_diagram
        if st.session_state.show_diagram:
            st.image("diagrama.png", caption="Diagrama del circuito con ESP32, sensores y pantalla OLED", use_container_width=True)

    st.write("""
    **Pasos y Herramientas Utilizadas:**
    - Se realizó un diagrama esquemático del circuito.
    - Se utilizaron herramientas como Fritzing para el diseño inicial.
    - Se validó la conexión de los componentes en una protoboard antes de la soldadura.
    """)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    st.header("Montaje en Protoboard 🔧")
    st.write("""
    En esta sección, se explica cómo se realizó el montaje del circuito en una protoboard. Se utilizó un código en Arduino para probar el funcionamiento de los sensores y la pantalla OLED.
    **Pasos:**
    - Conectar los componentes según el diagrama.
    - Probar el código en Arduino para verificar el funcionamiento.
    """)

    if st.button("Código de Arduino"):
        st.file_uploader("Sube tu código de Arduino aquí", type=["ino"])

    if st.button("Ver Video Funcionamiento Protoboard"):
        if 'show_video_protoboard' not in st.session_state:
            st.session_state.show_video_protoboard = False
        st.session_state.show_video_protoboard = not st.session_state.show_video_protoboard
        if st.session_state.show_video_protoboard:
            st.video("video funcionamiento protoboard.mp4")

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    st.header("Diseño de PCB 🖥️")
    if st.button("Ver Imagen del Diagrama de PCB"):
        if 'show_pcb' not in st.session_state:
            st.session_state.show_pcb = False
        st.session_state.show_pcb = not st.session_state.show_pcb
        if st.session_state.show_pcb:
            st.image("diseño pcb.png", caption="Diseño de PCB", use_container_width=True)

    if st.button("Ver Imagen EasyEDA"):
        if 'show_easyeda' not in st.session_state:
            st.session_state.show_easyeda = False
        st.session_state.show_easyeda = not st.session_state.show_easyeda
        if st.session_state.show_easyeda:
            st.image("easyeda.png", caption="EasyEDA Diseño", use_container_width=True)

    st.write("""
    **Pasos:**
    - Diseñar el PCB en EasyEDA.
    - Exportar el diseño para la fabricación.
    """)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    st.header("Soldadura e Implementación de Sensores 🔩")
    st.write("""
    En esta sección, se detalla el proceso de soldadura de los componentes en el PCB y la implementación de los sensores.
    **Pasos:**
    - Soldar los componentes en el PCB siguiendo el diseño.
    - Verificar las conexiones antes de encender el dispositivo.
    """)

    if st.button("Ver componentes soldados"):
        if 'show_soldered_components' not in st.session_state:
            st.session_state.show_soldered_components = False
        st.session_state.show_soldered_components = not st.session_state.show_soldered_components
        if st.session_state.show_soldered_components:
            st.image("componentes soldados.jpg", caption="Resultado Final", use_container_width=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    st.header("Creación de Carcasa 🏠")
    st.write("""
    Se diseñó una carcasa utilizando SolidWorks para proteger el controlador. La carcasa fue hecha a medida para adaptarse perfectamente al PCB y los componentes.
    **Pasos:**
    - Diseñar la carcasa en SolidWorks.
    - Imprimir la carcasa en 3D.
    """)

    if st.button("Ver Imagen Planos de Carcasa"):
        if 'show_case_plans' not in st.session_state:
            st.session_state.show_case_plans = False
        st.session_state.show_case_plans = not st.session_state.show_case_plans
        if st.session_state.show_case_plans:
            st.image("planos de carcasa.jpg", caption=" Planos de Carcasa", use_container_width=True)

    if st.button("Ver Imagen Impresión 3D de la Carcasa"):
        if 'show_3d_case' not in st.session_state:
            st.session_state.show_3d_case = False
        st.session_state.show_3d_case = not st.session_state.show_3d_case
        if st.session_state.show_3d_case:
            st.image("impresion 3d carcasa.jpg", caption="Impresión 3D de la Carcasa", use_container_width=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    st.header("Envío de Datos a ThingSpeak 📊")
    st.write("""
    En esta sección, se explica cómo se envían los datos recolectados por los sensores a la plataforma ThingSpeak. ThingSpeak es una plataforma de IoT que permite la visualización y análisis de datos en tiempo real. 
    Al utilizar ThingSpeak, podemos monitorear las condiciones ambientales desde cualquier lugar a través de su interfaz web.

    **Pasos para el envío de datos:**
    - Configurar la cuenta en ThingSpeak y crear un canal para recibir los datos.
    - Utilizar la API de ThingSpeak para enviar los datos desde el ESP32.
    - Visualizar los datos en gráficos y tablas en la plataforma.

    **Importancia de ThingSpeak:**
    - Permite el almacenamiento y análisis de datos a largo plazo.
    - Facilita la creación de alertas y notificaciones basadas en los datos recolectados.
    - Proporciona una interfaz amigable para la visualización de datos, lo que facilita la toma de decisiones informadas.

    Si deseas ver cómo se ven los datos en ThingSpeak, puedes hacer clic en el botón a continuación.
    """)

    if st.button("Ver Imagen Datos en ThingSpeak"):
        if 'show_thinkspeak_data' not in st.session_state:
            st.session_state.show_thinkspeak_data = False
        st.session_state.show_thinkspeak_data = not st.session_state.show_thinkspeak_data
        if st.session_state.show_thinkspeak_data:
            st.image("datos en thinkspeak.jpg", caption="Datos en ThingSpeak", use_container_width=True)

elif selection == "Resultados":
    st.header("Resultados 📈")
    st.write("""
    En esta sección se presentan los resultados finales del proyecto, incluyendo la carcasa y el prototipo final.
    """)

    if st.button("Ver Imagen Carcasa Final"):
        if 'show_carcasa_final' not in st.session_state:
            st.session_state.show_carcasa_final = False
        st.session_state.show_carcasa_final = not st.session_state.show_carcasa_final
        if st.session_state.show_carcasa_final:
            st.image("carcasa final.jpg", caption="Carcasa Final", use_container_width=True)

    if st.button("Ver Imagen Prototipo Final"):
        if 'show_prototipo_final' not in st.session_state:
            st.session_state.show_prototipo_final = False
        st.session_state.show_prototipo_final = not st.session_state.show_prototipo_final
        if st.session_state.show_prototipo_final:
            st.image("prototipo final.jpg", caption="Prototipo Final", use_container_width=True)

    if st.button("Ver Video Funcionamiento Prototipo Final"):
        if 'show_video_prototipo_final' not in st.session_state:
            st.session_state.show_video_prototipo_final = False
        st.session_state.show_video_prototipo_final = not st.session_state.show_video_prototipo_final
        if st.session_state.show_video_prototipo_final:
            st.video("funcionamiento prototipo final.mp4")

elif selection == "Conclusiones":
    st.header("Conclusiones 🎉")
    st.write("""
    - El proyecto demostró la viabilidad de utilizar el ESP32 para el monitoreo ambiental.
    - La integración de sensores y la visualización de datos en tiempo real son efectivas.
    - La carcasa diseñada proporciona una protección adecuada para el hardware.
    - La experiencia adquirida en el diseño y la implementación de este proyecto es invaluable para futuros desarrollos.
    - ¡Estamos emocionados por las posibilidades que ofrece esta tecnología! 🚀
    """)

    if st.button("Descargar Manual de Usuario"):
        with open("manual de usuario.pdf", "rb") as f:
            st.download_button("Descargar", f, file_name="manual de usuario.pdf", mime="application/pdf")

elif selection == "Contacto":
    st.header("Contacto 📞")
    st.write("""
    Si deseas realizar un proyecto similar o tienes alguna pregunta, no dudes en contactarnos:
    - **Julián David Granados Gómez**: julian@example.com
    - **Natalia Serrano Ardila**: natalia@example.com
    - **Angie Tatiana Silva Higuera**: angie@example.com
    """)

    st.write("¡Gracias por visitar nuestro proyecto! Si tienes alguna duda o comentario, no dudes en escribirnos.")