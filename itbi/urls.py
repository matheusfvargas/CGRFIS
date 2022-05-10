from . import views
from django.urls import path

app_name = 'itbi'
urlpatterns = [
    path('', views.index, name = "index"),
    path('add', views.incluir_processo, name='incluir_processo'),
    path('edit', views.listar_processo, name='listar_processo'),
    path('edit/update', views.editar_processo, name='editar_processo'),
]