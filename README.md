# ANALISADOR DE CONFLICTOS

Este proyecto está diseñado para realizar un análisis de conflictos o movimientos sociales a partir de información extraída mediante scraping de diversas fuentes de noticias. El análisis categoriza la información en las siguientes áreas clave:

- descripcion_conflicto
- causas
- actores_involucrados
- fechas_importantes
- zona_region
- impacto
- soluciones_propuestas

El objetivo es transformar la información raspada en un formato JSON, estructurado de manera que facilite la comprensión profunda de los conflictos sociales presentes en las noticias. Este análisis tiene como propósito ayudar a identificar patrones recurrentes, generar soluciones proactivas y utilizar la inteligencia artificial para mejorar la toma de decisiones relacionadas con los conflictos sociales.

## Requisitos del Proyecto

### Lo que necesitas:
1. **Python 3.x** (preferiblemente Python 3.7 o superior)
2. **Un archivo `scraped_texts.json`** con el siguiente formato:
   ```json
   {
      "linkdeejemplo": "Contenido scrappeado de la url"
   }
   ```
    Este archivo contiene las URL escrapeadas junto con el contenido  correspondiente.

3. **Requisitos del Proyecto**

    Un entorno virtual para evitar conflictos de dependencias y gestionar las bibliotecas necesarias para ejecutar el proyecto.

## Instrucciones para configurar y ejecutar el proyecto

1. Clona el repositorio

    Primero, clona el repositorio a tu máquina local:
    ```bash
    git clone https://github.com/cparragatorres/analisis-conflicto-noticias.git
    cd tu-repositorio
    ```
2. Crear un entorno virtual

    Para crear un entorno virtual, usa venv:

    ```bash
    python -m venv venv
    ```
3. Activar el entorno virtual

    En Windows:
    ```bash
    venv\Scripts\activate
    ```
    En macOS/Linux:
    ```bash
    source venv/bin/activate
    ```
4. Instalar los requisitos

    Una vez que el entorno virtual esté activado, instala las dependencias necesarias usando pip:

    ```bash
    pip install -r requirements.txt
    ```
5. Configuración del archivo scraped_texts.json

    Crea un archivo llamado scraped_texts.json en la raíz del proyecto y asegúrate de que tenga el siguiente formato

    ```json
    {
      "linkdeejemplo": "Contenido scrappeado de la url"
    }
    ```
    Este archivo será utilizado por el código para procesar el contenido de las URLs.

6. Ejecutar el código

    Una vez configurado todo, abrir `analisis_conflictos.ipynb` y darle al botón de **`Run All`**

    Al final se generará un archivo llamado `join_respuestas_gemini.json` donde estará el análisis de conflicto realizado por Gemini IA y estructurado en un diccionario.

## Estructura del Proyecto

```bash
/analisis_de_conflictos
    /venv                   # Entorno virtual
    /prompts                # Prompts estructurados
    /utils                  # Funciones
      /functionss.py        # Funciones generales
      /gemini_functions.py  # Funciones usando gemini
    .gitignore              # Carpetas y archivos ignorados
    analisis_conflictos.ipynb   # Código Principal a ejecutar
    config.py               # API_KEY (ignorado en .gitignore)
    join_respuestas_gemini.json # Resultado del Codigo Principal
    README.md               # Este archivo
    requirements.txt        # Archivo de dependencias
    scraped_texts.json      # Archivo JSON con las URLs y su contenido
```

#

📌 Desarrollado con ❤️ por cparragatorres