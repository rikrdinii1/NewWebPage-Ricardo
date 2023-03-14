from django.db import models

# Modulos para importar los datos que estaremos guardando
from django.db.models.fields import TextField, CharField
from django.db.models.fields.files import ImageField

class Main(models.Model):
    """Clase que guarda los datos del usuario"""
    name = CharField(max_length=100)
    image = ImageField(upload_to='main/images/')
    description = TextField(blank=True)
    subtitle = CharField(max_length=300, blank=True)



