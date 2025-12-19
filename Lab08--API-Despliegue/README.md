Quiz API Project
Descripción General

Este proyecto es una API de Quizzes desarrollada con Django y Django REST Framework. Permite crear quizzes, agregar preguntas y opciones, validar respuestas y gestionar usuarios con perfiles y registros de intentos. Además, incluye aplicaciones adicionales para extender la funcionalidad.

Instrucciones para Ejecutar el Proyecto
1. Clona el repositorio
git clone <URL-del-repositorio>
cd <carpeta-del-proyecto>

2. Crea y activa un entorno virtual
python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

3. Instala las dependencias
pip install -r requirements.txt

4. Aplica las migraciones
python manage.py makemigrations
python manage.py migrate

5. Crea un superusuario
python manage.py createsuperuser


Sigue las instrucciones para definir usuario, email y contraseña.

6. Ejecuta el servidor de desarrollo
python manage.py runserver

7. Accede a la API y al admin

Admin: http://127.0.0.1:8000/admin/

API Root: http://127.0.0.1:8000/api/

Estructura del Proyecto
quiz_api/
├── config/                # Configuración principal de Django
├── quizzes/               # App principal de quizzes
├── users/                 # Gestión de usuarios y perfiles
├── media/                 # Archivos subidos (avatares)
├── requirements.txt       # Dependencias
└── README.md

Endpoints Principales

/api/quizzes/ — CRUD de quizzes

/api/questions/ — CRUD de preguntas

/api/choices/ — CRUD de opciones

/api/quizzes/<id>/validate/ — Validar respuestas de un quiz

Aplicaciones Adicionales
1. User Management System (Perfiles de Usuario)

Autor: Mathias Villena

Permite crear y gestionar perfiles de usuario, incluyendo biografía y avatar. Cada usuario puede tener un perfil único y registrar sus intentos de quiz.

Modelo Profile:

user (relación uno a uno con User)

bio (biografía)

avatar (imagen de perfil)

created_at (fecha de creación)

Modelo QuizAttempt:

user (usuario que intentó el quiz)

quiz (quiz realizado)

score (puntaje obtenido)

max_score (puntaje máximo)

completed_at (fecha de intento)
Endpoint general:
/api/users/ 

Endpoints separados:

/api/users/profiles/ — Listar y crear perfiles

/api/users/attempts/ — Listar y crear intentos

2. Quiz Categories and Tags

Autor: Carlos Asparrin

Permite organizar los quizzes por categorías y etiquetas para una mejor clasificación y búsqueda.

Modelo Category:

name (nombre de la categoría)

description (descripción)

Modelo Tag:

name (nombre de la etiqueta)

Relaciones:

Los quizzes pueden pertenecer a una categoría y tener múltiples etiquetas.
3. Quiz Analytics System

Autor: Angela Lopez

Permite analizar el desempeño de los quizzes y preguntas, mostrando estadísticas de intentos y tasas de éxito.

Modelo QuestionStat:

question (pregunta relacionada)

attempts (número de intentos)

correct_attempts (número de respuestas correctas)

success_rate (tasa de éxito)

Modelo QuizActivity:

quiz (quiz relacionado)

date (fecha)

views (vistas)

starts (inicios)

completions (finalizaciones)

Notas Adicionales

Para subir imágenes de perfil, asegúrate de tener configurado MEDIA_ROOT y MEDIA_URL en settings.py.

Puedes probar los endpoints usando la interfaz web de DRF, Thunder Client o Postman.

El proyecto está pensado para ser extendido fácilmente con nuevas funcionalidades.


# Proyecto de API de Quizzes con Categorías y Etiquetas

## 1. Visión General

Este proyecto consiste en una aplicación Django que expone dos APIs REST principales:

1.  **API de Quizzes (`/api/`)**: Gestionada por la aplicación `quizzes`. Permite crear, leer, actualizar y eliminar quizzes, junto con sus preguntas y opciones.
2.  **API de Categorías y Etiquetas (`/api/category_tags/`)**: Gestionada por la aplicación `category_tags`. Permite gestionar categorías y etiquetas que pueden ser asociadas a los quizzes.

Ambas APIs están diseñadas para interactuar entre sí. La API de Quizzes consume la API de Categorías y Etiquetas para:
*   Poblar opciones de selección (categorías y etiquetas) al crear/actualizar un quiz.
*   Validar que las categorías y etiquetas seleccionadas para un quiz existan.
*   Mostrar los nombres de las categorías y etiquetas asociadas a un quiz, en lugar de solo sus IDs, en las respuestas JSON.

La aplicación `category_tags` también incluye un endpoint proxy (`/api/category_tags/proxied-quizzes/`) que puede reenviar peticiones a la API de Quizzes, demostrando una forma de composición de servicios.

## 2. Características Implementadas

*   **Gestión de Quizzes**: CRUD completo para quizzes, preguntas y opciones.
*   **Gestión de Categorías**: CRUD completo para categorías.
*   **Gestión de Etiquetas**: CRUD completo para etiquetas.
*   **Integración entre APIs**:
    *   Los quizzes pueden ser asociados con una categoría y múltiples etiquetas provenientes de la API de `category_tags`.
    *   Validación de la existencia de categorías/etiquetas externas al crear/actualizar un quiz.
    *   Serializadores en la API de `quizzes` que muestran los nombres de las categorías/etiquetas (obtenidos de la API `category_tags`) en lugar de solo IDs.
    *   Formularios en la API navegable de Django REST framework para `quizzes` que cargan dinámicamente las categorías y etiquetas disponibles desde la API `category_tags`.
*   **Cliente API Interno**: Módulos cliente (`quizzes/category_tags_api_client.py` y `category_tags/quizzes_api_client.py`) para facilitar la comunicación entre las aplicaciones.
*   **Proxy API (Ejemplo)**: Un endpoint en `category_tags` que actúa como proxy para la API de `quizzes`.

## 3. Estructura del Proyecto

El proyecto se organiza principalmente en dos aplicaciones Django:

*   `quizzes/`:
    *   `models.py`: Define los modelos `Quiz`, `Question`, `Choice`. El modelo `Quiz` incluye campos `category_id_external` y `tag_ids_external` para almacenar los IDs de la API `category_tags`.
    *   `serializers.py`: Define los serializadores para los modelos de `quizzes`. `QuizSerializer` incluye lógica para interactuar con la API de `category_tags` para obtener nombres y validar IDs.
    *   `views.py`: Contiene los `ViewSet` para exponer los endpoints de la API de quizzes.
    *   `urls.py`: Define las rutas para la API de quizzes.
    *   `category_tags_api_client.py`: Cliente para realizar llamadas a la API de `category_tags`.
*   `category_tags/`:
    *   `models.py`: Define los modelos `Category` y `Tag`.
    *   `serializers.py`: Define los serializadores para `Category` y `Tag`.
    *   `views.py`: Contiene los `ViewSet` para `Category`, `Tag`, y el `ProxiedQuizViewSet`.
    *   `urls.py`: Define las rutas para la API de categorías/etiquetas.
    *   `quizzes_api_client.py`: Cliente para realizar llamadas a la API de `quizzes` (usado por el proxy).
*   `config/` (o el nombre de tu proyecto principal):
    *   `settings.py`: Configuración del proyecto, incluyendo las URLs base para las APIs internas (`QUIZZES_API_BASE_URL`, `CATEGORY_TAGS_BASE_URL`).
    *   `urls.py`: Archivo de URLs principal que enruta a las aplicaciones.

## 4. Configuración y Ejecución Local

1.  **Clonar el repositorio (si aplica):**
    ```bash
    git clone <tu-repositorio-url>
    cd <nombre-del-directorio-del-proyecto>
    ```

2.  **Crear y activar un entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows
    # venv\Scripts\activate
    # En macOS/Linux
    # source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    Asegúrate de tener un archivo `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    # Dependencias clave probables: Django, djangorestframework, requests, psycopg2-binary (si usas PostgreSQL)
    ```

4.  **Configurar la base de datos:**
    *   Asegúrate de que la configuración de `DATABASES` en `config/settings.py` sea correcta para tu entorno local (SQLite es común para desarrollo).

5.  **Aplicar migraciones:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Crear un superusuario (opcional, para acceder al Admin de Django):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Configurar variables de entorno (si es necesario):**
    *   En `config/settings.py`, las URLs base para las APIs internas están definidas:



🚀 Despliegue de Proyecto Django en Render
1. Configuración Inicial
Asegúrate de tener un proyecto Django funcionando localmente y una cuenta en Render. Genera el archivo requirements.txt con pip freeze > requirements.txt. Luego, crea un archivo Procfile en la raíz del proyecto con el contenido:
web: gunicorn config.wsgi:application
(Reemplaza config por el nombre real de tu módulo de configuración). Opcionalmente, agrega un archivo runtime.txt con la versión de Python, por ejemplo: python-3.10.12.

2. Configuración para producción
En settings.py, establece:

DEBUG = False  
ALLOWED_HOSTS = ['.onrender.com']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
Luego ejecuta: python manage.py collectstatic.

3. Subir a GitHub y crear servicio en Render
Sube el proyecto a un repositorio en GitHub. En Render, crea un nuevo Web Service, conecta tu repositorio y define:
Build Command: pip install -r requirements.txt
Start Command: gunicorn config.wsgi:application

4. Variables de entorno
En Render, en Environment > Environment Variables, agrega al menos:

DJANGO_SETTINGS_MODULE=config.settings  
SECRET_KEY=tu_clave_secreta  
DEBUG=False
Agrega otras variables necesarias para tu base de datos o API externas.

5. Migraciones y usuario admin
Desde la pestaña "Shell" del servicio en Render, ejecuta:

python manage.py migrate  
python manage.py createsuperuser

🎉 ¡Listo!


Créditos

Mathias Villena — User Management System

Carlos Asparrin — Quiz Categories and Tags

Angela Lopez — Quiz Analytics System

Este proyecto es parte del laboratorio de Desarrollo de Aplicaciones Empresariales.