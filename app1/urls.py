from django.urls import path #Se crea archivo urls.py para cada app, y se llaman desde el urls.py del proyecto
from app1 import views
from app1.views import FormularioRegistroView

urlpatterns = [    
    path('', views.bienvenida, name='bienvenida'),
    path('verRegistros/', FormularioRegistroView.verRegistros, name='verRegistros'),
    path('crearRegistro/', FormularioRegistroView.crearRegistro, name='crearRegistro'),    
    path('eliminarRegistro/<int:id_persona>', FormularioRegistroView.eliminarRegistro, name='eliminarRegistro'), 
    path('editarRegistro/<int:id_persona>', FormularioRegistroView.editarRegistro, name='editarRegistro'),
]