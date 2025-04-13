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

# 📊 Analytics App – Book View & Usage Statistics

The analytics app is part of the library management project and provides advanced data analysis features related to books, authors, and categories.

This app was developed by Mathias Villena as part of the enterprise application development lab. 💻✨

---

## 🔍 What does this app do?

It allows you to:

- Display a dashboard with book view statistics
- Show the top 5 most viewed books
- Identify the most popular authors
- Analyze the most viewed categories
- Provide a beautiful and responsive web interface with customized CSS styling

---

## 📁 Structure

The analytics app includes:

- models.py → defines BookView and analytical models
- views.py → handles business logic and data processing
- urls.py → specific routes under /analytics/
- templates/analytics/:
  - base_analytics.html
  - dashboard.html
  - book_views.html
  - author_analytics.html
  - category_analytics.html

---

## ✅ Prerequisites

Before running this app, make sure you have:

- Django properly installed
- The library app configured and populated with Book data
- Registered users via the users app
- Applied all required migrations
- The custom user model set correctly

In your settings.py:

```python
AUTH_USER_MODEL = 'users.LibraryUser'
#Att: Mathias villena
