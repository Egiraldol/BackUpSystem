import os
from zipfile import ZipFile, ZIP_DEFLATED
import dask
from typing import List


@dask.delayed
def agregar_a_zip(ruta_archivo: str, ruta_base: str) -> tuple:
    with open(ruta_archivo, "rb") as f:
        data = f.read()
    ruta_relativa = os.path.relpath(ruta_archivo, ruta_base)
    return ruta_relativa, data


def comprimir_archivos_en_zip(archivos: List[str], carpeta_base: str, nombre_salida: str) -> None:
    tareas = [agregar_a_zip(archivo, carpeta_base) for archivo in archivos]
    resultados = dask.compute(*tareas)

    with ZipFile(nombre_salida, "w", compression=ZIP_DEFLATED) as zipf:
        for ruta_relativa, data in resultados:
            zipf.writestr(ruta_relativa, data)
