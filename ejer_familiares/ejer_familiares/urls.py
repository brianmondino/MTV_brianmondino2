"""ejer_familiares URL Configuration

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
from django.urls import path
from ejer_familiares.view import saludo, template1_test, template2_test, temp3_entrega


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('template1_test/', template1_test, name = 'template1_test'),
    path('template2_test/', template2_test, name = 'template2_test'),
    path('temp3_entrega/', temp3_entrega, name = 'temp3_entrega'),
]
