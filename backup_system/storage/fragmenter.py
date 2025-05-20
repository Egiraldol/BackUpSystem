import os


def fragmentar_archivo(ruta: str, tamano_maximo_mb: int, carpeta_destino: str):
    tamano_maximo = tamano_maximo_mb * 1024 * 1024
    with open(ruta, "rb") as f:
        index = 0
        while True:
            data = f.read(tamano_maximo)
            if not data:
                break
            nombre_fragmento = f"{os.path.basename(ruta)}.part{index:03d}"
            ruta_fragmento = os.path.join(carpeta_destino, nombre_fragmento)
            with open(ruta_fragmento, "wb") as f_out:
                f_out.write(data)
            index += 1
