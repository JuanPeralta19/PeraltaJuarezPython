"""PreEntrega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from CarsApp.views import index, template_herencia, mostrar_vehiculos_americanos, agregar_vehiculos_americanos,buscar_vehiculo, mostrar_vehiculos_europeos,mostrar_vehiculos_japoneses
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index"),
    path('Vehiculos/Americanos', mostrar_vehiculos_americanos, name="Admin de vehiculos americanos"),
    path('Vehiculos/Americanos/Agregar', agregar_vehiculos_americanos, name="Vehiculos americanos agregados"),
    path('Vehiculos/Americanos/Buscar', buscar_vehiculo, name="Buscar vehiculo"),
    path('Vehiculos/Europeos',mostrar_vehiculos_europeos, name= "Admin de vehiculos europeos"),
    path('Vehiculos/Japoneses',mostrar_vehiculos_japoneses, name= "Admin de vehiculos japoneses"),
    
]

