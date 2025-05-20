import os
from typing import List


def listar_archivos_recursivamente(directorio: str) -> List[str]:
    archivos = []
    for ruta_actual, _, archivos_en_ruta in os.walk(directorio):
        for archivo in archivos_en_ruta:
            ruta_completa = os.path.join(ruta_actual, archivo)
            archivos.append(ruta_completa)
    return archivos


def obtener_todos_los_archivos(directorios: List[str]) -> List[str]:
    todos_los_archivos = []
    for directorio in directorios:
        archivos = listar_archivos_recursivamente(directorio)
        todos_los_archivos.extend(archivos)
    return todos_los_archivos
