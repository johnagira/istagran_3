from django.contrib import admin
from django.urls import path
from app import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app_views.home, name='home'),
    path('registro', app_views.registro, name='registro'),
    path('noticias', app_views.noticias, name='noticias'),
    path('logout', app_views.logout, name='logout'),
    path('perfil', app_views.perfil, name='perfil'),
]