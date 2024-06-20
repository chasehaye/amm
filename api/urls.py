from django.urls import path, include
from .views import MediaView

urlpatterns = [
    path('view/', MediaView.as_view()),
]
