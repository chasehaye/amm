from django.urls import path, include
from .views import CreateAnimeView

urlpatterns = [
    path('create', CreateAnimeView.as_view())
]
