# 🚀 Configuración del Repositorio GitHub

## Pasos para subir ScriptCoach a GitHub

### 1. Crear el repositorio en GitHub
1. Ve a: https://github.com/new
2. **Repository name:** `scriptcoach`
3. **Description:** `AI-powered script generator for social media content (Reels/Shorts/TikTok)`
4. **Visibility:** Public (recomendado)
5. **NO** marques ninguna opción adicional
6. Haz clic en **"Create repository"**

### 2. Conectar el repositorio local con GitHub

Una vez creado el repositorio, ejecuta estos comandos:

```bash
# Reemplaza 'TU-USUARIO' con tu nombre de usuario de GitHub
git remote add origin https://github.com/TU-USUARIO/scriptcoach.git

# Subir el código
git push -u origin main
```

### 3. Verificar que todo esté subido

```bash
# Verificar el estado
git status

# Verificar el remoto
git remote -v
```

### 4. Configuración adicional (opcional)

```bash
# Agregar descripción al repositorio
# Ve a Settings > General > Description en GitHub

# Configurar topics (etiquetas)
# Ve a la página principal del repositorio y haz clic en "Add topics"
# Sugeridos: python, flask, ai, openai, social-media, content-creation
```

## 🎯 Estructura del Repositorio

```
scriptcoach/
├── app.py                 # Aplicación Flask principal
├── script_processor.py    # Lógica de procesamiento y IA
├── requirements.txt       # Dependencias de Python
├── templates/
│   └── index.html        # Interfaz web
├── README.md             # Documentación principal
├── LICENSE              # Licencia MIT
├── .gitignore           # Archivos a ignorar
├── config.example       # Ejemplo de configuración
└── ejemplos_uso.md      # Ejemplos de uso
```

## 🔧 Configuración para Usuarios

Los usuarios que clonen el repositorio deberán:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/TU-USUARIO/scriptcoach.git
   cd scriptcoach
   ```

2. **Crear entorno virtual:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # macOS/Linux
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar API key:**
   - Crear archivo `.env`
   - Agregar tu API key de DeepSeek

5. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```

## 🎉 ¡Listo!

Una vez completados estos pasos, tu proyecto ScriptCoach estará disponible en GitHub y otros desarrolladores podrán contribuir o usar tu código.
