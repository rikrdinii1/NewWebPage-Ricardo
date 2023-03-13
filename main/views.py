from django.shortcuts import render

# Importamos la consulta a la base de datos
from .models import Main

# Create your views here.
def home(request):
    '''Funcion para que nos arroje la pagina de inicio'''
    main = Main.objects.all()
    return render(request, 'home.html', {'main':main})
