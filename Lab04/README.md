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



# 📚 Library App – Gestión de Libros, Autores y Publicaciones

La aplicación `library` es el núcleo del sistema de gestión de biblioteca y tiene como objetivo principal manejar toda la información relacionada con libros, autores, editoriales, categorías y vistas de libros. Forma parte integral del proyecto de desarrollo de aplicaciones empresariales orientado a bibliotecas.

---

## 🧩 Modelos y Relaciones

La app implementa múltiples tipos de relaciones disponibles en Django:

### 🔹 One-to-Many (ForeignKey)
- Un **autor** puede escribir varios **libros**.
- Una **categoría** puede estar asociada a muchos **libros**.

### 🔹 One-to-One (OneToOneField)
- Cada **autor** tiene un perfil único a través del modelo `AuthorProfile`.

### 🔹 Many-to-Many (ManyToManyField)
- Un **libro** puede pertenecer a múltiples **categorías**.

### 🔹 Many-to-Many con tabla intermedia
- La relación entre **libro** y **editorial** se maneja con una tabla intermedia llamada `Publication`, que también guarda campos como país y fecha de publicación.

---

## 🛠️ Requisitos previos

Antes de usar esta app, asegúrate de tener:

- Python 
- Django instalado
- Proyecto Django inicializado
- La app `users` configurada y activa (para estadísticas de vistas)
- Base de datos configurada

---

python manage.py makemigrations library
python manage.py migrate

#Ejecutar proyecto
python manage.py runserver

#Att: Angeela-Lopeez


