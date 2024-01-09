from django.contrib import admin
from django.urls import path
from .views import subirblog, eliminar, editar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', subirblog, name='blogs'),  
    path('eliminar/<int:m_id>', eliminar, name='eliminar'),
    path('editar/<int:m_id>', editar, name='editar'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)