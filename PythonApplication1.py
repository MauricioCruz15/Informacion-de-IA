import os
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, 
    QLineEdit, QListWidget, QTextBrowser, QLabel, QSplitter,
    QStackedWidget, QPushButton, QFrame, QScrollArea
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

# Obtiene la ruta de la carpeta donde reside este archivo .py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Texto e información detallada para el término del Glosario
HTML_SISTEMA_INTELIGENTE = """
<h1 style="color: #0F172A; font-size: 24px; margin-bottom: 12px; text-decoration: none;">Sistema Inteligente</h1>

<p style="font-size: 16px; color: #334155; line-height: 1.6;">
Un <b>sistema inteligente</b> es un sistema informático (software o hardware) diseñado para percibir su entorno, 
procesar información, aprender de ella y tomar decisiones o acciones de manera autónoma para alcanzar un objetivo específico.
<br><br>
A diferencia de un programa tradicional (que sigue un conjunto fijo de reglas preprogramadas), un sistema inteligente 
puede adaptarse a situaciones nuevas, optimizar sus resultados con la experiencia y manejar incertidumbre.
</p>

<h3 style="color: #2563EB; font-size: 18px; margin-top: 20px; text-decoration: none;">Componentes Clave</h3>
<ul style="font-size: 15px; color: #334155; line-height: 1.6;">
    <li><b>Percepción (Entradas):</b> Capta datos del entorno mediante sensores, datos de entrada del usuario o bases de datos.</li>
    <li><b>Procesamiento y Aprendizaje:</b> Utiliza algoritmos de IA para analizar datos, encontrar patrones y razonar.</li>
    <li><b>Toma de Decisiones:</b> Selecciona la mejor acción posible basándose en sus objetivos y el análisis previo.</li>
    <li><b>Acción (Salidas):</b> Ejecuta una respuesta a través de actuadores, interfaces, alertas o automatizaciones.</li>
    <li><b>Retroalimentación (Feedback):</b> Evalúa el resultado de su acción para aprender y mejorar en el futuro.</li>
</ul>

<h3 style="color: #2563EB; font-size: 18px; margin-top: 20px; text-decoration: none;">Ejemplo Práctico: Termostato Inteligente</h3>
<p style="font-size: 15px; color: #334155; line-height: 1.6;">
<b>1. Percepción:</b> Mide la temperatura actual mediante sensores y detecta presencia.<br>
<b>2. Procesamiento y Aprendizaje:</b> Analiza tus horarios habituales y las condiciones climáticas para predecir cuándo necesitas la casa fría o caliente.<br>
<b>3. Toma de Decisiones:</b> Determina encender el aire acondicionado 20 minutos antes de que llegues a casa para optimizar el consumo de energía.<br>
<b>4. Acción:</b> Envía la señal al sistema de climatización para encenderse.<br>
<b>5. Retroalimentación:</b> Si ajustas manualmente la temperatura desde la app, el sistema registra ese cambio para ajustar su modelo de predicción futuro.
</p>

<hr style="border: none; border-top: 1px solid #CBD5E1; margin: 20px 0;">

<h2 style="color: #0F172A; font-size: 20px; margin-top: 10px; text-decoration: none;">Análisis Detallado del Flujo de Información</h2>

<div style="margin-top: 15px;">
    <h3 style="color: #0EA5E9; font-size: 17px; margin-bottom: 5px; text-decoration: none;">📥 1. Entradas (Captura y Sensado)</h3>
    <p style="font-size: 15px; color: #334155; line-height: 1.6; margin-top: 0;">
    Representan el punto de contacto inicial entre el sistema inteligente y el mundo exterior:
    </p>
    <ul style="font-size: 15px; color: #334155; line-height: 1.6;">
        <li><b>Sensores físicos:</b> Cámaras, micrófonos, termómetros, GPS, acelerómetros y sensores de proximidad.</li>
        <li><b>Interacción con usuarios:</b> Prompts de texto, comandos de voz, clics e historial de preferencias.</li>
        <li><b>Fuentes de datos externas:</b> Consultas a APIs, bases de datos relacionales, transmisiones en vivo y lecturas de archivos.</li>
    </ul>
</div>

<div style="margin-top: 20px;">
    <h3 style="color: #8B5CF6; font-size: 17px; margin-bottom: 5px; text-decoration: none;">⚙️ 2. Procesamiento de Datos (Núcleo Cognitivo)</h3>
    <p style="font-size: 15px; color: #334155; line-height: 1.6; margin-top: 0;">
    Etapa donde los datos crudos se transforman en conocimiento útil mediante razonamiento algorítmico:
    </p>
    <ul style="font-size: 15px; color: #334155; line-height: 1.6;">
        <li><b>Limpieza y Preprocesamiento:</b> Filtrado de ruido, normalización de datos y extracción de características relevantes.</li>
        <li><b>Inferencia y Aprendizaje:</b> Aplicación de modelos matemáticos (redes neuronales, árboles de decisión) para reconocer patrones y hacer predicciones.</li>
        <li><b>Razonamiento y Lógica:</b> Evaluación de reglas, cálculo de probabilidades e identificación de la mejor alternativa de solución.</li>
    </ul>
</div>

<div style="margin-top: 20px;">
    <h3 style="color: #10B981; font-size: 17px; margin-bottom: 5px; text-decoration: none;">🎯 3. Solución y Salida (Acción o Respuesta)</h3>
    <p style="font-size: 15px; color: #334155; line-height: 1.6; margin-top: 0;">
    Resultado tangible que genera el sistema inteligente para resolver la necesidad detectada:
    </p>
    <ul style="font-size: 15px; color: #334155; line-height: 1.6;">
        <li><b>Respuestas en pantalla o interfaz:</b> Recomendaciones personalizadas, respuestas textuales (chatbots), gráficos o alertas.</li>
        <li><b>Acciones mecánicas o físicas:</b> Control de actuadores, movimiento de brazos robóticos o frenado automático en vehículos.</li>
        <li><b>Retroalimentación (Bucle de Mejora):</b> El impacto producido genera nuevos datos que alimentan al modelo en iteraciones futuras.</li>
    </ul>
</div>
"""

# Datos del Glosario
GLOSARIO_IA = {
    "Aprendizaje Automático": "Subcampo de la IA centrado en entrenar algoritmos con datos para que realicen predicciones o tomen decisiones sin ser programados explícitamente para cada tarea.",
    "Aprendizaje Profundo": "Subconjunto del ML que utiliza redes neuronales profundas (de múltiples capas) para procesar patrones complejos en grandes volúmenes de datos no estructurados.",
    "IA Generativa": "Modelos de aprendizaje profundo capaces de generar contenido original (texto, imágenes, vídeo, audio o código) a partir de las instrucciones (prompts) enviadas por el usuario.",
    "Red Neuronal Artificial": "Algoritmo de ML inspirado en la estructura del cerebro humano, compuesto por capas de nodos (neuronas) interconectadas que procesan y analizan datos complejos.",
    "Red Neuronal Convolucional": "Tipo de red neuronal profunda especialmente diseñada para el procesamiento de datos con estructura de cuadrícula, como imágenes.",
    "Red Neuronal Recurrente": "Red neuronal diseñada para procesar datos secuenciales o de series temporales (como texto o voz) aprovechando estados de memoria interna.",
    "Aprendizaje Supervisado": "Técnica de ML que utiliza conjuntos de datos etiquetados por humanos para entrenar a los modelos a clasificar datos o predecir resultados con precisión.",
    "Aprendizaje No Supervisado": "Método donde el modelo analiza datos no etiquetados para descubrir patrones, estructuras o agrupaciones ocultas de manera autónoma.",
    "Aprendizaje Semi-supervisado": "Enfoque híbrido que combina una pequeña cantidad de datos etiquetados con una gran cantidad de datos no etiquetados para entrenar modelos.",
    "Aprendizaje Autosupervisado": "Técnica que genera sus propias etiquetas implícitas a partir de datos no estructurados en lugar de depender del etiquetado humano previo.",
    "Aprendizaje por Reforzamiento": "Enfoque de ML basado en la prueba y error, donde el sistema aprende a tomar decisiones mediante una función de recompensa y castigo.",
    "Aprendizaje por Transferencia": "Proceso mediante el cual el conocimiento adquirido al resolver un problema se reutiliza para mejorar el rendimiento en una tarea diferente pero relacionada.",
    "NLP Procesamiento del Lenguaje Natural": "Rama de la IA que otorga a los sistemas la capacidad de interpretar, comprender y responder al lenguaje humano.",
    "Visión por Computadora": "Campo de la IA dedicado a que las máquinas identifiquen, interpreten y procesen información del mundo visual (imágenes y vídeos).",
    "Modelo Base o Fundacional": "Modelo de aprendizaje profundo entrenado con enormes volúmenes de datos no etiquetados que sirve como base para construir diversas aplicaciones derivadas.",
    "LLM Gran Modelo de Lenguaje": "Tipo de modelo base entrenado masivamente con texto para entender y generar lenguaje natural.",
    "Transformadores": "Arquitectura de aprendizaje profundo entrenada en datos secuenciales que permite generar secuencias extendidas de contenido (palabras, código, imágenes).",
    "Ajuste Fino": "Proceso de adaptar y especializar un modelo base preentrenado alimentándolo con datos etiquetados específicos de un dominio o tarea.",
    "RAG Generación Aumentada por Recuperación": "Técnica que permite a un modelo generativo consultar fuentes de información externas fuera de sus datos de entrenamiento para responder con mayor precisión y relevancia.",
    "RLHF (Reinforcement Learning with Human Feedback)": "Método de ajuste donde evaluadores humanos califican o corrigen las respuestas del modelo para orientar su aprendizaje futuro.",
    "Ética en la IA": "Campo que aborda la transparencia, gobernanza, eliminación de sesgos (data bias) y la responsabilidad en el desarrollo y despliegue de tecnologías de IA.",
    "Agentes de IA": "Sistemas autónomos construidos sobre modelos de lenguaje capaces de percibir su entorno, tomar decisiones dinámicas y ejecutar secuencias de tareas para lograr un objetivo específico.",
    "Sistema Inteligente": HTML_SISTEMA_INTELIGENTE
}


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Explorador de Inteligencia Artificial')
        self.resize(1100, 720)

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ---------------- Barra Lateral (Menú de Navegación) ----------------
        sidebar = QFrame()
        sidebar.setObjectName("Sidebar")
        sidebar.setFixedWidth(240)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(10, 20, 10, 20)
        sidebar_layout.setSpacing(10)

        title_menu = QLabel("MENÚ IA")
        title_menu.setStyleSheet("font-size: 18px; font-weight: bold; color: #94A3B8; margin-bottom: 12px; padding-left: 5px; text-decoration: none;")
        sidebar_layout.addWidget(title_menu)

        self.btn_inicio = QPushButton("🏠 Inicio")
        self.btn_ramas = QPushButton("🌳 Ramas de la IA")
        self.btn_clasificacion = QPushButton("📊 Clasificación")
        self.btn_timeline = QPushButton("⏳ Línea del Tiempo")
        self.btn_glosario = QPushButton("📖 Glosario")
        self.btn_ensayo = QPushButton("📝 Ensayo")
        self.btn_proyecto = QPushButton("🛠 Proyecto Práctico")

        self.botones_menu = [
            self.btn_inicio,
            self.btn_ramas, 
            self.btn_clasificacion, 
            self.btn_timeline, 
            self.btn_glosario,
            self.btn_ensayo,
            self.btn_proyecto
        ]

        for index, btn in enumerate(self.botones_menu):
            btn.setCheckable(True)
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, idx=index: self.cambiar_pagina(idx))
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()
        main_layout.addWidget(sidebar)

        # ---------------- Contenedor Dinámico ----------------
        self.stack = QStackedWidget()

        self.stack.addWidget(self.crear_pagina_inicio())          # 0
        self.stack.addWidget(self.crear_pagina_ramas())           # 1
        self.stack.addWidget(self.crear_pagina_clasificacion())   # 2
        self.stack.addWidget(self.crear_pagina_timeline())        # 3
        self.stack.addWidget(self.crear_pagina_glosario())        # 4
        self.stack.addWidget(self.crear_pagina_ensayo())          # 5
        self.stack.addWidget(self.crear_pagina_proyecto())        # 6 (Proyecto Práctico es el índice 6)

        main_layout.addWidget(self.stack)
        self.cambiar_pagina(0)

    def cambiar_pagina(self, index):
        self.stack.setCurrentIndex(index)
        for i, btn in enumerate(self.botones_menu):
            btn.setChecked(i == index)

    # ---------------- 1. INICIO ----------------
    def crear_pagina_inicio(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setAlignment(Qt.AlignTop)

        title = QLabel("Inteligencia Artificial")
        title.setStyleSheet("font-size: 32px; font-weight: bold; color: #1E293B; margin-bottom: 20px; text-decoration: none;")
        
        card = QFrame()
        card.setStyleSheet("background-color: white; border: 1px solid #E2E8F0; border-radius: 10px; padding: 25px;")
        card_layout = QVBoxLayout(card)

        desc = QLabel(
            "La Inteligencia Artificial es un campo interdisciplinario dedicado al diseño de sistemas capaces "
            "de realizar tareas asociadas con la inteligencia humana, como aprender, razonar, reconocer patrones, "
            "comprender lenguaje, resolver problemas y tomar decisiones."
        )
        desc.setWordWrap(True)
        desc.setStyleSheet("font-size: 18px; line-height: 1.6; color: #334155; border: none; text-decoration: none;")

        card_layout.addWidget(desc)
        layout.addWidget(title)
        layout.addWidget(card)
        return page

    # ---------------- 2. RAMAS ----------------
    def crear_pagina_ramas(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("Ramas Disciplinares de la IA")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #1E293B; margin-bottom: 18px; text-decoration: none;")
        layout.addWidget(title)

        ramas_info = [
            ("Filosofía", "Aristóteles (300 AC) Describe de forma estructurada la forma como el ser humano produce conclusiones racionales a partir de un grupo de premisas. (Silogismos)"),
            ("Matemáticas", "Razonamiento con algoritmos. Cálculo: brindó las herramientas que nos permiten la modelación de diferentes tipos de fenómenos."),
            ("Psicología", "Refuerza la idea de que los humanos y otros animales pueden ser considerados como máquinas para el procesamiento de información (Conductismo y Psicología cognitiva por Piaget y Craik)."),
            ("Computación", "Las teorías de la IA encuentran un medio para su implementación de artefactos y modelado cognitivo a través de las computadoras."),
            ("Lingüística", "Aporta un área híbrida conocida como lingüística computacional o procesamiento del lenguaje natural."),
            ("Economía", "Área experta en la toma de decisiones basada en pérdidas/ganancias de rendimiento (Teoría de la decisión, Teoría de Juegos, Procesos de Markov)."),
            ("Neurociencia", "Ha contribuido a la IA con los conocimientos recabados sobre la forma en que el cerebro procesa la información.")
        ]

        for rama, texto in ramas_info:
            card = QFrame()
            card.setStyleSheet("background-color: white; border: 1px solid #E2E8F0; border-radius: 8px; padding: 15px; margin-bottom: 10px;")
            card_layout = QVBoxLayout(card)
            
            lbl_title = QLabel(f"• {rama}")
            lbl_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #2563EB; border: none; text-decoration: none;")
            
            lbl_desc = QLabel(texto)
            lbl_desc.setWordWrap(True)
            lbl_desc.setStyleSheet("font-size: 16px; color: #475569; border: none; margin-top: 4px; text-decoration: none;")

            card_layout.addWidget(lbl_title)
            card_layout.addWidget(lbl_desc)
            layout.addWidget(card)

        scroll.setWidget(content)
        return scroll

    # ---------------- 3. CLASIFICACIÓN ----------------
    def crear_pagina_clasificacion(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("Clasificación de Modelos de IA")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #1E293B; margin-bottom: 20px; text-decoration: none;")
        layout.addWidget(title)

        clasificaciones = [
            {
                "titulo": "IA Débil o Estrecha (Narrow AI - ANI)", 
                "desc": "Diseñada para resolver tareas específicas: traducción, recomendación, reconocimiento de imágenes, de voz o chat. Impulsa la mayor parte de la IA actual.",
                "img": "ani.jpg"
            },
            {
                "titulo": "IA Fuerte o General (AGI - General Artificial Intelligence)", 
                "desc": "Busca crear máquinas con inteligencia humana completa, capaces de realizar cualquier tarea intelectual. Es una categoría hipotética.",
                "img": "agi.jpg"
            },
            {
                "titulo": "IA Superinteligente (ASI)", 
                "desc": "Sistema hipotético que superaría a los humanos en todas las áreas cognitivas, siendo autoconsciente y con capacidad de planificación del futuro.",
                "img": "asi.jpg"
            }
        ]

        for item in clasificaciones:
            card = QFrame()
            card.setStyleSheet("background-color: white; border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px; margin-bottom: 20px;")
            card_layout = QVBoxLayout(card)

            lbl_type = QLabel(item["titulo"])
            lbl_type.setStyleSheet("font-size: 20px; font-weight: bold; color: #0F172A; border: none; text-decoration: none;")

            lbl_desc = QLabel(item["desc"])
            lbl_desc.setWordWrap(True)
            lbl_desc.setStyleSheet("font-size: 16px; color: #334155; margin-top: 6px; margin-bottom: 12px; border: none; text-decoration: none;")

            card_layout.addWidget(lbl_type)
            card_layout.addWidget(lbl_desc)

            ruta_img = os.path.join(BASE_DIR, "Imagenes", item["img"])
            pixmap = QPixmap(ruta_img)

            if not pixmap.isNull():
                lbl_img = QLabel()
                lbl_img.setPixmap(pixmap.scaledToWidth(750, Qt.SmoothTransformation))
                lbl_img.setAlignment(Qt.AlignCenter)
                lbl_img.setStyleSheet("border: none; margin-top: 5px;")
                card_layout.addWidget(lbl_img)
            else:
                lbl_error = QLabel(f"No se encontró la imagen: {item['img']}")
                lbl_error.setStyleSheet("color: #EF4444; font-size: 14px; border: none; text-decoration: none;")
                card_layout.addWidget(lbl_error)

            layout.addWidget(card)

        scroll.setWidget(content)
        return scroll

    # ---------------- 4. LÍNEA DEL TIEMPO ----------------
    def crear_pagina_timeline(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("Línea del Tiempo de la Inteligencia Artificial")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #1E293B; margin-bottom: 20px; text-decoration: none;")
        layout.addWidget(title)

        nombres_archivo = [
            "Linea_del_tiempo.jpg",
            "Linea_del_tiempo.png",
            "linea_del_tiempo.jpg",
            "linea_del_tiempo.png"
        ]

        pixmap = QPixmap()
        for nombre in nombres_archivo:
            ruta_absoluta = os.path.join(BASE_DIR, "Imagenes", nombre)
            pixmap = QPixmap(ruta_absoluta)
            if not pixmap.isNull():
                break

        if not pixmap.isNull():
            lbl_img = QLabel()
            lbl_img.setPixmap(pixmap.scaledToWidth(850, Qt.SmoothTransformation))
            lbl_img.setAlignment(Qt.AlignCenter)
            lbl_img.setStyleSheet("background-color: white; border: 1px solid #E2E8F0; border-radius: 8px; padding: 15px;")
            layout.addWidget(lbl_img)
        else:
            lbl_error = QLabel("⚠️ No se encontró la imagen de la línea del tiempo en la carpeta 'Imagenes'.")
            lbl_error.setStyleSheet("color: #EF4444; font-size: 16px; font-weight: bold; padding: 20px; background-color: #FEE2E2; border-radius: 8px; text-decoration: none;")
            layout.addWidget(lbl_error)

        layout.addStretch()
        scroll.setWidget(content)
        return scroll

    # ---------------- 5. GLOSARIO ----------------
    def crear_pagina_glosario(self):
        page = QWidget()
        layout_principal = QHBoxLayout(page)
        layout_principal.setContentsMargins(15, 15, 15, 15)

        splitter = QSplitter(Qt.Horizontal)

        panel_izquierdo = QWidget()
        panel_izquierdo.setMinimumWidth(320)
        layout_izquierdo = QVBoxLayout(panel_izquierdo)
        layout_izquierdo.setContentsMargins(0, 0, 10, 0)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText('🔍 Buscar término...')
        self.search_input.textChanged.connect(self.filtrar_terminos)
        layout_izquierdo.addWidget(self.search_input)

        self.lista_terminos = QListWidget()
        self.lista_terminos.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lista_terminos.addItems(sorted(GLOSARIO_IA.keys()))
        self.lista_terminos.currentTextChanged.connect(self.mostrar_definicion)
        layout_izquierdo.addWidget(self.lista_terminos)

        panel_derecho = QWidget()
        layout_derecho = QVBoxLayout(panel_derecho)
        layout_derecho.setContentsMargins(10, 0, 0, 0)

        self.titulo_label = QLabel('Selecciona un término')
        self.titulo_label.setWordWrap(True)
        self.titulo_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #0F172A; margin-bottom: 10px; text-decoration: none;")
        layout_derecho.addWidget(self.titulo_label)

        # Configuración para permitir contenido HTML rico correctamente
        self.definicion_text = QTextBrowser()
        self.definicion_text.setAcceptRichText(True)
        self.definicion_text.setStyleSheet("font-size: 16px; color: #334155; border: 1px solid #CBD5E1; border-radius: 8px; padding: 15px; line-height: 1.5; background-color: white;")
        layout_derecho.addWidget(self.definicion_text)

        # Botón interactivo que aparece cuando el término es "Sistema Inteligente"
        self.btn_esquema_glosario = QPushButton()
        self.btn_esquema_glosario.setCursor(Qt.PointingHandCursor)
        self.btn_esquema_glosario.setToolTip("Haz clic para ir al Proyecto Práctico")
        self.btn_esquema_glosario.clicked.connect(lambda: self.cambiar_pagina(6)) # Página 6: Proyecto Práctico

        layout_btn = QVBoxLayout(self.btn_esquema_glosario)
        layout_btn.setContentsMargins(10, 10, 10, 10)

        nombres_imagen = [
            "Esquema_Sistemas_Inteligentes.webp",
            "Esquema_Sistemas_Inteligentes.png",
            "Esquema_Sistemas_Inteligentes.jpg",
            "Esquema_Sistemas_Inteligentes.jpeg",
            "Esquema_Sistema_Inteligente.webp",
            "Esquema_Sistema_Inteligente.png",
            "Esquema_Sistema_Inteligente.jpg"
        ]

        pixmap = QPixmap()
        for nombre in nombres_imagen:
            ruta_absoluta = os.path.join(BASE_DIR, "Imagenes", nombre)
            pixmap = QPixmap(ruta_absoluta)
            if not pixmap.isNull():
                break

        if not pixmap.isNull():
            lbl_img = QLabel()
            lbl_img.setPixmap(pixmap.scaledToWidth(500, Qt.SmoothTransformation))
            lbl_img.setAlignment(Qt.AlignCenter)
            lbl_img.setStyleSheet("border: none;")
            layout_btn.addWidget(lbl_img)
        else:
            lbl_error = QLabel("⚠️ No se encontró la imagen del esquema.")
            lbl_error.setStyleSheet("color: #EF4444; font-size: 14px; border: none;")
            layout_btn.addWidget(lbl_error)

        lbl_hint = QLabel("💡 Presiona esta imagen/botón para ir al Proyecto Práctico")
        lbl_hint.setAlignment(Qt.AlignCenter)
        lbl_hint.setStyleSheet("font-size: 13px; font-weight: bold; color: #2563EB; margin-top: 6px; border: none;")
        layout_btn.addWidget(lbl_hint)

        self.btn_esquema_glosario.setStyleSheet("""
            QPushButton {
                background-color: #F8FAFC;
                border: 2px dashed #93C5FD;
                border-radius: 10px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #EFF6FF;
                border-color: #2563EB;
            }
        """)

        self.btn_esquema_glosario.setVisible(False)
        layout_derecho.addWidget(self.btn_esquema_glosario)

        splitter.addWidget(panel_izquierdo)
        splitter.addWidget(panel_derecho)
        splitter.setSizes([320, 520])

        layout_principal.addWidget(splitter)

        if self.lista_terminos.count() > 0:
            self.lista_terminos.setCurrentRow(0)

        return page

    def filtrar_terminos(self, texto):
        texto = texto.lower()
        for i in range(self.lista_terminos.count()):
            item = self.lista_terminos.item(i)
            item.setHidden(texto not in item.text().lower())

    def mostrar_definicion(self, termino):
        if termino and termino in GLOSARIO_IA:
            self.titulo_label.setText(termino)
            contenido = GLOSARIO_IA[termino]
            
            # Usar setHtml para renderizar todo como formato web/HTML
            self.definicion_text.setHtml(contenido)

            # Mostrar el botón interactivo solo para "Sistema Inteligente"
            if termino == "Sistema Inteligente":
                self.btn_esquema_glosario.setVisible(True)
            else:
                self.btn_esquema_glosario.setVisible(False)
        else:
            self.titulo_label.setText("Selecciona un término")
            self.definicion_text.clear()
            self.btn_esquema_glosario.setVisible(False)

    # ---------------- 6. ENSAYO ----------------
    def crear_pagina_ensayo(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(30, 30, 30, 30)

        card = QFrame()
        card.setStyleSheet("background-color: white; border: 1px solid #E2E8F0; border-radius: 10px; padding: 25px;")
        card_layout = QVBoxLayout(card)

        ensayo_html = """
        <h1 style="color: #0F172A; font-size: 24px; margin-bottom: 15px; text-decoration: none;">La Encrucijada Algorítmica: Ética y Aspectos Sociales de la Inteligencia Artificial</h1>
        
        <h3 style="color: #2563EB; font-size: 18px; margin-top: 15px; text-decoration: none;">Introducción</h3>
        <p style="font-size: 16px; color: #334155; line-height: 1.6;">
        La inteligencia artificial (IA) ha dejado de ser una especulación de la ciencia ficción para convertirse en el motor invisible —y cada vez más evidente— de la sociedad contemporánea. Desde la automatización industrial y el diagnóstico médico hasta la moderación de contenido en redes sociales y la optimización de procesos judiciales, los algoritmos moldean la vida cotidiana a una velocidad sin precedentes. Sin embargo, este despliegue masivo genera una tensión fundamental: la capacidad técnica para desarrollar modelos de IA avanza significativamente más rápido que nuestra comprensión de sus implicaciones éticas y sociales. Analizar la inteligencia artificial desde una perspectiva moral no es un freno al progreso, sino una condición indispensable para asegurar que la tecnología responda a los valores colectivos de justicia, equidad y dignidad humana.
        </p>

        <h3 style="color: #2563EB; font-size: 18px; margin-top: 15px; text-decoration: none;">Los Sesgos Algorítmicos y la Reproducción de la Inequidad</h3>
        <p style="font-size: 16px; color: #334155; line-height: 1.6;">
        Uno de los mitos más persistentes en torno a la tecnología es la neutralidad del código. Los sistemas de aprendizaje automático no toman decisiones en un vacío abstracto; aprenden a partir de conjuntos de datos históricos que reflejan prejuicios, disparidades sistémicas y desigualdades culturales.<br><br>
        Cuando un algoritmo de selección de personal o de concesión de créditos se entrena con datos procedentes de décadas pasadas, tiende a replicar y amplificar patrones de discriminación de género, raza o nivel socioeconómico. La opacidad de muchos de estos sistemas —el denominado fenómeno de la «caja negra»— dificulta la auditoría y la rendición de cuentas, desplazando la responsabilidad humana hacia procesos automatizados de difícil impugnación.
        </p>

        <h3 style="color: #2563EB; font-size: 18px; margin-top: 15px; text-decoration: none;">El Impacto en el Empleo y la Redefinición del Trabajo</h3>
        <p style="font-size: 16px; color: #334155; line-height: 1.6;">
        En el plano socioeconómico, la automatización y la adopción de modelos generativos están transformando la estructura del mercado laboral. A diferencia de revoluciones industriales anteriores, que sustituyeron principalmente la fuerza física, la IA impacta directamente en tareas cognitivas, creativas y analíticas.
        </p>
        <ul style="font-size: 16px; color: #334155; line-height: 1.6;">
            <li><b>Desplazamiento laboral:</b> Profesiones en áreas como atención al cliente, redacción técnica, análisis financiero básico y programación de rutina experimentan una reestructuración acelerada.</li>
            <li><b>Brecha de habilidades:</b> La velocidad de transición sobrepasa la capacidad de adaptación de los sistemas educativos tradicionales, lo que corre el riesgo de polarizar el mercado entre una elite técnica altamente capacitada y una fuerza laboral precarizada.</li>
            <li><b>Precarización y supervisión:</b> Las plataformas basadas en IA para la gestión del trabajo flexible imponen ritmos intensivos de supervisión algorítmica, debilitando en ocasiones los derechos laborales consolidados.</li>
        </ul>

        <h3 style="color: #2563EB; font-size: 18px; margin-top: 15px; text-decoration: none;">Privacidad, Vigilancia y Autonomía Individual</h3>
        <p style="font-size: 16px; color: #334155; line-height: 1.6;">
        El modelo económico que sustenta a buena parte del desarrollo de la IA se basa en la extracción masiva de datos personales. La vigilancia comercial y estatal se ha profundizado a través de tecnologías como el reconocimiento facial, el análisis de comportamiento y el perfilado predictivo.<br><br>
        Esta recopilación continua de información no solo plantea riesgos evidentes para la privacidad, sino que condiciona la autonomía individual. Algoritmos diseñados para maximizar la atención del usuario manipulan la información que este consume, influyendo en la opinión pública, polarizando el debate político y erosionando la confianza en las instituciones democráticas.
        </p>

        <h3 style="color: #2563EB; font-size: 18px; margin-top: 15px; text-decoration: none;">Gobernanza, Regulación y Responsabilidad</h3>
        <p style="font-size: 16px; color: #334155; line-height: 1.6;">
        Ante estos desafíos, la comunidad internacional ha comenzado a articular marcos regulatorios normativos y éticos. Principios como la transparencia, la explicabilidad, la seguridad y la supervisión humana son hoy el eje central de normativas emergentes (como la Ley de Inteligencia Artificial de la Unión Europea y las recomendaciones de la UNESCO).
        </p>
        
        <table border="1" style="border-collapse: collapse; width: 100%; text-align: center; font-size: 15px; color: #334155; margin: 15px 0; border-color: #CBD5E1;">
            <tr style="background-color: #F1F5F9;">
                <th colspan="4" style="padding: 10px; color: #0F172A;">Ejes de la IA Responsable</th>
            </tr>
            <tr>
                <td style="padding: 10px;"><b>Transparencia y Auditoría</b></td>
                <td style="padding: 10px;"><b>Equidad Sin Sesgos</b></td>
                <td style="padding: 10px;"><b>Privacidad de Datos</b></td>
                <td style="padding: 10px;"><b>Control Humano</b></td>
            </tr>
        </table>

        <p style="font-size: 16px; color: #334155; line-height: 1.6;">
        El reto central radica en diseñar esquemas de gobernanza que protejan los derechos fundamentales sin asfixiar la innovación tecnológica ni acentuar la brecha entre los países desarrollados —que lideran la propiedad intelectual de la IA— y las naciones en desarrollo.
        </p>

        <h3 style="color: #2563EB; font-size: 18px; margin-top: 15px; text-decoration: none;">Conclusión</h3>
        <p style="font-size: 16px; color: #334155; line-height: 1.6;">
        La inteligencia artificial es un reflejo amplificado de la propia humanidad: contiene el potencial de resolver problemas globales complejos como el cambio climático o la medicina personalizada, pero también la capacidad de consolidar injusticias históricas. La dimensión ética de la IA no debe entenderse como un catálogo de prohibiciones, sino como un marco de diseño para garantizar que la tecnología se ponga al servicio de las personas. La construcción de un futuro donde la IA potencie el bienestar colectivo dependerá de la capacidad de los gobiernos, la industria y la sociedad civil para exigir transparencia, equidad y responsabilidad en cada etapa del desarrollo tecnológico.
        </p>
        """

        lbl_ensayo = QLabel(ensayo_html)
        lbl_ensayo.setWordWrap(True)
        lbl_ensayo.setStyleSheet("border: none;")

        card_layout.addWidget(lbl_ensayo)
        layout.addWidget(card)

        scroll.setWidget(content)
        return scroll

    # ---------------- 7. PROYECTO PRÁCTICO DE SISTEMA INTELIGENTE ----------------
    def crear_pagina_proyecto(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(30, 30, 30, 30)

        card = QFrame()
        card.setStyleSheet("background-color: white; border: 1px solid #E2E8F0; border-radius: 10px; padding: 25px;")
        card_layout = QVBoxLayout(card)

        proyecto_html = """
        <h1 style="color: #0F172A; font-size: 26px; margin-bottom: 12px; text-decoration: none;">Caso Práctico: Sistema Inteligente de Prevención de Fugas de Agua (AquaGuard AI)</h1>
        
        <p style="font-size: 16px; color: #334155; line-height: 1.6;">
        Este proyecto ilustra la implementación de un <b>Sistema Inteligente</b> aplicado al hogar conectado (IoT). 
        A continuación, se detalla el ciclo completo alineado con las fases del esquema: <b>Entradas, Procesamiento de Datos y Solución/Acciones</b>.
        </p>

        <hr style="border: none; border-top: 1px solid #E2E8F0; margin: 20px 0;">

        <!-- 1. ENTRADAS -->
        <div style="background-color: #F0F9FF; border-left: 4px solid #0EA5E9; padding: 18px; border-radius: 6px; margin-bottom: 20px;">
            <h3 style="color: #0369A1; font-size: 19px; margin-top: 0; margin-bottom: 8px; text-decoration: none;">📥 1. ENTRADAS (Sensores y Datos)</h3>
            <p style="font-size: 16px; color: #334155; line-height: 1.5; margin: 0;">
            El sistema recopila telemetría constante desde el entorno residencial:
            </p>
            <ul style="font-size: 16px; color: #334155; line-height: 1.6; margin-top: 8px; margin-bottom: 0;">
                <li><b>Sensor de Flujo Ultrasonido:</b> Mide el caudal de agua consumido en litros por minuto (L/min).</li>
                <li><b>Sensor de Humedad de Suelo (en tuberías):</b> Registra presencia atípica de agua en paredes o pisos.</li>
                <li><b>Sensor de Presión de Agua:</b> Detecta caídas bruscas de presión en la tubería principal.</li>
                <li><b>Datos de Contexto (API Externa):</b> Calendario de ocupación de la vivienda y datos meteorológicos.</li>
            </ul>
        </div>

        <!-- 2. PROCESAMIENTO Y DATOS -->
        <div style="background-color: #F5F3FF; border-left: 4px solid #8B5CF6; padding: 18px; border-radius: 6px; margin-bottom: 20px;">
            <h3 style="color: #6D28D9; font-size: 19px; margin-top: 0; margin-bottom: 8px; text-decoration: none;">⚙ 2. DATOS Y PROCESAMIENTO (Modelo IA)</h3>
            <p style="font-size: 16px; color: #334155; line-height: 1.5; margin: 0;">
            El microcontrolador / servidor local procesa la información para determinar si existe una fuga real o solo un consumo alto normal:
            </p>
            <ul style="font-size: 16px; color: #334155; line-height: 1.6; margin-top: 8px; margin-bottom: 0;">
                <li><b>Preprocesamiento:</b> Filtrado de picos espurios o variaciones normales del uso doméstico.</li>
                <li><b>Detección de Anomalías (Modelo de Machine Learning):</b> Algoritmo de <i>Isolation Forest</i> o <i>Autoencoder</i> preentrenado con patrones históricos del usuario.</li>
                <li><b>Evaluación de Reglas de Inferencia:</b> Si el flujo constante supera los 15 minutos en horario nocturno (mientras los usuarios duermen) AND la humedad en piso aumenta 10%, el sistema eleva la alerta a <b>Nivel Crítico</b>.</li>
            </ul>
        </div>

        <!-- 3. SOLUCIÓN Y SALIDA -->
        <div style="background-color: #ECFDF5; border-left: 4px solid #10B981; padding: 18px; border-radius: 6px; margin-bottom: 20px;">
            <h3 style="color: #047857; font-size: 19px; margin-top: 0; margin-bottom: 8px; text-decoration: none;">🎯 3. SOLUCIÓN Y ACCIONES (Respuesta Autónoma)</h3>
            <p style="font-size: 16px; color: #334155; line-height: 1.5; margin: 0;">
            El sistema ejecuta una solución preventiva directa para mitigar el daño material y económico:
            </p>
            <ul style="font-size: 16px; color: #334155; line-height: 1.6; margin-top: 8px; margin-bottom: 0;">
                <li><b>Cierre de Electro-válvula (Actuador):</b> Corta el suministro general de agua de forma autónoma en menos de 3 segundos.</li>
                <li><b>Notificación de Emergencia:</b> Envía una alerta de alta prioridad a la aplicación móvil del usuario con el diagnóstico (ej. <i>"Posible fuga detectada en baño secundario"</i>).</li>
                <li><b>Retroalimentación (Learning Loop):</b> Si el usuario reabre la válvula desde la app confirmando un falso positivo (ej. llenando una alberca), el modelo recalibra sus umbrales para aprender el nuevo hábito.</li>
            </ul>
        </div>

        <!-- TABLA RESUMEN -->
        <h3 style="color: #0F172A; font-size: 20px; margin-top: 25px; margin-bottom: 12px; text-decoration: none;">Resumen Arquitectónico del Proyecto</h3>
        <table border="1" style="border-collapse: collapse; width: 100%; text-align: left; font-size: 15px; color: #334155; margin-bottom: 10px; border-color: #CBD5E1;">
            <tr style="background-color: #F1F5F9; color: #0F172A;">
                <th style="padding: 12px;">Componente</th>
                <th style="padding: 12px;">Tecnología / Dispositivo</th>
                <th style="padding: 12px;">Función en el Sistema</th>
            </tr>
            <tr>
                <td style="padding: 10px;"><b>Entradas</b></td>
                <td style="padding: 10px;">Sensor YF-S201 / ESP32 IoT</td>
                <td style="padding: 10px;">Captura de flujo e higrometría continua.</td>
            </tr>
            <tr>
                <td style="padding: 10px;"><b>Procesamiento</b></td>
                <td style="padding: 10px;">Python + Scikit-Learn / TensorFlow Lite</td>
                <td style="padding: 10px;">Clasificación de anomalías y cálculo de riesgo.</td>
            </tr>
            <tr>
                <td style="padding: 10px;"><b>Solución</b></td>
                <td style="padding: 10px;">Válvula solenoide 12V + Firebase Push API</td>
                <td style="padding: 10px;">Corte de flujo automático y notificación al usuario.</td>
            </tr>
        </table>
        """

        lbl_proyecto = QLabel(proyecto_html)
        lbl_proyecto.setWordWrap(True)
        lbl_proyecto.setStyleSheet("border: none;")

        card_layout.addWidget(lbl_proyecto)
        layout.addWidget(card)

        scroll.setWidget(content)
        return scroll


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    app.setStyleSheet("""
        QWidget {
            font-family: 'Segoe UI', sans-serif;
            background-color: #F8FAFC;
            color: #0F172A;
        }
        QLabel, a, h1, h2, h3, h4, h5, h6 {
            text-decoration: none;
        }
        #Sidebar {
            background-color: #0F172A;
        }
        #Sidebar QPushButton {
            background-color: transparent;
            color: #94A3B8;
            border: none;
            border-radius: 6px;
            padding: 12px 14px;
            font-size: 16px;
            text-align: left;
            text-decoration: none;
        }
        #Sidebar QPushButton:hover {
            background-color: #1E293B;
            color: #F8FAFC;
        }
        #Sidebar QPushButton:checked {
            background-color: #2563EB;
            color: #FFFFFF;
            font-weight: bold;
        }
        QLineEdit {
            padding: 10px 14px;
            border: 1px solid #CBD5E1;
            border-radius: 6px;
            background-color: #FFFFFF;
            color: #0F172A;
            font-size: 16px;
            margin-bottom: 8px;
        }
        QListWidget {
            border: 1px solid #CBD5E1;
            border-radius: 6px;
            background-color: #FFFFFF;
            outline: none;
        }
        QListWidget::item {
            padding: 10px 12px;
            border-bottom: 1px solid #F1F5F9;
            color: #1E293B;
            font-size: 15px;
            text-decoration: none;
        }
        QListWidget::item:selected {
            background-color: #2563EB;
            color: #FFFFFF;
            font-weight: bold;
        }
        QScrollBar:vertical {
            border: none;
            background: #F1F5F9;
            width: 10px;
            border-radius: 5px;
        }
        QScrollBar::handle:vertical {
            background: #94A3B8;
            border-radius: 5px;
        }
    """)

    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
