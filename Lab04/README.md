# Business Application Development
Repository for the laboratory work of the Business Application Development course in the Software Design and Development program - Cycle IV

# 📚 Users App – User and Custom Content Management:

The Users app is part of the library management project and is responsible for:

-Registering new users using an extended user model (LibraryUser)
-Allowing users to log in and log out
-Displaying the user's customized profile
-Managing personal reading lists
-Creating and viewing book reviews

## Prerequisites:

Before running this app, make sure you have:

-Django installed
-The library app correctly configured
-Migrations applied
-The custom user model activated:

In settings.py:
```python
AUTH_USER_MODEL = 'users.LibraryUser'

## Run migrations:

python manage.py makemigrations users
python manage.py migrate

## Run the project:

python manage.py runserver  #In the src directory


### Recommended user creation:

User: SujetoDelta@
Password: Django12345678

------------------------------------------------------------------------

# 📚 Library App – Book, Author, and Publication Management

The library app is the core of the library management system and its primary goal is to manage all information related to books, authors, publishers, categories, and book views. It is an integral part of the Business Application Development project aimed at libraries.

---

## 🧩 Models and Relationships

The app implements multiple types of relationships available in Django:

-One-to-Many (ForeignKey)
-An author can write multiple books.

-A category can be associated with many books.

- One-to-One (OneToOneField)
-Each author has a unique profile through the AuthorProfile model.

- Many-to-Many (ManyToManyField)
-A book can belong to multiple categories.

- Many-to-Many with intermediate table
The relationship between book and publisher is managed with an intermediate table called Publication, which also stores fields like country and publication date.

---

## 🛠️ Prerequisites

Before using this app, ensure you have:

-Python
-Django installed
-Django project initialized
-The users app configured and active (for view statistics)
-Database configured

---

python manage.py makemigrations library
python manage.py migrate

#Ejecutar proyecto
python manage.py runserver

#Att: Angeela-Lopeez


