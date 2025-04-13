from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import ReadingList, BookReview
from .forms import ReadingListForm, BookReviewForm
from .forms import LibraryUserCreationForm 

def register(request):
    if request.method == 'POST':
        form = LibraryUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Te has registrado exitosamente! Bienvenido.')
            return redirect('profile')
        else:
            messages.error(request, 'Por favor corrige los errores indicados.')
    else:
        form = LibraryUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    reading_lists = user.reading_lists.all()
    reviews = user.reviews.all()
    return render(request, "users/profile.html", {
        "user": user,
        "reading_lists": reading_lists,
        "reviews": reviews,
    })

@login_required
def reading_list_list(request):
    reading_lists = request.user.reading_lists.all()
    return render(request, "users/reading_list_list.html", {
        "reading_lists": reading_lists
    })

@login_required
def reading_list_detail(request, pk):
    reading_list = get_object_or_404(ReadingList, pk=pk, user=request.user)
    return render(request, "users/reading_list_detail.html", {
        "reading_list": reading_list
    })

@login_required
def reading_list_create(request):
    if request.method == "POST":
        form = ReadingListForm(request.POST)
        if form.is_valid():
            reading_list = form.save(commit=False)
            reading_list.user = request.user
            reading_list.save()
            form.save_m2m()  # para guardar las relaciones many-to-many con Book
            return redirect("reading_list_detail", pk=reading_list.pk)
    else:
        form = ReadingListForm()
    return render(request, "users/reading_list_form.html", {
        "form": form
    })

@login_required
def review_list(request):
    reviews = request.user.reviews.all()
    return render(request, "users/review_list.html", {
        "reviews": reviews
    })

@login_required
def review_detail(request, pk):
    review = get_object_or_404(BookReview, pk=pk, user=request.user)
    return render(request, "users/review_detail.html", {
        "review": review
    })

@login_required
def review_create(request):
    if request.method == "POST":
        form = BookReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("review_detail", pk=review.pk)
    else:
        form = BookReviewForm()
    return render(request, "users/review_form.html", {
        "form": form
    })
