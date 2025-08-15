# 📝 Ejemplos de Uso - ScriptCoach

## 🎯 Casos de Uso Reales

### 1. **Consultor de Marketing Digital**
```
Mensaje: "Hola! Mi email es juan@marketingpro.com. Necesito un guión sobre estrategias de Instagram para TikTok, 60 segundos, tono profesional. Objetivo: generar leads para mi consultoría."
```

**Resultado esperado:**
- **Hook:** "Como consultor de marketing digital, te digo que..."
- **Tema:** estrategias de Instagram
- **Objetivo:** leadgen
- **CTA:** "Agenda tu consulta gratuita"

### 2. **Coach de Fitness**
```
Mensaje: "Email: maria@fitcoach.com Tema: rutinas de 10 minutos para principiantes Plataforma: reels Duración: 45 segundos Tono: amigable Objetivo: awareness"
```

**Resultado esperado:**
- **Hook:** "¿Sabías que rutinas de 10 minutos puede cambiar todo?"
- **Tema:** rutinas de 10 minutos para principiantes
- **Objetivo:** awareness
- **CTA:** "Sígueme para más contenido así"

### 3. **Emprendedor Tech**
```
Mensaje: "Mi email es carlos@startup.com y quiero contenido sobre fundraising para startups. Plataforma: YouTube Shorts, 90 segundos, tono directo, objetivo: autoridad."
```

**Resultado esperado:**
- **Hook:** "Como experto en fundraising para startups, te digo que..."
- **Tema:** fundraising para startups
- **Objetivo:** autoridad
- **CTA:** "¿Quieres que te ayude con esto?"

## 🔧 Formatos de Entrada

### Formato Libre (Recomendado)
```
"Hola! Mi email es usuario@ejemplo.com. Necesito un guión sobre [TEMA] para [PLATAFORMA], [DURACIÓN] segundos, tono [TONO]. Quiero [OBJETIVO]."
```

### Formato Estructurado
```
Email: usuario@ejemplo.com
Tema: [tema del contenido]
Plataforma: [reels|tiktok|shorts|youtube|podcast]
Duración: [30|45|60|90] segundos
Tono: [directo|amigable|humor|profesional]
Objetivo: [awareness|leadgen|venta|autoridad]
```

### Formato Compacto
```
usuario@ejemplo.com - [tema] - [plataforma] - [duración]s - [tono] - [objetivo]
```

## 📊 Ejemplos de Salida

### JSON Completo
```json
{
  "meta": {
    "plataforma": "tiktok",
    "duracion_seg": 60,
    "objetivo": "leadgen",
    "nicho": "marca personal",
    "idioma": "es-AR",
    "email_destino": "usuario@ejemplo.com"
  },
  "guion": [
    {
      "seccion": "HOOK",
      "tiempo_est": "0-3s",
      "texto": "¿Quieres saber cómo marketing digital? [CORTA A: CONTEXTO]"
    },
    {
      "seccion": "CONTEXTO",
      "tiempo_est": "3-8s",
      "texto": "Hoy te voy a mostrar todo sobre marketing digital..."
    },
    {
      "seccion": "VALOR",
      "tiempo_est": "8-40s",
      "texto": "Aquí están los 3 puntos clave sobre marketing digital que necesitas saber..."
    },
    {
      "seccion": "PRUEBA/RESALTE",
      "tiempo_est": "40-55s",
      "texto": "Y esto es lo que pasó cuando implementé estos consejos en marketing digital..."
    },
    {
      "seccion": "CTA",
      "tiempo_est": "55-60s",
      "texto": "Descarga mi guía gratis en bio"
    }
  ],
  "hooks_alternativos": [
    "¿Quieres saber cómo marketing digital?",
    "El secreto de marketing digital que nadie te cuenta...",
    "3 errores que cometes en marketing digital"
  ],
  "ctas_alternativas": [
    "Descarga mi guía gratis en bio",
    "Comenta 'QUIERO' y te envío el PDF"
  ]
}
```

### Resumen WhatsApp
```
🎬 GUION LISTO

HOOK: ¿Quieres saber cómo marketing digital? [CORT...

PUNTOS CLAVE:
• Aquí están los 3 puntos clave sobre marketing digital...
• Y esto es lo que pasó cuando implementé estos consejos...

CTA: Descarga mi guía gratis en bio...

MINIATURA: MARKETING DIGITAL

📧 Enviando paquete completo a tu email.
```

## 🎨 Personalización por Nicho

### Para Coaches y Consultores
- **Objetivo:** autoridad + leadgen
- **Tono:** profesional + amigable
- **CTAs:** consultas gratuitas, guías descargables

### Para Creadores de Contenido
- **Objetivo:** awareness + venta
- **Tono:** amigable + humor
- **CTAs:** seguir, comentar, compartir

### Para Emprendedores
- **Objetivo:** venta + autoridad
- **Tono:** directo + profesional
- **CTAs:** agendar llamadas, descargar recursos

## 🚀 Tips para Mejores Resultados

### 1. **Sé Específico con el Tema**
❌ "marketing"
✅ "estrategias de email marketing para e-commerce"

### 2. **Define el Objetivo Claro**
❌ "quiero más seguidores"
✅ "objetivo: leadgen para mi consultoría"

### 3. **Especifica la Plataforma**
❌ "para redes sociales"
✅ "plataforma: TikTok"

### 4. **Incluye el Tono Deseado**
❌ "contenido profesional"
✅ "tono: amigable pero profesional"

### 5. **Menciona la Duración**
❌ "video corto"
✅ "60 segundos"

## 🔄 Flujo de Trabajo Recomendado

1. **Recibe mensaje de WhatsApp**
2. **Pega en ScriptCoach**
3. **Genera guión**
4. **Copia resumen para responder**
5. **Adjunta JSON por email**
6. **Guarda para seguimiento**

## 📈 Métricas de Éxito

- **Tiempo de respuesta:** < 2 minutos
- **Calidad del guión:** Estructura profesional
- **Personalización:** Adaptado al nicho
- **Completitud:** JSON + resumen listos

---

**¡ScriptCoach transforma mensajes simples en guiones profesionales! 🎬**
