superuser problem solved: https://stackoverflow.com/questions/32532900/not-able-to-create-super-user-with-django-manage-py

1. cuando se inicia, se coloca: django-admin startproject [nombre_proyecto]
2. para crear los proyectos se hace con el comando: python manage.py startapp [nombre]
cada que se agrega un modelo, se ingresa cn el siguiente comando
3. hay que crear el archivo "db.sqlite3"
4. hay que agregar los modelos, por lo que ingresamos al archivo "settings" en la carpeta [nombre_proyecto] y en la seccion INSTALLED_APPS ponemos los nombres correspondientes
5. python manage.py makemigrations
6. python manage.py migrate 

# Pendientes

agregar: Escuelas para poder controlarlo desde el Admin/
Modificar: cambiar el comportamiento para que la seccion de portafolio se muestre como la de blog. 

# Para agregar nuevas secciones
python manage.py startapp [nombre_de_la_app]