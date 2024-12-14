from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, PermissionView
from .views import RateAnimeForUserView, LinkAnimeToUserListView, GetAnimeListForUserView, GetUserRatingForAnime

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
    path('<str:username>/rating/for/<int:animeId>', GetUserRatingForAnime.as_view()),
    path('<str:username>/rate/<int:animeId>', RateAnimeForUserView.as_view()),








    # --- anime related views --- #

    # rating views
    #  ^ payload is score: 1-10 ^

]