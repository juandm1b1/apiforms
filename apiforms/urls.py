"""apiforms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, logout_then_login #Para traer login y logout por defecto

from app1 import views
from app1.views import FormularioRegistroView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.bienvenida, name='bienvenida'),
#     path('registro/', FormularioRegistroView.crearRegistro, name='registro'),
#     path('formcontacto/', views.Form_contacto),
#     path('nombre/', views.nombre),
#     #path('login/', views.login, name='login'),
#     path('eliminarRegistro/<int:id_persona>', FormularioRegistroView.eliminarRegistro, name='eliminarRegistro'), 
#     path('editarRegistro/<int:id_persona>', FormularioRegistroView.editarRegistro, name='editarRegistro'),
# ]
