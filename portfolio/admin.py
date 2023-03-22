from django.contrib import admin

# Importamos el modulo para que pueda leer la clase creada
from .models import Main, Portfolio, Document

admin.site.register(Main)
admin.site.register(Portfolio)
admin.site.register(Document)