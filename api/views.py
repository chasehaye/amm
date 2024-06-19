from django.shortcuts import render
from rest_framework import generics
from .serializers import MediaSerializer
from .models import Media
# Create your views here.

class MediaView(generics.ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
