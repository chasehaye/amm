from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, PermissionView
from .views import UserAnimeRatingView, AnimeListLinkView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('admin', PermissionView.as_view()),

    # --- anime related views --- #

    # rating views
    path('<int:userId>/rate/<int:animeId>', UserAnimeRatingView.as_view()),
    #  ^ payload is score: 1-10 ^





# unfinished
    path('link/<int:arr>/<str:id>', AnimeListLinkView.as_view())
]