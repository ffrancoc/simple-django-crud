from django.urls import path
from . import views

urlpatterns = [
    # Rutas de vistas
    path('', views.index),
    path('home/', views.home, name='home'),
    # Rutas de formularios
    path('form/post/persona', views.form_post_persona, name='form_post_persona'),
    path('form/update/persona', views.form_update_persona, name='form_update_persona'),
    path('form/delete/persona/<int:id>', views.form_delete_persona, name='form_delete_persona'),
    # Rutas de operaciones base de datos
    #path('db/create/persona', views.db_create_persona, name='db_create_persona'),
    #path('db/delete/persona', views.db_delete_persona, name='db_delete_persona'),
    #path('db/update/persona', views.db_update_persona, name='db_update_persona'),
]
