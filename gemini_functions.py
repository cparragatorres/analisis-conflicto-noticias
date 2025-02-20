import google.generativeai as genai
import json
from config import API_KEY

# Configura la API de Gemini utilizando la clave de API desde config.py
def configurar_api():
    """Configura la API de Gemini con la clave proporcionada desde config.py."""
    try:
        genai.configure(api_key=API_KEY)
        print("API de Gemini configurada correctamente.")
    except Exception as e:
        print(f"Error al configurar la API de Gemini: {e}")

# Función para leer el archivo JSON
def read_json_file(filename):
    """Leer un archivo JSON y devolver su contenido."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error al leer el archivo JSON: {e}")
        return None

# Función para hacer la solicitud a la API de Gemini
def enviar_a_gemini(prompt):
    """Envía un prompt a la API de Gemini y devuelve la respuesta."""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash') #Utiliza GenerativeModel
        response = model.generate_content(prompt) #Utiliza generate_content
        return response.text  # Devuelve el texto de la respuesta de Gemini

    except Exception as e:
        print(f"Error al enviar solicitud a Gemini: {e}")
        return None

# Función para procesar la respuesta de Gemini
def process_gemini_response(response):
    """Procesar la respuesta de Gemini y extraer el resultado."""
    if response and 'response' in response:
        return response['response'].get('result', None)
    else:
        print("Respuesta de Gemini no contiene los datos esperados.")
    return None

# Función para guardar el resultado procesado en un archivo JSON
def save_json_file(data, filename):
    """Guardar los datos procesados en un archivo JSON."""
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Archivo guardado como {filename}")
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")
