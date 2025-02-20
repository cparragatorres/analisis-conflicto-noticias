def limpiar_json(json_data, valor_a_eliminar):
    """Elimina las claves de un JSON que tengan un valor específico."""
    return {clave: valor for clave, valor in json_data.items() if valor != valor_a_eliminar}