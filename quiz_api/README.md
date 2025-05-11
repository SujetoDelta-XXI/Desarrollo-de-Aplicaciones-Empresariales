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

/api/profiles/ — CRUD de perfiles de usuario

/api/attempts/ — CRUD de intentos de quiz

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

Créditos

Mathias Villena — User Management System

Carlos Asparrin — Quiz Categories and Tags

Angela Lopez — Quiz Analytics System

Este proyecto es parte del laboratorio de Desarrollo de Aplicaciones Empresariales.