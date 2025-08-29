import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QStackedWidget, QGridLayout, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from sintetizador import SintetizadorVoz
from silla_ruedas import SillaRuedas
from leerclics import MonitorPuntero
import threading


class MainWindow(QWidget):
   def __init__(self):
       super().__init__()
       self.sintetizador = SintetizadorVoz()
       self.silla_ruedas = SillaRuedas()
       self.setWindowTitle('Control Domótico')
       self.setGeometry(100, 100, 1920, 1080)  # Tamaño de la interfaz a 1920x1080


       # Crear Stacked Widget para alternar entre interfaces
       self.stack = QStackedWidget(self)


       # Crear las interfaces principales (Domótica, Movimiento, Configuración, Focos, Hora)
       self.create_main_menu()
       self.create_domotica_menu()
       self.create_movimiento_menu()  # Ajuste en este menú
       self.create_config_menu()
       self.create_focos_menu()
       self.create_hora_menu()
       self.create_youtube_menu() 


       # Mostrar el menú principal inicialmente
       self.stack.setCurrentIndex(0)


       # Layout para la ventana
       layout = QVBoxLayout()
       layout.addWidget(self.stack)
       self.setLayout(layout)
       self.monitor= MonitorPuntero(tiempo_espera=2)
       hilo = threading.Thread(target=self.monitor.iniciar)
       hilo.start() 


   def create_main_menu(self):
       # Menú principal con botones
       menu_widget = QWidget()
       layout = QGridLayout()


       # Configurar estilo de los botones
       button_style = "font-size: 24px; padding: 20px;"


       # Botón Domótica
       btn_domotica = QPushButton('Domótica')
       btn_domotica.setStyleSheet(button_style)
       btn_domotica.setIcon(QIcon('icons/domotica_icon.png'))
       btn_domotica.clicked.connect(lambda: self.stack.setCurrentIndex(1))
       btn_domotica.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_domotica, 0, 0)


       # Botón Movimiento
       btn_movimiento = QPushButton('Movimiento')
       btn_movimiento.setStyleSheet(button_style)
       btn_movimiento.setIcon(QIcon('icons/movimiento_icon.png'))
       btn_movimiento.clicked.connect(lambda: self.stack.setCurrentIndex(2))
       btn_movimiento.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_movimiento, 0, 1)


       # Botón Configuración
       btn_config = QPushButton('Configuración')
       btn_config.setStyleSheet(button_style)
       btn_config.setIcon(QIcon('icons/configuracion_icon.png'))
       btn_config.clicked.connect(lambda: self.stack.setCurrentIndex(3))
       btn_config.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_config, 1, 0)


       # Botón Emergencia
       btn_emergencia = QPushButton('Emergencia')
       btn_emergencia.setStyleSheet("font-size: 24px; padding: 20px;")
       btn_emergencia.setIcon(QIcon('icons/emergencia_icon.png'))
       btn_emergencia.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_emergencia, 1, 1)
       btn_emergencia.clicked.connect(lambda: self.sintetizador.hablar("   AAlexa, llama a Doctor Carlos Reyes.",120.0))
       


       menu_widget.setLayout(layout)
       self.stack.addWidget(menu_widget)


   def create_domotica_menu(self):
       domotica_widget = QWidget()
       layout = QGridLayout()

       # Botón Clima
       btn_clima = QPushButton('Clima en San Andrés Cholula, Puebla')
       btn_clima.setStyleSheet("font-size: 20px; padding: 20px;")
       btn_clima.setIcon(QIcon('icons/clima_icon.png'))
       btn_clima.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_clima, 0, 0)
       btn_clima.clicked.connect(lambda: self.sintetizador.hablar("   AAlexa, ¿Cual es el clima de San Andres, Cholula?.", 120.0))

       # Botón Focos
       btn_focos = QPushButton('Focos')
       btn_focos.setStyleSheet("font-size: 20px; padding: 20px;")
       btn_focos.setIcon(QIcon('icons/lightbulb_icon.png'))
       btn_focos.clicked.connect(lambda: self.stack.setCurrentIndex(4))
       btn_focos.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_focos, 1, 0)

       # Botón YouTube
       btn_youtube = QPushButton('YouTube')
       btn_youtube.setStyleSheet("font-size: 20px; padding: 20px;")
       btn_youtube.setIcon(QIcon('icons/youtube_icon.png'))
       btn_youtube.clicked.connect(lambda: self.stack.setCurrentIndex(6))  # Índice para el menú de YouTube
       btn_youtube.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_youtube, 2, 0)

       # Botón Horas
       btn_horas = QPushButton('Horas')
       btn_horas.setStyleSheet("font-size: 20px; padding: 20px;")
       btn_horas.setIcon(QIcon('icons/time_icon.png'))
       btn_horas.clicked.connect(lambda: self.stack.setCurrentIndex(5))
       btn_horas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_horas, 3, 0)

       # Botón Regresar
       btn_back = QPushButton('Regresar')
       btn_back.setStyleSheet("font-size: 24px; padding: 20px;")
       btn_back.setIcon(QIcon('icons/back_icon.png'))
       btn_back.clicked.connect(lambda: self.stack.setCurrentIndex(0))
       btn_back.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_back, 4, 0)

       domotica_widget.setLayout(layout)
       self.stack.addWidget(domotica_widget)

   def create_youtube_menu(self):
       youtube_widget = QWidget()
       layout = QGridLayout()

       # Crear 12 botones para canales de YouTube
       canales_youtube = [
           ("Canal 1", "   AAlexa, abre Canal Hola soy German en YouTube."),
           ("Canal 2", "   AAlexa, abre Canal Fernanflo en YouTube."),
           ("Canal 3", "   AAlexa, abre Canal Julio Profe en YouTube."),
           ("Canal 4", "   AAlexa, abre Canal Dalas Review en YouTube."),
           ("Canal 5", "   AAlexa, abre Canal FEDEWOLF en YouTube."),
           ("Canal 6", "   AAlexa, abre Canal LA COTORRISA en YouTube."),
           ("Canal 7", "   AAlexa, abre Canal LA CAPITAL en YouTube."),
           ("Canal 8", "   AAlexa, abre Canal FARIDIEK en YouTube."),
           ("Canal 9", "   AAlexa, abre Canal YAIRH 17en YouTube."),
           ("Canal 10", "   AAlexa, abre Canal TODOPROGRAMADOR en YouTube."),
           ("Canal 11", "   AAlexa, abre Canal EL MARIANA en YouTube."),
           ("Canal 12", "   AAlexa, abre Canal VEGETA777 en YouTube.")
       ]

       # Añadir botones al menú
       for i, (nombre, comando) in enumerate(canales_youtube):
           btn = QPushButton(nombre)
           btn.setStyleSheet("font-size: 20px; padding: 20px;")
           btn.clicked.connect(lambda _, c=comando: self.sintetizador.hablar(c, 120.0))
           btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
           layout.addWidget(btn, i // 3, i % 3)

       # Botón Regresar
       btn_back = QPushButton('Regresar')
       btn_back.setStyleSheet("font-size: 24px; padding: 20px;")
       btn_back.setIcon(QIcon('icons/back_icon.png'))
       btn_back.clicked.connect(lambda: self.stack.setCurrentIndex(1))
       btn_back.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_back, 4, 0, 1, 3)

       youtube_widget.setLayout(layout)
       self.stack.addWidget(youtube_widget)


    

    

   def create_movimiento_menu(self):
       # Menú de Movimiento ajustado
       movimiento_widget = QWidget()
       layout = QGridLayout()


       button_style = "font-size: 24px; padding: 20px;"


       # Botón Adelante
       btn_adelante = QPushButton('Adelante')
       btn_adelante.setStyleSheet(button_style)
       btn_adelante.setIcon(QIcon('icons/adelante_icon.png'))
       btn_adelante.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_adelante, 0, 1)
       btn_adelante.pressed.connect(lambda: self.silla_ruedas.mover(319,426,319,426))
       btn_adelante.released.connect(lambda: self.silla_ruedas.parar())




       # Botón Atrás
       btn_atras = QPushButton('Atrás')
       btn_atras.setStyleSheet(button_style)
       btn_atras.setIcon(QIcon('icons/atras_icon.png'))
       btn_atras.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_atras, 2, 1)
       btn_atras.pressed.connect(lambda: self.silla_ruedas.mover(324,849,324,849,))
       btn_atras.released.connect(lambda: self.silla_ruedas.parar())



       # Botón Izquierda
       btn_izquierda = QPushButton('Izquierda')
       btn_izquierda.setStyleSheet(button_style)
       btn_izquierda.setIcon(QIcon('icons/izquierda_icon.png'))
       btn_izquierda.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_izquierda, 1, 0)
       btn_izquierda.pressed.connect(lambda: self.silla_ruedas.mover(1803,847,1803,847))
       btn_izquierda.released.connect(lambda: self.silla_ruedas.parar())




       # Botón Derecha
       btn_derecha = QPushButton('Derecha')
       btn_derecha.setStyleSheet(button_style)
       btn_derecha.setIcon(QIcon('icons/derecha_icon.png'))
       btn_derecha.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_derecha, 1, 2)
       btn_derecha.pressed.connect(lambda: self.silla_ruedas.mover(2236,833,2236,833))
       btn_derecha.released.connect(lambda: self.silla_ruedas.parar())


       # Botón Regresar
       btn_back = QPushButton('Regresar')
       btn_back.setStyleSheet(button_style)
       btn_back.setIcon(QIcon('icons/back_icon.png'))
       btn_back.clicked.connect(lambda: self.stack.setCurrentIndex(0))
       btn_back.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_back, 3, 0, 1, 3)


       movimiento_widget.setLayout(layout)
       self.stack.addWidget(movimiento_widget)

   def create_config_menu(self):
       config_widget = QWidget()
       layout = QGridLayout()


       button_style = "font-size: 24px; padding: 20px;"


       # Botones de configuración
       btn_vel_silla = QPushButton('Velocidad de Silla')
       btn_vel_silla.setStyleSheet(button_style)
       btn_vel_silla.setIcon(QIcon('icons/vel_silla_icon.png'))
       btn_vel_silla.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_vel_silla, 0, 0)


       btn_vol_voz = QPushButton('Volumen de Voz')
       btn_vol_voz.setStyleSheet(button_style)
       btn_vol_voz.setIcon(QIcon('icons/vol_voz_icon.png'))
       btn_vol_voz.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_vol_voz, 0, 1)


       btn_vel_habla = QPushButton('Velocidad de Habla')
       btn_vel_habla.setStyleSheet(button_style)
       btn_vel_habla.setIcon(QIcon('icons/vel_habla_icon.png'))
       btn_vel_habla.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_vel_habla, 1, 0)


       btn_cambiar_voz = QPushButton('Cambiar Voz')
       btn_cambiar_voz.setStyleSheet(button_style)
       btn_cambiar_voz.setIcon(QIcon('icons/cambiar_voz_icon.png'))
       btn_cambiar_voz.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_cambiar_voz, 1, 1)


       # Botón Regresar
       btn_back = QPushButton('Regresar')
       btn_back.setStyleSheet(button_style)
       btn_back.setIcon(QIcon('icons/back_icon.png'))
       btn_back.clicked.connect(lambda: self.stack.setCurrentIndex(0))
       layout.addWidget(btn_back, 2, 0, 1, 2)


       config_widget.setLayout(layout)
       self.stack.addWidget(config_widget)


   def create_focos_menu(self):
       focos_widget = QWidget()
       layout = QGridLayout()


       # Botón Encender Focos
       btn_encender_focos = QPushButton('Encender Focos')
       btn_encender_focos.setStyleSheet("font-size: 20px; padding: 20px;")
       btn_encender_focos.setIcon(QIcon('icons/encender_icon.png'))
       btn_encender_focos.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_encender_focos, 0, 0)
       btn_encender_focos.clicked.connect(lambda: self.sintetizador.hablar("   AAlexa, ENCIENDE SMART BOLT 2.", 120.0))



       # Botón Apagar Focos
       btn_apagar_focos = QPushButton('Apagar Focos')
       btn_apagar_focos.setStyleSheet("font-size: 20px; padding: 20px;")
       btn_apagar_focos.setIcon(QIcon('icons/apagar_icon.png'))
       btn_apagar_focos.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_apagar_focos, 1, 0)
       btn_encender_focos.clicked.connect(lambda: self.sintetizador.hablar("   AAlexa, APAGA SMART BOLT 2.", 120.0))


       # Botón Regresar
       btn_back = QPushButton('Regresar')
       btn_back.setStyleSheet("font-size: 24px; padding: 20px;")
       btn_back.setIcon(QIcon('icons/back_icon.png'))
       btn_back.clicked.connect(lambda: self.stack.setCurrentIndex(1))
       btn_back.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_back, 2, 0)


       focos_widget.setLayout(layout)
       self.stack.addWidget(focos_widget)


   def create_hora_menu(self):
       hora_widget = QWidget()
       layout = QGridLayout()
       # Botón para mostrar la hora en diferentes ciudades
       btn_horaMexico = QPushButton('Hora en Ciudad de México')
       btn_horaMexico.setStyleSheet("font-size: 24px; padding: 20px;")
       btn_horaMexico.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_horaMexico, 0, 0)
       btn_horaMexico.clicked.connect(lambda: self.sintetizador.hablar("   AAlexa, CUAL ES EL HORARIO EN CIUDAD DE MEXICO, MEXICO", 120.0))


       btn_horaCanada = QPushButton('Hora en Toronto, Canadá')
       btn_horaCanada.setStyleSheet("font-size: 24px; padding: 20px;")
       btn_horaCanada.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_horaCanada, 1, 0)
       btn_horaCanada.clicked.connect(lambda: self.sintetizador.hablar("   AAlexa, CUAL ES EL HORARIO EN CIUDAD DE OTAWA, CANADA", 120.0))


       btn_horaChina = QPushButton('Hora en Pekín, China')
       btn_horaChina.setStyleSheet("font-size: 24px; padding: 20px;")
       btn_horaChina.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_horaChina, 2, 0)
       btn_horaCanada.clicked.connect(lambda: self.sintetizador.hablar("   AAlexa, CUAL ES EL HORARIO EN CIUDAD DE PEKIN, CHINA", 120.0))



       # Botón Regresar
       btn_back = QPushButton('Regresar')
       btn_back.setStyleSheet("font-size: 24px; padding: 20px;")
       btn_back.setIcon(QIcon('icons/back_icon.png'))
       btn_back.clicked.connect(lambda: self.stack.setCurrentIndex(1))
       btn_back.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
       layout.addWidget(btn_back)


       hora_widget.setLayout(layout)
       self.stack.addWidget(hora_widget)





# Código para ejecutar la aplicación
if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec_())
