# 1. Operaciones básicas con condicionales anidados
def operaciones(a, b, tipo):
    if tipo == "suma":
        return a + b
    else:
        if tipo == "resta":
            return a - b
        else:
            if tipo == "multi":
                return a * b
            else:
                if tipo == "divi":
                    if b != 0:
                        return a / b
                    else:
                        return "error"
                else:
                    return None


# 2. Filtrar usuarios mayores de edad
def usuarios_mayores(lista):
    resultado = []
    for i in range(len(lista)):
        u = lista[i]
        if "nombre" in u:
            if "edad" in u:
                if u["edad"] >= 18:
                    resultado.append(u["nombre"])
    return resultado


# 3. Calcular estadísticas simples
def estadisticas(nums):
    total = 0
    for n in nums:
        total = total + n
    promedio = total / len(nums)
    if promedio > 50:
        return {"promedio": promedio, "estado": "ok"}
    else:
        return {"promedio": promedio, "estado": "bajo"}


# 4. Cargar configuración con valores por defecto
def cargar_config(cfg):
    if cfg is None:
        return "sin config"
    if "timeout" in cfg:
        t = cfg["timeout"]
    else:
        t = 30
    if "reintentos" in cfg:
        r = cfg["reintentos"]
    else:
        r = 3
    return {"timeout": t, "reintentos": r}


# 5. Procesar items y duplicar valores positivos
def procesar_items(items):
    salida = []
    for i in range(len(items)):
        it = items[i]
        if "valor" in it:
            if it["valor"] > 0:
                salida.append(it["valor"] * 2)
            else:
                salida.append(0)
        else:
            salida.append(None)
    return salida
