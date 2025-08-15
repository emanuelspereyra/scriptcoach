from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from dotenv import load_dotenv
from script_processor import ScriptProcessor

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configurar la API key de DeepSeek
DEEPSEEK_API_KEY = "sk-ee5c7c3f1674411b89ae50b657489c43"
os.environ["OPENAI_API_KEY"] = DEEPSEEK_API_KEY
os.environ["OPENAI_API_BASE"] = "https://api.deepseek.com/v1"

script_processor = ScriptProcessor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/process-message', methods=['POST'])
def process_message():
    try:
        data = request.get_json()
        message = data.get('message', '')
        
        if not message:
            return jsonify({
                'error': 'Mensaje requerido',
                'whatsapp_resumen': 'Por favor envía un mensaje con tu email y brief.'
            }), 400
        
        result = script_processor.process_whatsapp_message(message)
        return jsonify(result)
        
    except Exception as e:
        print(f"Error processing message: {str(e)}")
        return jsonify({
            'error': 'Error interno del servidor',
            'whatsapp_resumen': 'Hubo un error procesando tu mensaje. Intenta de nuevo.'
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
