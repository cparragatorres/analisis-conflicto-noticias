import os
import json

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