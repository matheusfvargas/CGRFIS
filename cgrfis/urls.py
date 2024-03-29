"""cgrfis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from usuarios import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from argparse import Namespace

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('itbi/', include('itbi.urls')),
    path('plantadevalores/', include(("pvi.urls","pvi"), namespace = "pvi")),
    path('registro/', user_views.registro, name = 'registro'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name = 'usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'usuarios/logout.html'), name='logout'),
    path('perfil/', user_views.perfil, name='perfil')
]