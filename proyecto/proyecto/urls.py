"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from cabanas import views as views_cabanas
from admin_users import views as views_users
from renta import views as views_renta
from admin_cabanas import views as views_admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_cabanas.catalogo, name='Catalogo'),
    path('contacto/', views_cabanas.contacto, name='Contacto'),
    path('sobre_nosotros/', views_cabanas.sobre_nosotros, name='Sobre_Nosotros'),
    path('perfil/', views_users.perfil, name='Perfil'),
    path('error_404/', views_cabanas.error_404, name='Error_404'),
    path('editar_perfil/', views_users.editar_perfil, name='Editar_Perfil'),
    path('vista_cabana_usuario', views_cabanas.vista_cabana_usuario, name='Vista_Cabana_Usuario'),
    path('rentar_cabana', views_renta.rentar_cabana, name='Rentar_Cabana'),
    path('editar_cabana', views_admin.editar_cabana, name='Editar_Cabana'),
    path('crear_cabana', views_admin.crear_cabana, name='Crear_Cabana'),
    path('login', views_users.login, name='Login'),
    path('registro', views_users.registro, name='Registro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

