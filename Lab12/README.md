# SeriesApp - (Django + React)

SeriesApp: es una aplicación web full-stack diseñada para la gestión de series y categorías. El backend ha sido desarrollado con Django REST Framework, mientras que el frontend utilizaReact 19 + Vite. El diseño visual está incorporando una interfaz limpia, moderna y completamente responsive.

---------------------------------------------------------------------------------------------------------------

## 🔐 Credenciales de Acceso

- Usuario: admin@tecsup.edu.pe
- Contraseña: 123456

Estas credenciales te permiten acceder al sistema como administrador para gestionar series y categorías.

---------------------------------------------------------------------------------------------------------------

## Tecnologías Utilizadas

- Backend: Django 5.2, Django REST Framework, SQLite (base de datos local)
- Frontend: React 19, Vite, Bootstrap 5, Bootstrap Icons

---------------------------------------------------------------------------------------------------------------

## Funcionalidades

- Autenticación protegida por login
- CRUD completo de categorías (crear, editar, eliminar y listar)
- CRUD completo de series con relación a sus categorías
- Diseño visual moderno y adaptativo (responsive)
- Consumo de API REST en tiempo real desde React
- Separación clara entre frontend y backend

---------------------------------------------------------------------------------------------------------------

## Instrucciones de Instalación y Ejecución

### 1. Backend (Django)

cd cinepoli-API
python manage.py runserver


### 2. Frontend (React + Vite)

react
react-dom
react-router-dom
vite (si es Vite)
axios (para consumir APIs)

cd seriesapp-frontend
npm install
npm run dev

### 3. Despliegue (Render):

## API:

django - Framework backend principal
djangorestframework	- Para crear APIs REST en Django
django-cors-headers	- Para permitir solicitudes del frontend (CORS)
psycopg2-binary	- Conector de Django con PostgreSQL
dj-database-url	- Para leer DATABASE_URL desde Render
gunicorn - Servidor WSGI para producción (usado en Render)
whitenoise - Sirve archivos estáticos en producción (CSS, JS, etc.)

------------------------
La API se expondrá en: [https://cinepoli-api.onrender.com/api/]

El frontend estará disponible en: [https://desarrollo-de-aplicaciones-empresariales.onrender.com]

---------------------------------------------------------------------------------------------------------------

## 🌐 Rutas del Proyecto en local:

- Frontend: http://localhost:5173/
- API (Django): http://localhost:8000/api/
- Login protegido: mediante las credenciales proporcionadas

---

## 👨‍🎓 Proyecto Académico

Este proyecto fue desarrollado como parte de la formación académica en TECSUP – 2025, en el curso de desarrollo web full-stack, integrando las tecnologías más demandadas de la industria actual.

Autores del Proyecto:
- Carlos A. Asparrin  
- Ángela J. López  
- Mathias J. Villena