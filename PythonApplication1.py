import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, 
    QLineEdit, QListWidget, QTextEdit, QLabel, QSplitter,
    QStackedWidget, QPushButton, QFrame, QScrollArea
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

# Datos del Glosario extraídos de la versión previa
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
    "Agentes de IA": "Sistemas autónomos construidos sobre modelos de lenguaje capaces de percibir su entorno, tomar decisiones dinámicas y ejecutar secuencias de tareas para lograr un objetivo específico."
}


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Explorador de Inteligencia Artificial')
        self.resize(1000, 650)

        # Layout Principal (Barra lateral de menú + Contenido variable)
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ---------------- Barra Lateral (Menú de Navegación) ----------------
        sidebar = QFrame()
        sidebar.setObjectName("Sidebar")
        sidebar.setFixedWidth(220)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(10, 20, 10, 20)
        sidebar_layout.setSpacing(10)

        title_menu = QLabel("MENÚ IA")
        title_menu.setStyleSheet("font-size: 16px; font-weight: bold; color: #94A3B8; margin-bottom: 10px; padding-left: 5px;")
        sidebar_layout.addWidget(title_menu)

        self.btn_inicio = QPushButton("🏠 Inicio")
        self.btn_ramas = QPushButton("🌳 Ramas de la IA")
        self.btn_clasificacion = QPushButton("📊 Clasificación")
        self.btn_timeline = QPushButton("⏳ Línea del Tiempo")
        self.btn_glosario = QPushButton("📖 Glosario")

        self.botones_menu = [self.btn_inicio, self.btn_ramas, self.btn_clasificacion, self.btn_timeline, self.btn_glosario]

        for index, btn in enumerate(self.botones_menu):
            btn.setCheckable(True)
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, idx=index: self.cambiar_pagina(idx))
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()
        main_layout.addWidget(sidebar)

        # ---------------- Contenedor Dinámico (Stacked Widget) ----------------
        self.stack = QStackedWidget()

        # Agregar las 5 páginas a la pila
        self.stack.addWidget(self.crear_pagina_inicio())
        self.stack.addWidget(self.crear_pagina_ramas())
        self.stack.addWidget(self.crear_pagina_clasificacion())
        self.stack.addWidget(self.crear_pagina_timeline())
        self.stack.addWidget(self.crear_pagina_glosario())

        main_layout.addWidget(self.stack)

        # Seleccionar página 0 (Inicio) por defecto
        self.cambiar_pagina(0)

    def cambiar_pagina(self, index):
        self.stack.setCurrentIndex(index)
        for i, btn in enumerate(self.botones_menu):
            btn.setChecked(i == index)

    # ---------------- 1. PÁGINA DE INICIO ----------------
    def crear_pagina_inicio(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setAlignment(Qt.AlignTop)

        title = QLabel("Inteligencia Artificial")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #1E293B; margin-bottom: 20px;")
        
        card = QFrame()
        card.setStyleSheet("background-color: white; border: 1px solid #E2E8F0; border-radius: 10px; padding: 25px;")
        card_layout = QVBoxLayout(card)

        desc = QLabel(
            "La Inteligencia Artificial es un campo interdisciplinario dedicado al diseño de sistemas capaces "
            "de realizar tareas asociadas con la inteligencia humana, como aprender, razonar, reconocer patrones, "
            "comprender lenguaje, resolver problemas y tomar decisiones."
        )
        desc.setWordWrap(True)
        desc.setStyleSheet("font-size: 16px; line-height: 1.6; color: #334155; border: none;")

        card_layout.addWidget(desc)
        layout.addWidget(title)
        layout.addWidget(card)
        return page

    # ---------------- 2. PÁGINA DE RAMAS ----------------
    def crear_pagina_ramas(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("Ramas Disciplinares de la IA")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #1E293B; margin-bottom: 15px;")
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
            card.setStyleSheet("background-color: white; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px; margin-bottom: 8px;")
            card_layout = QVBoxLayout(card)
            
            lbl_title = QLabel(f"• {rama}")
            lbl_title.setStyleSheet("font-size: 16px; font-weight: bold; color: #2563EB; border: none;")
            
            lbl_desc = QLabel(texto)
            lbl_desc.setWordWrap(True)
            lbl_desc.setStyleSheet("font-size: 14px; color: #475569; border: none;")

            card_layout.addWidget(lbl_title)
            card_layout.addWidget(lbl_desc)
            layout.addWidget(card)

        scroll.setWidget(content)
        return scroll

    # ---------------- 3. PÁGINA DE CLASIFICACIÓN (CON IMÁGENES) ----------------
    def crear_pagina_clasificacion(self):
        from PySide6.QtGui import QPixmap

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("Clasificación de Modelos de IA")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #1E293B; margin-bottom: 20px;")
        layout.addWidget(title)

        clasificaciones = [
            {
                "titulo": "IA Débil o Estrecha (Narrow AI - ANI)", 
                "desc": "Diseñada para resolver tareas específicas: traducción, recomendación, reconocimiento de imágenes, de voz o chat. Impulsa la mayor parte de la IA actual[cite: 4].",
                "img": "Imagenes/ani.jpg"
            },
            {
                "titulo": "IA Fuerte o General (AGI - General Artificial Intelligence)", 
                "desc": "Busca crear máquinas con inteligencia humana completa, capaces de realizar cualquier tarea intelectual. Es una categoría hipotética[cite: 3].",
                "img": "Imagenes/agi.jpg"
            },
            {
                "titulo": "IA Superinteligente (ASI)", 
                "desc": "Sistema hipotético que superaría a los humanos en todas las áreas cognitivas, siendo autoconsciente y con capacidad de planificación del futuro[cite: 2].",
                "img": "Imagenes/asi.jpg"
            }
        ]

        for item in clasificaciones:
            card = QFrame()
            card.setStyleSheet("background-color: white; border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px; margin-bottom: 20px;")
            card_layout = QVBoxLayout(card)

            lbl_type = QLabel(item["titulo"])
            lbl_type.setStyleSheet("font-size: 18px; font-weight: bold; color: #0F172A; border: none;")

            lbl_desc = QLabel(item["desc"])
            lbl_desc.setWordWrap(True)
            lbl_desc.setStyleSheet("font-size: 14px; color: #334155; margin-top: 5px; margin-bottom: 12px; border: none;")

            card_layout.addWidget(lbl_type)
            card_layout.addWidget(lbl_desc)

            # Cargar infografía correspondiente
            pixmap = QPixmap(item["img"])
            if not pixmap.isNull():
                lbl_img = QLabel()
                lbl_img.setPixmap(pixmap.scaledToWidth(750, Qt.SmoothTransformation))
                lbl_img.setAlignment(Qt.AlignCenter)
                lbl_img.setStyleSheet("border: none; margin-top: 5px;")
                card_layout.addWidget(lbl_img)
            else:
                lbl_error = QLabel(f"No se encontró la imagen: {item['img']}")
                lbl_error.setStyleSheet("color: #EF4444; font-size: 12px; border: none;")
                card_layout.addWidget(lbl_error)

            layout.addWidget(card)

        scroll.setWidget(content)
        return scroll

# ---------------- 4. PÁGINA DE LÍNEA DEL TIEMPO (CON INFOGRAFÍA) ----------------
    def crear_pagina_timeline(self):
        from PySide6.QtGui import QPixmap

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("Línea del Tiempo de la Inteligencia Artificial")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #1E293B; margin-bottom: 20px;")
        layout.addWidget(title)

        # Posibles nombres y formatos para la imagen
        opciones_ruta = [
            "Imagenes/Linea_del_tiempo.png",
            "Imagenes/Linea_del_tiempo.jpg",
            "Imagenes/linea_del_tiempo.png",
            "Imagenes/linea_del_tiempo.jpg"
        ]

        pixmap = QPixmap()
        ruta_encontrada = ""

        # Probar cada opción hasta encontrar el archivo exacto
        for ruta in opciones_ruta:
            pixmap = QPixmap(ruta)
            if not pixmap.isNull():
                ruta_encontrada = ruta
                break

        if not pixmap.isNull():
            lbl_img = QLabel()
            # Ajustamos el ancho a 800px para que el texto de la infografía sea legible
            lbl_img.setPixmap(pixmap.scaledToWidth(800, Qt.SmoothTransformation))
            lbl_img.setAlignment(Qt.AlignCenter)
            lbl_img.setStyleSheet("background-color: white; border: 1px solid #E2E8F0; border-radius: 8px; padding: 15px;")
            layout.addWidget(lbl_img)
        else:
            lbl_error = QLabel("⚠️ No se encontró la imagen de la línea del tiempo en la carpeta 'Imagenes'.\nAsegúrate de guardar el archivo como 'Linea_del_tiempo.png' o '.jpg'")
            lbl_error.setStyleSheet("color: #EF4444; font-size: 14px; font-weight: bold; padding: 20px; background-color: #FEE2E2; border-radius: 8px;")
            layout.addWidget(lbl_error)

        layout.addStretch()
        scroll.setWidget(content)
        return scroll

    # ---------------- 5. PÁGINA DEL GLOSARIO ----------------
    def crear_pagina_glosario(self):
        page = QWidget()
        layout_principal = QHBoxLayout(page)
        layout_principal.setContentsMargins(15, 15, 15, 15)

        splitter = QSplitter(Qt.Horizontal)

        # Panel Izquierdo (Buscador y Lista)
        panel_izquierdo = QWidget()
        panel_izquierdo.setMinimumWidth(280)
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

        # Panel Derecho (Detalle)
        panel_derecho = QWidget()
        layout_derecho = QVBoxLayout(panel_derecho)
        layout_derecho.setContentsMargins(10, 0, 0, 0)

        self.titulo_label = QLabel('Selecciona un término')
        self.titulo_label.setWordWrap(True)
        self.titulo_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #0F172A; margin-bottom: 8px;")
        layout_derecho.addWidget(self.titulo_label)

        self.definicion_text = QTextEdit()
        self.definicion_text.setReadOnly(True)
        self.definicion_text.setStyleSheet("font-size: 15px; color: #334155; border: 1px solid #CBD5E1; border-radius: 8px; padding: 15px;")
        layout_derecho.addWidget(self.definicion_text)

        splitter.addWidget(panel_izquierdo)
        splitter.addWidget(panel_derecho)
        splitter.setSizes([280, 500])

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
            self.definicion_text.setText(GLOSARIO_IA[termino])
        else:
            self.titulo_label.setText("Selecciona un término")
            self.definicion_text.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    app.setStyleSheet("""
        QWidget {
            font-family: 'Segoe UI', sans-serif;
            background-color: #F8FAFC;
            color: #0F172A;
        }
        #Sidebar {
            background-color: #0F172A;
        }
        #Sidebar QPushButton {
            background-color: transparent;
            color: #94A3B8;
            border: none;
            border-radius: 6px;
            padding: 10px 12px;
            font-size: 14px;
            text-align: left;
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
            padding: 8px 12px;
            border: 1px solid #CBD5E1;
            border-radius: 6px;
            background-color: #FFFFFF;
            color: #0F172A;
            font-size: 14px;
            margin-bottom: 5px;
        }
        QListWidget {
            border: 1px solid #CBD5E1;
            border-radius: 6px;
            background-color: #FFFFFF;
            outline: none;
        }
        QListWidget::item {
            padding: 8px 10px;
            border-bottom: 1px solid #F1F5F9;
            color: #1E293B;
        }
        QListWidget::item:selected {
            background-color: #2563EB;
            color: #FFFFFF;
            font-weight: bold;
        }
        QScrollBar:vertical {
            border: none;
            background: #F1F5F9;
            width: 8px;
            border-radius: 4px;
        }
        QScrollBar::handle:vertical {
            background: #94A3B8;
            border-radius: 4px;
        }
    """)

    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())