import zipfile
from tkinter import filedialog
from encryption.aes_encryptor import generar_clave
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os


def desencriptar_archivo(ruta_encriptada: str, ruta_salida: str, password: str):
    with open(ruta_encriptada, "rb") as f:
        salt = f.read(16)
        iv = f.read(16)
        datos = f.read()

    clave = generar_clave(password, salt)
    cipher = Cipher(algorithms.AES(clave), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    datos_desencriptados = decryptor.update(datos) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    datos_final = unpadder.update(datos_desencriptados) + unpadder.finalize()

    with open(ruta_salida, "wb") as f_out:
        f_out.write(datos_final)


def descomprimir_zip(ruta_zip: str, destino: str):
    with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
        zip_ref.extractall(destino)


def restaurar_backup():
    ruta_archivo = filedialog.askopenfilename(title="Selecciona archivo de backup (.zip o .enc)")
    if not ruta_archivo:
        return

    destino = filedialog.askdirectory(title="Selecciona carpeta de restauración")
    if not destino:
        return

    if ruta_archivo.endswith(".enc"):
        password = input("Introduce la contraseña para desencriptar: ")
        ruta_zip_temporal = ruta_archivo.replace(".enc", ".zip")
        try:
            desencriptar_archivo(ruta_archivo, ruta_zip_temporal, password)
            descomprimir_zip(ruta_zip_temporal, destino)
            os.remove(ruta_zip_temporal)
        except Exception as e:
            print(f"Error al desencriptar: {str(e)}")
            return
    else:
        descomprimir_zip(ruta_archivo, destino)

    print(f"Backup restaurado correctamente en: {destino}")
