from django.urls import path
from .views import CreateAnimeView, IndexAnimeView, FindAnimeView, DeleteAnimeView, UpdateAnimeView, SearchIndexAnimeView, FindAnimeAbbrvView
from .views import CreateStudioView, IndexStudioView, DeleteStudioView, CreateGenreView, IndexGenreView, DeleteGenreView

urlpatterns = [
    # Anime related views
    path('index/search', SearchIndexAnimeView.as_view()),
    path('create', CreateAnimeView.as_view()),
    path('index', IndexAnimeView.as_view()),
    path('<int:id>/abbrv', FindAnimeAbbrvView.as_view()),
    path('<int:id>', FindAnimeView.as_view()),
    path('<int:id>/delete', DeleteAnimeView.as_view()),
    path('<int:id>/update', UpdateAnimeView.as_view()),
    # Studio views
    path('studio/create', CreateStudioView.as_view()),
    path('studio/index', IndexStudioView.as_view()),
    path('studio/delete/<int:studio_id>', DeleteStudioView.as_view()),
    # Genre views
    path('genre/create', CreateGenreView.as_view()),
    path('genre/index', IndexGenreView.as_view()),
    path('genre/delete/<int:genre_id>', DeleteGenreView.as_view()),
]
