from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Author, Book, Category, Publisher

def home(request):
    context = {
        'total_books': Book.objects.count(),
        'total_authors': Author.objects.count(),
        'total_categories': Category.objects.count(),
        'total_publishers': Publisher.objects.count(),
        'categories': Category.objects.annotate(
            book_count=Count('books')
        ).order_by('-book_count')[:5],
        'recent_books': Book.objects.select_related('author').order_by('-publication_date')[:5],
    }
    return render(request, 'library/home.html', context)

def author_list(request):
    authors = Author.objects.all().order_by('name')
    return render(request, 'library/author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.books.select_related('author').prefetch_related('categories')
    return render(request, 'library/author_detail.html', {'author': author, 'books': books})

def book_list(request):
    books = Book.objects.all().select_related('author').order_by('title')
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    categories = book.categories.all()
    publications = book.publication_set.select_related('publisher').all()
    
    context = {
        'book': book, 
        'categories': categories,
        'publications': publications
    }
    return render(request, 'library/book_detail.html', context)

def category_list(request):
    categories = Category.objects.annotate(book_count=Count('books')).order_by('name')
    return render(request, 'library/category_list.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = category.books.all().select_related('author')
    return render(request, 'library/category_detail.html', {'category': category, 'books': books})

def publisher_list(request):
    publishers = Publisher.objects.annotate(book_count=Count('book')).order_by('name')
    return render(request, 'library/publisher_list.html', {'publishers': publishers})
