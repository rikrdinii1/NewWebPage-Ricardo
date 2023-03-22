from django.urls import path

# importamos el archivo de views y las funciones para poder renderizar
from .views import render_proyects, project_detail, render_proyects2

# variable para identificar el proyecto
app_name = "blog"
urlpatterns = [
    # cuando visiten la pagina inicial rendericen los proyectos
    path("", render_proyects, name="projects"),
    path("<int:project_id>", project_detail, name="project_detail"),  # Para hacer URL dinamicas por cada proyecto
    path("projects2/", render_proyects2, name = "projects2")
]
