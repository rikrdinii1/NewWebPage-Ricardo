from django.db import models

# Modulos para importar los datos que estaremos guardando
from django.db.models.fields import TextField, CharField, URLField
from django.db.models.fields.files import ImageField

from ckeditor.fields import RichTextField

class Main(models.Model):
    """Clase que guarda los datos del usuario"""

    name = CharField(max_length=100)
    image = ImageField(upload_to="main/images/")
    subtitle = CharField(max_length=300, blank=False)
    description = RichTextField(blank=True)
    

class Portfolio(models.Model):
    """Clase con el modelo de datos para el portafolio"""

    title = TextField(max_length=100)
    subtitle = TextField(max_length=300, blank=True)
    main_image = ImageField(upload_to="main/images/")
    second_image = ImageField(upload_to="main/images/", blank=True)
    third_image = ImageField(upload_to="main/images/", blank=True)

    description = RichTextField()
    url = URLField(blank=True)

class Document(models.Model):
    pdf = models.FileField(upload_to='portfolio/')


