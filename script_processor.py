import re
import json
from email_validator import validate_email, EmailNotValidError
from openai import OpenAI
import os

class ScriptProcessor:
    def __init__(self):
        try:
            # Configurar variables de entorno si no están seteadas
            if not os.getenv("OPENAI_API_KEY"):
                os.environ["OPENAI_API_KEY"] = "sk-ee5c7c3f1674411b89ae50b657489c43"
            if not os.getenv("OPENAI_API_BASE"):
                os.environ["OPENAI_API_BASE"] = "https://api.deepseek.com/v1"
            
            # Intentar inicializar el cliente con configuración mínima
            self.client = OpenAI(
                api_key=os.getenv("OPENAI_API_KEY"),
                base_url=os.getenv("OPENAI_API_BASE")
            )
            print("✅ OpenAI client initialized successfully")
        except Exception as e:
            print(f"Warning: Could not initialize OpenAI client: {e}")
            # Intentar con configuración alternativa
            try:
                self.client = OpenAI(
                    api_key=os.getenv("OPENAI_API_KEY")
                )
                print("✅ OpenAI client initialized with alternative config")
            except Exception as e2:
                print(f"Warning: Alternative initialization also failed: {e2}")
                self.client = None
    
    def validate_email(self, email):
        """Valida si el email es válido"""
        if not email:
            return False
            
        # Validación simple con regex
        email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        return bool(re.match(email_pattern, email))
    
    def parse_message(self, message):
        """Parsea el mensaje de WhatsApp y extrae los parámetros"""
        message_lower = message.lower()
        
        # Extraer email
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        email_match = re.search(email_pattern, message)
        email = email_match.group() if email_match else None
        
        # Extraer otros parámetros por palabras clave
        params = {
            'email': email,
            'tema': None,
            'nicho': 'marca personal',
            'objetivo': 'autoridad',
            'plataforma': 'reels',
            'duracion': 60,
            'tono': 'directo',
            'contexto': ''
        }
        
        # Detectar nicho automáticamente
        nicho_keywords = {
            'coaching': ['coach', 'coaching', 'entrenador', 'mentor'],
            'consultoría': ['consultor', 'consultoría', 'asesor', 'asesoría'],
            'fitness': ['fitness', 'ejercicio', 'gimnasio', 'deporte', 'salud'],
            'marketing': ['marketing', 'publicidad', 'ventas', 'negocio'],
            'tech': ['tecnología', 'programación', 'software', 'app', 'startup'],
            'educación': ['educación', 'enseñanza', 'curso', 'formación'],
            'belleza': ['belleza', 'cosmética', 'maquillaje', 'skincare'],
            'cocina': ['cocina', 'recetas', 'gastronomía', 'chef'],
            'viajes': ['viajes', 'turismo', 'destinos', 'aventura'],
            'finanzas': ['finanzas', 'dinero', 'inversión', 'ahorro']
        }
        
        for nicho, keywords in nicho_keywords.items():
            if any(keyword in message_lower for keyword in keywords):
                params['nicho'] = nicho
                break
        
        # Detectar objetivo
        if 'awareness' in message_lower or 'conocimiento' in message_lower:
            params['objetivo'] = 'awareness'
        elif 'leadgen' in message_lower or 'leads' in message_lower or 'generar leads' in message_lower:
            params['objetivo'] = 'leadgen'
        elif 'venta' in message_lower or 'vender' in message_lower:
            params['objetivo'] = 'venta'
        
        # Detectar plataforma
        if 'tiktok' in message_lower:
            params['plataforma'] = 'tiktok'
        elif 'shorts' in message_lower or 'youtube shorts' in message_lower:
            params['plataforma'] = 'shorts'
        elif 'youtube' in message_lower:
            params['plataforma'] = 'youtube'
        elif 'podcast' in message_lower:
            params['plataforma'] = 'podcast'
        
        # Detectar duración
        duration_pattern = r'\b(30|45|60|90)\s*(seg|segundos|s)?\b'
        duration_match = re.search(duration_pattern, message_lower)
        if duration_match:
            params['duracion'] = int(duration_match.group(1))
        
        # Detectar tono
        if 'amigable' in message_lower or 'friendly' in message_lower:
            params['tono'] = 'amigable'
        elif 'humor' in message_lower or 'gracioso' in message_lower:
            params['tono'] = 'humor'
        elif 'profesional' in message_lower:
            params['tono'] = 'profesional'
        
        # Extraer tema del contexto general
        # Remover email y parámetros específicos para obtener el tema
        clean_message = re.sub(email_pattern, '', message)
        
        # Remover palabras clave específicas pero preservar el contexto
        keywords_to_remove = [
            r'\b(awareness|leadgen|venta|autoridad)\b',
            r'\b(reels|tiktok|shorts|youtube|podcast)\b',
            r'\b(30|45|60|90)\s*(seg|segundos|s)?\b',
            r'\b(directo|amigable|humor|profesional)\b',
            r'\b(email|correo|tema|plataforma|duración|duracion|tono|objetivo)\s*:?\s*',
            r'\b(necesito|quiero|busco|deseo)\s+un?\s+(guión|guion|script|contenido)\b',
            r'\b(sobre|acerca de|relacionado con)\b',
            r'\b(hola|mi|es|para|y|quiero|generar)\b',
            r'[^\w\s]'  # Remover caracteres especiales
        ]
        
        for pattern in keywords_to_remove:
            clean_message = re.sub(pattern, ' ', clean_message, flags=re.IGNORECASE)
        
        # Limpiar espacios extra
        clean_message = re.sub(r'\s+', ' ', clean_message).strip()
        
        if clean_message and len(clean_message) > 5:
            params['tema'] = clean_message
            params['contexto'] = clean_message
        
        return params
    
    def generate_script_with_ai(self, params):
        """Genera el guión completo usando DeepSeek AI"""
        
        prompt = f"""
Eres ScriptCoach, un asistente experto en crear guiones listos para grabar contenido de redes sociales.

PARÁMETROS DEL CLIENTE:
- Email: {params['email']}
- Tema: {params['tema'] or 'Contenido de valor general'}
- Nicho: {params.get('nicho', 'marca personal')}
- Objetivo: {params['objetivo']}
- Plataforma: {params['plataforma']}
- Duración: {params['duracion']} segundos
- Tono: {params['tono']}
- Contexto: {params['contexto']}

GENERA UN JSON COMPLETO con esta estructura exacta:

{{
  "meta": {{
    "plataforma": "{params['plataforma']}",
    "duracion_seg": {params['duracion']},
    "objetivo": "{params['objetivo']}",
    "nicho": "{params.get('nicho', 'marca personal')}",
    "idioma": "es-AR",
    "email_destino": "{params['email']}"
  }},
  "guion": [
    {{"seccion": "HOOK", "tiempo_est": "0-3s", "texto": "Hook impactante que capture atención inmediata"}},
    {{"seccion": "CONTEXTO", "tiempo_est": "3-8s", "texto": "Contexto breve del tema"}},
    {{"seccion": "VALOR", "tiempo_est": "8-40s", "texto": "Contenido de valor principal con puntos clave"}},
    {{"seccion": "PRUEBA/RESALTE", "tiempo_est": "40-55s", "texto": "Prueba social, ejemplo o dato impactante"}},
    {{"seccion": "CTA", "tiempo_est": "55-60s", "texto": "Call to action claro y específico"}}
  ],
  "hooks_alternativos": ["Hook alternativo 1", "Hook alternativo 2", "Hook alternativo 3"],
  "ctas_alternativas": ["CTA alternativa 1", "CTA alternativa 2"],
  "broll": [
    {{"momento": "0-3s", "descripcion": "B-roll para el hook"}},
    {{"momento": "8-20s", "descripcion": "B-roll para el contenido principal"}}
  ],
  "overlays": [
    {{"momento": "0-3s", "texto": "Texto overlay para hook"}},
    {{"momento": "50-60s", "texto": "Texto overlay para CTA"}}
  ],
  "copy_publicacion": {{
    "titulo": "Título atractivo para la publicación",
    "descripcion": "Descripción que invite a ver el video completo",
    "hashtags": ["#hashtag1", "#hashtag2", "#hashtag3"]
  }},
  "miniatura": {{
    "pose": "Pose sugerida para la miniatura",
    "texto_grande": "Texto principal para la miniatura"
  }},
  "variantes_extra": [
    {{"duracion_seg": 30, "nota": "versión corta", "cambios_clave": ["Eliminar sección de contexto", "Condensar valor en 15s"]}},
    {{"duracion_seg": 90, "nota": "versión extendida", "cambios_clave": ["Agregar más ejemplos", "Incluir story personal"]}}
  ],
  "lista_tomas": [
    {{"plano": "Primer plano", "encuadre": "Centrado", "locacion": "Fondo simple", "luz": "Luz frontal suave", "nota": "Para hook y CTA"}}
  ],
  "checklist_pre_grabacion": [
    "luz frontal suave",
    "micrófono cerca",
    "modo avión",
    "fondo simple",
    "ensayo del hook x3"
  ],
  "ideas_ab_test": {{
    "hooks": ["Hook A", "Hook B"],
    "cta": ["CTA A", "CTA B"],
    "miniatura": ["Miniatura A", "Miniatura B"]
  }}
}}

REGLAS IMPORTANTES:
1. El tono debe ser {params['tono']}
2. Duración exacta: {params['duracion']} segundos
3. Plataforma: {params['plataforma']}
4. Objetivo: {params['objetivo']}
5. Frases cortas y directas
6. Indicar cortes con [CORTA A:] y [INSERT B-ROLL:]
7. Contenido grabable con celular
8. Cero relleno, solo valor

Responde SOLO con el JSON válido, sin texto adicional.
"""

        try:
            if self.client is None:
                raise Exception("No AI client available")
                
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "Eres ScriptCoach, experto en crear guiones para redes sociales. Responde solo con JSON válido."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            content = response.choices[0].message.content.strip()
            
            # Limpiar el JSON si viene con markdown
            if content.startswith('```json'):
                content = content[7:]
            if content.endswith('```'):
                content = content[:-3]
            
            # Validar que el JSON sea válido
            parsed_json = json.loads(content)
            
            # Verificar que tenga la estructura básica requerida
            required_fields = ['meta', 'guion', 'hooks_alternativos', 'ctas_alternativas']
            if not all(field in parsed_json for field in required_fields):
                raise Exception("AI response missing required fields")
                
            return parsed_json
            
        except Exception as e:
            print(f"Error generating script with AI: {str(e)}")
            # No usar fallback, lanzar error para que se maneje arriba
            raise Exception("La IA no pudo generar el guión en este momento")
    
    def generate_fallback_json(self, params):
        """Genera un JSON de respaldo si falla la IA"""
        
        # Generar contenido específico basado en los parámetros
        tema = params.get('tema', 'contenido de valor')
        objetivo = params.get('objetivo', 'autoridad')
        plataforma = params.get('plataforma', 'reels')
        duracion = params.get('duracion', 60)
        tono = params.get('tono', 'directo')
        
        # Ajustar tiempos según duración
        if duracion == 30:
            tiempos = ["0-2s", "2-5s", "5-25s", "25-28s", "28-30s"]
        elif duracion == 45:
            tiempos = ["0-3s", "3-7s", "7-35s", "35-42s", "42-45s"]
        elif duracion == 90:
            tiempos = ["0-5s", "5-12s", "12-70s", "70-82s", "82-90s"]
        else:  # 60s
            tiempos = ["0-3s", "3-8s", "8-40s", "40-55s", "55-60s"]
        
        # Generar hooks según objetivo
        if objetivo == 'leadgen':
            hooks = [
                f"¿Quieres saber cómo {tema.lower()}?",
                f"El secreto de {tema.lower()} que nadie te cuenta...",
                f"3 errores que cometes en {tema.lower()}"
            ]
            cta_principal = "Descarga mi guía gratis en bio"
            cta_alt = "Comenta 'QUIERO' y te envío el PDF"
        elif objetivo == 'venta':
            hooks = [
                f"¿Estás listo para transformar tu {tema.lower()}?",
                f"Esto es lo que cambió mi {tema.lower()} para siempre...",
                f"El método que uso para {tema.lower()}"
            ]
            cta_principal = "Agenda tu consulta gratuita"
            cta_alt = "Envíame DM para más info"
        elif objetivo == 'awareness':
            hooks = [
                f"¿Sabías que {tema.lower()} puede cambiar todo?",
                f"La verdad sobre {tema.lower()} que nadie dice...",
                f"Por qué {tema.lower()} es fundamental"
            ]
            cta_principal = "Sígueme para más contenido así"
            cta_alt = "Comparte si te sirvió"
        else:  # autoridad
            hooks = [
                f"Como experto en {tema.lower()}, te digo que...",
                f"Después de años en {tema.lower()}, aprendí que...",
                f"El error más común en {tema.lower()}"
            ]
            cta_principal = "¿Quieres que te ayude con esto?"
            cta_alt = "Comenta tus dudas abajo"
        
        return {
            "meta": {
                "plataforma": plataforma,
                "duracion_seg": duracion,
                "objetivo": objetivo,
                "nicho": params.get('nicho', 'marca personal'),
                "idioma": "es-AR",
                "email_destino": params['email']
            },
            "guion": [
                {"seccion": "HOOK", "tiempo_est": tiempos[0], "texto": f"{hooks[0]} [CORTA A: CONTEXTO]"},
                {"seccion": "CONTEXTO", "tiempo_est": tiempos[1], "texto": f"Hoy te voy a mostrar todo sobre {tema.lower()}..."},
                {"seccion": "VALOR", "tiempo_est": tiempos[2], "texto": f"Aquí están los 3 puntos clave sobre {tema.lower()} que necesitas saber..."},
                {"seccion": "PRUEBA/RESALTE", "tiempo_est": tiempos[3], "texto": f"Y esto es lo que pasó cuando implementé estos consejos en {tema.lower()}..."},
                {"seccion": "CTA", "tiempo_est": tiempos[4], "texto": cta_principal}
            ],
            "hooks_alternativos": hooks,
            "ctas_alternativas": [cta_principal, cta_alt],
            "broll": [
                {"momento": tiempos[0], "descripcion": f"B-roll relacionado a {tema.lower()}"},
                {"momento": tiempos[2], "descripcion": f"B-roll de apoyo al contenido sobre {tema.lower()}"}
            ],
            "overlays": [
                {"momento": tiempos[0], "texto": f"💡 {tema.upper()}"},
                {"momento": tiempos[4], "texto": "¡ACCIÓN!"}
            ],
            "copy_publicacion": {
                "titulo": f"Todo sobre {tema} que necesitas saber",
                "descripcion": f"Descubre los secretos de {tema.lower()} que nadie te cuenta...",
                "hashtags": [f"#{tema.replace(' ', '')}", "#marcapersonal", "#contenido"]
            },
            "miniatura": {
                "pose": "Expresión de sorpresa/descubrimiento",
                "texto_grande": f"{tema.upper()}"
            },
            "variantes_extra": [
                {"duracion_seg": 30, "nota": "versión corta", "cambios_clave": ["Solo hook + valor + CTA"]},
                {"duracion_seg": 90, "nota": "versión extendida", "cambios_clave": ["Más ejemplos y story personal"]}
            ],
            "lista_tomas": [
                {"plano": "Primer plano", "encuadre": "Centrado", "locacion": "Fondo simple", "luz": "Luz frontal suave", "nota": "Para todo el video"}
            ],
            "checklist_pre_grabacion": [
                "luz frontal suave",
                "micrófono cerca",
                "modo avión",
                "fondo simple",
                "ensayo del hook x3"
            ],
            "ideas_ab_test": {
                "hooks": [hooks[0], hooks[1]],
                "cta": [cta_principal, cta_alt],
                "miniatura": ["Expresión sorpresa", "Expresión confianza"]
            }
        }
    
    def generate_whatsapp_summary(self, json_data):
        """Genera el resumen para WhatsApp basado en el JSON generado"""
        
        hook = json_data['guion'][0]['texto']
        cta = json_data['guion'][-1]['texto']
        miniatura = json_data['miniatura']['texto_grande']
        
        # Obtener puntos clave del contenido de valor
        valor_text = json_data['guion'][2]['texto']
        
        summary = f"""🎬 GUION LISTO

HOOK: {hook[:50]}...

PUNTOS CLAVE:
• {valor_text[:60]}...
• {json_data['guion'][3]['texto'][:60]}...

CTA: {cta[:40]}...

MINIATURA: {miniatura}

📧 Enviando paquete completo a tu email."""
        
        return summary
    
    def process_whatsapp_message(self, message):
        """Procesa el mensaje completo y devuelve el resultado"""
        
        # Parsear el mensaje
        params = self.parse_message(message)
        
        # Validar email
        if not params['email'] or not self.validate_email(params['email']):
            return {
                'error': 'email inválido',
                'whatsapp_resumen': '❌ Email inválido. Por favor envía un email válido y tu brief.'
            }
        
        # Generar el guión con IA
        try:
            json_entregable = self.generate_script_with_ai(params)
            
            # Generar resumen para WhatsApp
            whatsapp_resumen = self.generate_whatsapp_summary(json_entregable)
            
            return {
                'json_entregable': json_entregable,
                'whatsapp_resumen': whatsapp_resumen
            }
            
        except Exception as e:
            # Si la IA falla, devolver error específico
            return {
                'error': 'ia_no_disponible',
                'whatsapp_resumen': '❌ En estos momentos no puedo responderte. La IA está temporalmente no disponible. Por favor intenta en unos minutos.'
            }
