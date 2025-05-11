from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("quizzes.urls")),
    path("api/category_tags/", include('category_tags.urls')),
    path("api-auth/", include("rest_framework.urls")),
    path('api/users/', include('users.urls')),
    path("api/analytics/", include("analytics.urls")), 
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)