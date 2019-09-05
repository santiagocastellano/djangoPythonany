from django.contrib import admin
from django.urls import include,path
from sudapp import views
urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('delimitacionesdisponibles', views.delimitacionesDisponibles),
    path('consultardelimitacion', views.consultarDelimitacion),
    path('consultardelimitaciones', views.consultarDelimitaciones),
    path('deldir', views.delDir),
    path('deldirDesamb', views.deldirDesamb),
]