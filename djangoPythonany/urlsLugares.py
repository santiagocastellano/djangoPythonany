from django.contrib import admin
from django.urls import include,path
from sudapp import views
urlpatterns = [
    path('obtenerClasesDeLugares', views.obtenerClasesDeLugares),
    path('buscarLugar', views.buscarLugar),
    path('buscarLugarPorPerfil', views.buscarLugarPorPerfil),
]