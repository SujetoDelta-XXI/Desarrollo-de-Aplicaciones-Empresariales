# Desarrollo-de-Aplicaciones-Empresariales
Repositorio de los laboratorios del curso Desarrollo de Aplicaciones Empresariales de la carrera de Diseño y Desarrollo de Software - Ciclo IV

# 📚 Users App – Gestión de Usuarios y Contenido Personalizado: 

La aplicación users es parte del proyecto de gestión de biblioteca y se encarga de:

- Registrar nuevos usuarios utilizando un modelo de usuario extendido (LibraryUser)
- Permitir el inicio y cierre de sesión
- Mostrar el perfil personalizado del usuario
- Gestionar listas de lectura personales
- Crear y visualizar reseñas de libros

## Requisitos previos:

Antes de ejecutar esta app, asegúrate de tener:

- Django instalado
- La app library correctamente configurada
- Las migraciones aplicadas
- El modelo de usuario personalizado activo:

En settings.py:
```python
AUTH_USER_MODEL = 'users.LibraryUser'

## Realizar las migraciones:

python manage.py makemigrations users
python manage.py migrate

## Ejecutar el proyecto

python manage.py runserver  #En el directorio src


### Creación de usuario recomendadado:

User: SujetoDelta@
Password: Django12345678






