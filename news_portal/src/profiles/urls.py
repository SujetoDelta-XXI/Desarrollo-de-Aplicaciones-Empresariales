from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/reading-history/', views.reading_history_view, name='reading_history'),
    path('profile/bookmarks/', views.bookmarks_view, name='bookmarks'),
    path('profile/bookmarks/add/<int:article_id>/', views.add_bookmark, name='add_bookmark'),
    path('profile/bookmarks/remove/<int:bookmark_id>/', views.remove_bookmark, name='remove_bookmark'),
    path('profile/subscriptions/', views.manage_subscriptions, name='manage_subscriptions'),
    path('profile/toggle-dark-mode/', views.toggle_dark_mode, name='toggle_dark_mode'),
    path('record-view/<int:article_id>/', views.record_article_view, name='record_article_view'),
]