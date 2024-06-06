from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from config import settings
from core.views import house, facial, clasificacion, informes, recetas, recomendacion, home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('dashboard/', house),
    path('facial/', facial, name='facial'),
    path('clasificacion/', clasificacion),
    path('informes/', informes),
    path('recetas/', recetas),
    path('recomendacion/', recomendacion),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)