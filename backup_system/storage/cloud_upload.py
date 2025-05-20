from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


def subir_a_google_drive(ruta_archivo: str):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    nombre = ruta_archivo.split("/")[-1]
    archivo = drive.CreateFile({'title': nombre})
    archivo.SetContentFile(ruta_archivo)
    archivo.Upload()
    return archivo['title']
