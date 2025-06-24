from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('afiliacion/', views.afiliacion, name='afiliacion'),
    path('servicios/', views.servicios, name='servicios'),
    path('beneficios/', views.beneficios, name='beneficios'),
    path('noticias/', views.noticias, name='noticias'),
    path('contacto/', views.contacto, name='contacto'),
]
