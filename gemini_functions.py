# gemini_functions.py

import requests
import json

# Función para leer el archivo JSON
def read_json_file(filename):
    """Leer un archivo JSON y devolver su contenido."""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error al leer el archivo JSON: {e}")
        return None

# Función para hacer la solicitud a la API de Gemini
def send_to_gemini(input_text, api_key):
    """Enviar texto a la API de Gemini y obtener la respuesta."""
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}'
    body = {
        "contents": [
            {
                "parts": [
                    {
                        "text": input_text
                    }
                ]
            }
        ]
    }
    try:
        response = requests.post(url, json=body)
        response.raise_for_status()  # Levanta error si la solicitud falla
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"Error HTTP: {err}")
    except Exception as e:
        print(f"Error al hacer la solicitud: {e}")
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
