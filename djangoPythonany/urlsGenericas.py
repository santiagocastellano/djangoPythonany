from django.contrib import admin
from django.urls import include,path
from sudapp import views
urlpatterns = [
    path('todaslasregiones', views.todasLasRegiones),
    path('obtenerSMPPorPuerta', views.obtenerSMPPorPuerta),
    path('convertirCoordenadas', views.convertirCoordenadas),
]