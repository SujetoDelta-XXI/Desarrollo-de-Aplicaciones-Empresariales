from django.contrib import admin
from .models import Author, AuthorProfile, Category, Publisher, Book, Publication

class AuthorProfileInline(admin.StackedInline):
    model = AuthorProfile
    can_delete = False

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name',)
    inlines = [AuthorProfileInline]

class PublicationInline(admin.TabularInline):
    model = Publication
    extra = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'publication_date')
    list_filter = ('categories', 'author')
    search_fields = ('title', 'author__name', 'isbn')
    inlines = [PublicationInline]
    filter_horizontal = ('categories',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    search_fields = ('name',)

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('book', 'publisher', 'country', 'date_published')
    list_filter = ('publisher', 'country')
    search_fields = ('book__title', 'publisher__name', 'country')
