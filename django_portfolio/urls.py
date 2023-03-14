"""django_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

# Importamos nuevas librerias
from django.conf.urls.static import static
from django.conf import settings

# importamos en donde se encuentran las nuevas ligas a utilizar
from main import views
from portfolio.views import render_proyects2

urlpatterns = [
    path("admin/", admin.site.urls),
    # Agregamos los patrones de las ligas que hemos creado
    path('', views.home, name='home'), #con el nombre es como colocarle un ID a la liga
    path('projects/', include('portfolio.urls')), # con esta ruta renderizamos los proyectos
    path('projects2/', render_proyects2, name='projects2')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)