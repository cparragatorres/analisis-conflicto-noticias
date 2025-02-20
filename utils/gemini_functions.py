import google.generativeai as genai
import json
from config import API_KEY
import os

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

def cargar_prompt(archivo):
    """Carga un prompt desde un archivo de texto."""
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            prompt = file.read()
        return prompt
    except Exception as e:
        print(f"Error al cargar el archivo {archivo}: {e}")
        return None

# Función para hacer la solicitud a la API de Gemini
def enviar_a_gemini(prompt, jsonFile=None):
    """Envía un prompt a la API de Gemini y devuelve la respuesta."""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')

        if jsonFile:  # Si se proporcionan datos JSON
            prompt_con_datos = f"{prompt}\nDatos JSON: {json.dumps(jsonFile)}"
            response = model.generate_content(prompt_con_datos)
        else:  # Si solo se proporciona texto
            response = model.generate_content(prompt)
        return response.text  # Devuelve el texto de la respuesta de Gemini

    except Exception as e:
        print(f"Error al enviar solicitud a Gemini: {e}")
        return None

def guardar_respuesta_en_txt(respuesta, archivo_salida):
    """Guarda la respuesta obtenida en un archivo de texto en la carpeta respuestas."""
    try:
        # Verificar si la carpeta 'respuestas' existe, si no, crearla
        if not os.path.exists("respuestas"):
            os.makedirs("respuestas")

        # Ruta completa del archivo dentro de la carpeta respuestas
        ruta_completa = os.path.join("respuestas", archivo_salida)

        # Guardar la respuesta en el archivo
        with open(ruta_completa, 'w', encoding='utf-8') as file:
            file.write(respuesta)
        print(f"Respuesta guardada en {ruta_completa}")
    except Exception as e:
        print(f"Error al guardar la respuesta en el archivo {archivo_salida}: {e}")
