# 1. Operaciones básicas
def operaciones(primer_numero, segundo_numero, tipo_operacion):
    if tipo_operacion == "suma":
        return primer_numero + segundo_numero
    if tipo_operacion == "resta":
        return primer_numero - segundo_numero
    if tipo_operacion == "multi":
        return primer_numero * segundo_numero
    if tipo_operacion == "divi":
        return (
            primer_numero / segundo_numero
            if segundo_numero != 0
            else "error"
        )
    return None


# 2. Filtrar usuarios mayores de edad
def usuarios_mayores(usuarios):
    return [
        usuario["nombre"]
        for usuario in usuarios
        if "nombre" in usuario
        and "edad" in usuario
        and usuario["edad"] >= 18
    ]


# 3. Calcular estadísticas simples
def estadisticas(numeros):
    promedio = sum(numeros) / len(numeros)
    estado = "ok" if promedio > 50 else "bajo"
    return {"promedio": promedio, "estado": estado}


# 4. Cargar configuración con valores por defecto
def cargar_config(configuracion):
    if configuracion is None:
        return "sin config"
    return {
        "timeout": configuracion.get("timeout", 30),
        "reintentos": configuracion.get("reintentos", 3),
    }


# 5. Procesar items y duplicar valores positivos
def procesar_items(items):
    return [
        None
        if "valor" not in item
        else item["valor"] * 2
        if item["valor"] > 0
        else 0
        for item in items
    ]
