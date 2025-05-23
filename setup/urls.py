from django.contrib import admin
from django.urls import path, include
from setup import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
    path('', include('users.urls')),
    path("api/", include("api.urls")),
    path('', include('frontend.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
