from django.urls import path
from .views import MonitoreoListCreate

urlpatterns = [
    path('monitoreo/', MonitoreoListCreate.as_view(), name='monitoreo-list-create'),
  
]
