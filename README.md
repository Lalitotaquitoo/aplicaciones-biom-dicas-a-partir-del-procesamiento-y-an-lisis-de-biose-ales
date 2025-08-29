# Sistema de Control Domótico y Movilidad

Este proyecto es una interfaz de control domótico y de movilidad diseñada para personas con discapacidad motriz. Combina control de dispositivos inteligentes, movilidad de silla de ruedas y síntesis de voz en una aplicación intuitiva.

## Características Principales

### 🏠 Control Domótico
- Control de focos inteligentes (encender/apagar)
- Consulta del clima en San Andrés Cholula, Puebla
- Control de contenido de YouTube mediante comandos de voz
- Consulta de hora en diferentes ciudades del mundo

### 🦽 Control de Movilidad
- Control direccional de silla de ruedas (adelante, atrás, izquierda, derecha)
- Botón de parada de emergencia
- Comandos mediante interfaz táctil

### 🗣️ Síntesis de Voz
- Interacción con Alexa mediante comandos de voz predefinidos
- Configuración de velocidad y volumen de voz
- Selección de diferentes voces disponibles

### 👆 Sistema de Seguimiento Ocular
- Detección de permanencia del puntero para realizar clics automáticos
- Interacción sin necesidad de click físico

## Estructura del Proyecto

```
.
├── sintetizador.py      # Módulo de síntesis de voz
├── silla_ruedas.py      # Control de movilidad de silla
├── leerclics.py         # Sistema de seguimiento de puntero
└── PRUEBA INTERFAZ.py   # Interfaz gráfica principal
```

## Requisitos del Sistema

### Dependencias de Python
- PyQt5
- pyttsx3
- pyautogui

Instalar dependencias:
```bash
pip install PyQt5 pyttsx3 pyautogui
```

### Requisitos de Hardware/Software
- Dispositivo Android conectado vía ADB para control de silla
- Acceso a Internet para comandos de Alexa
- Sistema operativo Windows, macOS o Linux

## Instalación y Uso

1. Clona o descarga los archivos del proyecto
2. Instala las dependencias necesarias
3. Conecta tu dispositivo Android vía ADB
4. Ejecuta la aplicación principal:
```bash
python "PRUEBA INTERFAZ.py"
```

## Configuración

### Control de Silla de Ruedas
- Asegúrate de tener ADB instalado y configurado
- Conecta el dispositivo Android antes de ejecutar la aplicación
- Los comandos de movimiento se envían mediante ADB

### Comandos de Voz
- La aplicación utiliza síntesis de voz para interactuar con Alexa
- Los comandos están predefinidos para diferentes funcionalidades

### Interfaz de Usuario
- Diseñada para ser accesible con botones grandes y claros
- Navegación intuitiva entre diferentes secciones
- Feedback visual y auditivo para todas las acciones

## Funcionalidades Detalladas

### Menú Principal
- **Domótica**: Control de dispositivos inteligentes
- **Movimiento**: Control de la silla de ruedas
- **Configuración**: Ajustes de voz y silla
- **Emergencia**: Contacto rápido con médico

### Sección Domótica
- Consulta del clima local
- Control de focos inteligentes
- Acceso a canales de YouTube
- Consulta de hora en diferentes ciudades

### Sección Movimiento
- Control direccional completo
- Botones grandes para fácil acceso
- Funcionamiento con press/release para control continuo

## Personalización

### Comandos de Alexa
Puedes modificar los comandos de voz editando las cadenas de texto en los métodos correspondientes en `PRUEBA INTERFAZ.py`.

### Configuración de Voz
En la sección de configuración puedes ajustar:
- Velocidad de habla
- Volumen de voz
- Tipo de voz (según las disponibles en el sistema)

## Solución de Problemas

### ADB no detecta dispositivo
- Verifica la conexión USB
- Habilita la depuración USB en el dispositivo Android
- Ejecuta `adb devices` para confirmar la conexión

### Problemas de audio
- Verifica que los controladores de audio estén instalados
- Comprueba que el volumen del sistema no esté silenciado

### La interfaz no se muestra correctamente
- Asegúrate de tener todas las dependencias instaladas
- Verifica la resolución de pantalla (optimizado para 1920x1080)

## Contribuciones

Las contribuciones son bienvenidas. Puedes:
- Reportar bugs o problemas
- Sugerir nuevas funcionalidades
- Contribuir con mejoras de código

## Licencia

Este proyecto es de uso libre para fines educativos y de asistencia.

## Contacto

Para más información o soporte técnico, por favor contacta al equipo de desarrollo.

---

**Nota**: Esta aplicación está diseñada como prototipo para asistencia a personas con discapacidad motriz. Siempre prueba los controles de seguridad antes de su uso en entornos reales.
