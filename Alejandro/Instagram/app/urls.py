from django.urls import path
from app import views as app_views

urlpatterns = [
    path('', app_views.home, name='home'),
    path('registro', app_views.registro, name='registro'),
    path('noticias', app_views.noticias, name='noticias'),
]