from django.shortcuts import render

# Importamos la consulta a la base de datos
from .models import Main, Portfolio

# Create your views here.
def home(request):
    '''Funcion para que nos arroje la pagina de inicio'''
    main = Main.objects.all()
    return render(request, 'home.html', {'main':main})


# Create your views here.
def render_proyects(request):
    '''funcion para retornar el template de proyectos'''
    project = Portfolio.objects.all()
    return render(request, 'projects.html', {'project':project})

def project_detail(request, project_id):
    '''Funcion para renderizar el detalle del proyecto'''
    project = get_object_or_404(Portfolio, pk = project_id)
    return render(request, 'projects_detail.html', {'project':project})

# Create your views here.
def render_proyects2(request):
    '''funcion para retornar el template de proyectos'''
    project = Portfolio.objects.all()
    return render(request, 'projects2.html', {'project':project})