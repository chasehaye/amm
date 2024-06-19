from django.urls import path
from .views import MediaView

urlpatterns = [
    path('view/', MediaView.as_view()),
]
