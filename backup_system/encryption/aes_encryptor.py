from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from base64 import urlsafe_b64encode
import os
import dask


def generar_clave(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())


@dask.delayed
def encriptar_archivo(input_path: str, output_path: str, password: str) -> None:
    salt = os.urandom(16)
    clave = generar_clave(password, salt)
    iv = os.urandom(16)
    backend = default_backend()
    cipher = Cipher(algorithms.AES(clave), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()

    with open(input_path, 'rb') as f:
        datos = f.read()
    datos_padded = padder.update(datos) + padder.finalize()
    datos_encriptados = encryptor.update(datos_padded) + encryptor.finalize()

    with open(output_path, 'wb') as f:
        f.write(salt + iv + datos_encriptados)
