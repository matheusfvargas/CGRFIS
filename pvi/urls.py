from . import views
from pvi import apps
from django.urls import path



urlpatterns = [
    path('', views.inicio,name ='inicio'),
    path('resposta/', views.resposta, name = 'resposta'),
    path('observatorio/', views.observatorio, name = 'observatorio'),
    path('resposta/excel/', views.excel, name= 'excel'),
    ]