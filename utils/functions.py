import os
import json
import re

def limpiar_json(json_data, valor_a_eliminar):
    """Elimina las claves de un JSON que tengan un valor específico."""
    return {clave: valor for clave, valor in json_data.items() if valor != valor_a_eliminar}

def fragmentar_json(json_data, claves_por_fragmento=30):
    """Fragmenta un JSON en fragmentos más pequeños de tamaño específico."""
    # Fragmentar el JSON en listas de claves por el tamaño especificado
    fragmentos = [dict(list(json_data.items())[i:i+claves_por_fragmento]) for i in range(0, len(json_data), claves_por_fragmento)]
    return fragmentos

def guardar_fragmentos(fragmentos, carpeta_destino="jsons"):
    """Guarda cada fragmento en un archivo JSON en la carpeta especificada."""
    # Verificar si la carpeta 'jsons' existe, si no, crearla
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Guardar cada fragmento como un archivo JSON
    for i, fragmento in enumerate(fragmentos, start=1):
        nombre_archivo = os.path.join(carpeta_destino, f"conflicto{i}.json")
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as file:
                json.dump(fragmento, file, indent=4)
            print(f"Fragmento {i} guardado en {nombre_archivo}")
        except Exception as e:
            print(f"Error al guardar el fragmento {i}: {e}")

def extraer_json_de_txt(archivo_txt):
    try:
        # Leer el contenido del archivo
        with open(archivo_txt, "r", encoding="utf-8") as file:
            contenido = file.read()

        # Buscar JSON dentro de delimitadores ```json ... ```
        match = re.search(r"```json\n(.*?)\n```", contenido, re.DOTALL)

        if match:
            json_str = match.group(1)  # Extraer solo la parte JSON
            try:
                return json.loads(json_str)  # Convertir a diccionario JSON
            except json.JSONDecodeError as e:
                print(f"Error al decodificar JSON en {archivo_txt}: {e}")
                return None
        else:
            print(f"No se encontró JSON en {archivo_txt}")
            return None
    except Exception as e:
        print(f"Error al leer el archivo {archivo_txt}: {e}")
        return None

def unir_jsons(carpeta_jsons, archivo_salida):
    json_completo = {}

    # Obtener la lista de archivos JSON en la carpeta
    archivos_json = sorted([f for f in os.listdir(carpeta_jsons) if f.endswith(".json")])

    # Leer cada archivo JSON y combinarlo en un solo diccionario
    for archivo in archivos_json:
        ruta_json = os.path.join(carpeta_jsons, archivo)

        try:
            with open(ruta_json, "r", encoding="utf-8") as file:
                datos = json.load(file)
                json_completo.update(datos)  # Agregar datos al JSON combinado

        except json.JSONDecodeError as e:
            print(f"Error al procesar {archivo}: {e}")
        except Exception as e:
            print(f"Error al leer {archivo}: {e}")

    # Guardar el JSON consolidado
    try:
        with open(archivo_salida, "w", encoding="utf-8") as file:
            json.dump(json_completo, file, indent=4, ensure_ascii=False)
        print(f"JSON consolidado guardado en {archivo_salida}")
    except Exception as e:
        print(f"Error al guardar {archivo_salida}: {e}")