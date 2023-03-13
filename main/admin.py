from django.contrib import admin

# Importamos el modulo para que pueda leer la clase creada
from .models import Main

admin.site.register(Main)