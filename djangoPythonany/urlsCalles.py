
from django.contrib import admin
from django.urls import include,path
from sudapp import views
urlpatterns = [
    path('obtenerIdCuadraPorCodCalleAltura', views.obtenerIdCuadraPorCodCalleAltura),
    path('obtenerIdCuadraPor2CodigosDeCalle', views.obtenerIdCuadraPor2CodigosDeCalle),
    path('obtenerIdCuadraPorDireccion', views.obtenerIdCuadraPorDireccion),
    path('obtenerRecorridoMismaCallePorAltura', views.obtenerRecorridoMismaCallePorAltura),
    path('obtenerTodasLasCalles', views.obtenerTodasLasCalles),
    path('obtenerTramosDeCallesDentroDeRadio', views.obtenerTramosDeCallesDentroDeRadio),
    path('obtenerClasesDeLugares', views.obtenerClasesDeLugares),
]