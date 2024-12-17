from django.urls import path
from django.contrib import admin
from .views import RegisterView, LoginView, UserView, LogoutView, PermissionView
from .views import RateAnimeForUserView, LinkAnimeToUserListView, GetAnimeListForUserView, GetUserInfoForAnime, SetAnimeWatchNumberView

urlpatterns = [
    # user based views
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('admin', PermissionView.as_view()),
    # anime user related views
    path('<str:username>/link/anime', LinkAnimeToUserListView.as_view()),
    path('<str:username>/list/anime', GetAnimeListForUserView.as_view()),
    path('<str:username>/info/for/<int:animeId>', GetUserInfoForAnime.as_view()),
    path('<str:username>/rate/<int:animeId>', RateAnimeForUserView.as_view()),
    path('<str:username>/ep/cnt/<int:animeId>', SetAnimeWatchNumberView.as_view())

]
