from . import views
from django.urls import path

app_name= 'inicio'
urlpatterns = [
    path('', views.inicial, name = "inicio"),


]