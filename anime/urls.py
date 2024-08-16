from django.urls import path
from .views import CreateAnimeView, IndexAnimeView, FindAnimeView, DeleteAnimeView, UpdateAnimeView

urlpatterns = [
    path('create', CreateAnimeView.as_view()),
    path('index', IndexAnimeView.as_view()),
    path('<int:id>', FindAnimeView.as_view()),
    path('<int:id>/delete', DeleteAnimeView.as_view()),
    path('<int:id>/update', UpdateAnimeView.as_view()),
]
