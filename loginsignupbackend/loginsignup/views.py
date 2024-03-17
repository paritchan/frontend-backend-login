from django.shortcuts import render

from rest_framework import viewsets
from .serializers import loginsignupSerializer
from .models import loginsignup

class loginsignupView( viewsets.ModelViewSet):
    serializer_class = loginsignupSerializer
    queryset = loginsignup.objects.all()
