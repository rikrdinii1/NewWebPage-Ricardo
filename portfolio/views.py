from django.shortcuts import render, get_object_or_404
from .models import Portfolio



# Create your views here.
def render_proyects(request):
    '''funcion para retornar el template de proyectos'''
    project = Portfolio.objects.all()
    return render(request, 'projects.html', {'project':project})

def project_detail(request, project_id):
    '''Funcion para renderizar el detalle del proyecto'''
    project = get_object_or_404(Portfolio, pk = project_id)
    return render(request, 'projects_detail.html', {'project':project})
