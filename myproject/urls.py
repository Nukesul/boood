from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

# Простое представление для корневого пути
def home(request):
    return HttpResponse("Добро пожаловать в Boodai Pizza API! Используйте /api/ для доступа к endpoints.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', home),  # Добавляем маршрут для корневого URL
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)