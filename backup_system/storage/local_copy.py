import shutil
from tkinter import filedialog


def copiar_a_disco_externo(archivo_backup: str):
    destino = filedialog.askdirectory(title="Selecciona carpeta de destino (disco externo)")
    if not destino:
        return None
    nombre = archivo_backup.split("/")[-1]
    ruta_destino = f"{destino}/{nombre}"
    shutil.copy2(archivo_backup, ruta_destino)
    return ruta_destino
