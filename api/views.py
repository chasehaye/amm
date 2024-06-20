from django.shortcuts import render
from rest_framework import generics
from .serializers import MediaSerializer
from .models import Media
# Create your views here.

class MediaView(generics.CreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
