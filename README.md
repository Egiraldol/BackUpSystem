# Sistema de Respaldo Seguro

Este proyecto es un sistema de respaldo seguro que permite seleccionar múltiples carpetas, comprimirlas en un archivo ZIP, encriptarlo opcionalmente con AES-256, y almacenar el backup en disco externo, en la nube (Google Drive) o fragmentarlo para dispositivos USB. También incluye restauración desde backups.

## Características principales

- Selección múltiple de carpetas (con subcarpetas)
- Compresión con ZIP (algoritmo DEFLATE)
- Encriptación AES-256 opcional
- Almacenamiento en disco externo, Google Drive, o fragmentación para USB
- Paralelismo con Dask para acelerar compresión y encriptación
- Interfaz de línea de comandos (CLI) sencilla e intuitiva

## Requisitos

- Python 3.8+
- Paquetes listados en `requirements.txt`
- Acceso a Google Drive configurado (para subida en la nube)

## Instalación

1. Clona el repositorio:

   ```bash
   git clone <URL-del-repositorio>
   cd backup_system
   ```

2. Crea y activa un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

3. Instala dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

Ejecuta el programa con:

    ```bash
    python backup_system/main.py
    ```

Sigue el menú para crear backups, encriptar, copiar a disco externo, subir a Google Drive, fragmentar o restaurar backups.

## Configuración para Google Drive

Para subir a Google Drive, configura las credenciales en el archivo client_secrets.json y sigue las instrucciones del módulo storage.cloud_upload.

## Estructura del proyecto

backup_system/
├── main.py
├── core/
├── encryption/
├── storage/
├── restore/
├── requirements.txt
├── .gitignore
├── README.md
└── client_secrets.json
