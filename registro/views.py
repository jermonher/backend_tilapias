from rest_framework import generics
from .models import Monitoreo
from .serializer import MonitoreoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class MonitoreoListCreate(generics.ListCreateAPIView):
    queryset = Monitoreo.objects.all()
    serializer_class = MonitoreoSerializer
    


            