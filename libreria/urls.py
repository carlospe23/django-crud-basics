from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name='inicio'),
    path('about/', views.about, name='about'),
    path('libros/', views.libros, name='libros'),
    path('libros/crear', views.crear_libro, name='crear_libro'),
    path('borrar/<int:id>', views.borrar_libro, name='borrar_libro'),
    path('libro/editar/<int:id>', views.editar_libro, name='editar_libro')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)