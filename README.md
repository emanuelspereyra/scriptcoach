# 🎬 ScriptCoach

**Asistente experto en crear guiones listos para grabar** para Reels/Shorts/TikTok de marca personal.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-1.99.9-purple.svg)](https://openai.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Transforma mensajes de WhatsApp en guiones profesionales con detección inteligente de nicho y generación con IA.

## 🚀 Características

- **Parsing inteligente** de mensajes de WhatsApp
- **Validación automática** de emails
- **Generación con IA** usando DeepSeek
- **JSON estructurado** completo para envío por email
- **Resumen optimizado** para WhatsApp
- **Interfaz web moderna** y responsive

## 📋 Requisitos

- Python 3.8+
- pip (gestor de paquetes de Python)

## 🚀 Instalación Rápida

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/scriptcoach.git
cd scriptcoach

# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python app.py
```

## 🛠️ Instalación Detallada

1. **Clona el repositorio**
```bash
git clone https://github.com/tu-usuario/scriptcoach.git
cd scriptcoach
```

2. **Instala las dependencias**
```bash
pip install -r requirements.txt
```

3. **Ejecuta la aplicación**
```bash
python app.py
```

4. **Abre tu navegador**
```
http://localhost:5000
```

## 📱 Cómo usar

### 1. Interfaz Web
- Abre la aplicación en tu navegador
- Pega el mensaje de WhatsApp en el campo de texto
- Haz clic en "🚀 Generar Guión"
- Copia el resumen para WhatsApp y el JSON completo

### 2. API REST
```bash
curl -X POST http://localhost:5000/api/process-message \
  -H "Content-Type: application/json" \
  -d '{"message": "Mi email es usuario@ejemplo.com. Necesito un guión sobre marketing digital para TikTok, 60 segundos, tono amigable."}'
```

## 📝 Formato del Mensaje

El mensaje debe incluir:

**Obligatorio:**
- `email`: Dirección de email válida

**Opcionales (se detectan automáticamente):**
- `tema`: Tema del contenido
- `objetivo`: awareness | leadgen | venta | autoridad (default: autoridad)
- `plataforma`: reels | tiktok | shorts | youtube | podcast (default: reels)
- `duración`: 30 | 45 | 60 | 90 segundos (default: 60)
- `tono`: directo | amigable | humor | profesional (default: directo)
- `contexto`: Información adicional

### Ejemplos de mensajes:

```
"Hola! Mi email es usuario@ejemplo.com. Necesito un guión sobre marketing digital para TikTok, 60 segundos, tono amigable. Quiero generar leads."
```

```
"Email: maria@empresa.com
Tema: Productividad en el trabajo
Plataforma: reels
Duración: 45 segundos
Tono: profesional
Objetivo: autoridad"
```

## 📊 Estructura del JSON

El sistema genera un JSON completo con:

- **Meta**: Información del proyecto
- **Guión**: 5 secciones con tiempos específicos
- **Hooks alternativos**: 3 opciones de apertura
- **CTAs alternativas**: 2 opciones de cierre
- **B-roll**: Descripción de material de apoyo
- **Overlays**: Textos superpuestos
- **Copy de publicación**: Título, descripción y hashtags
- **Miniatura**: Sugerencias para thumbnail
- **Variantes extra**: Versiones de 30s y 90s
- **Lista de tomas**: Especificaciones técnicas
- **Checklist**: Preparación pre-grabación
- **A/B Testing**: Ideas para experimentar

## 🔧 Configuración

### Variables de Entorno
Crea un archivo `.env` (opcional):
```env
PORT=5000
OPENAI_API_KEY=tu-api-key-de-deepseek
OPENAI_API_BASE=https://api.deepseek.com/v1
```

> **Nota:** Para usar ScriptCoach, necesitas una API key de DeepSeek. Puedes obtenerla en [https://platform.deepseek.com/](https://platform.deepseek.com/)

### Personalización
- Modifica `script_processor.py` para ajustar el parsing
- Edita `templates/index.html` para cambiar la interfaz
- Ajusta los prompts en `generate_script_with_ai()` para diferentes estilos

## 🎯 Casos de Uso

### Para Agencias de Marketing
- Generar guiones para múltiples clientes
- Mantener consistencia en el tono de marca
- Optimizar para diferentes plataformas

### Para Creadores de Contenido
- Acelerar el proceso de creación
- Mantener estructura profesional
- Generar variantes para A/B testing

### Para Consultores
- Crear contenido de autoridad
- Generar leads cualificados
- Establecer expertise en nichos específicos

## 🚨 Manejo de Errores

- **Email inválido**: Devuelve error específico
- **Falta información**: Infiere valores por defecto
- **Error de IA**: Usa JSON de respaldo
- **Error de conexión**: Mensaje claro al usuario

## 🔒 Seguridad

- Validación de emails
- Sanitización de inputs
- Manejo seguro de API keys
- CORS configurado

## 📈 Próximas Mejoras

- [ ] Integración con WhatsApp Business API
- [ ] Sistema de templates personalizables
- [ ] Análisis de performance de guiones
- [ ] Exportación a diferentes formatos
- [ ] Dashboard de analytics

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Para contribuir:

1. **Fork** el proyecto
2. **Crea una rama** para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre un Pull Request**

### 🐛 Reportar Bugs

Si encuentras un bug, por favor:
- Abre un issue en GitHub
- Describe el problema detalladamente
- Incluye pasos para reproducir el error
- Adjunta logs si es posible

## 📄 Licencia

MIT License - ver archivo LICENSE para detalles.

## 🆘 Soporte

Si tienes problemas o preguntas:
- Abre un issue en GitHub
- Revisa la documentación
- Contacta al equipo de desarrollo

---

## 📋 Changelog

### v1.0.0 (2025-08-15)
- ✅ **Detección automática de nicho** (fitness, marketing, tech, etc.)
- ✅ **Integración con DeepSeek AI** para generación de guiones
- ✅ **Interfaz web moderna** con Flask
- ✅ **Parsing inteligente** de mensajes de WhatsApp
- ✅ **Validación de emails** automática
- ✅ **Manejo robusto de errores** con mensajes claros
- ✅ **Generación de JSON completo** para envío por email
- ✅ **Resumen optimizado** para WhatsApp

**ScriptCoach** - Transformando ideas en guiones profesionales 🎬
