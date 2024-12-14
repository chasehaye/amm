# All Backend APi calls
    User Resftul
    path('register', RegisterView.as_view()),
    payload -- name email password

    path('login', LoginView.as_view()),
    paylaod -- email password

    path('user', UserView.as_view()),
    payload -- none

    path('logout', LogoutView.as_view()),
    payload -- none

    path('admin', PermissionView.as_view()),
    payload -- none

    Anime restful
    path('create', CreateAnimeView.as_view()),
    payload -- list of anime data

    path('index', IndexAnimeView.as_view()),
    paylaod -- none

    path('<int:id>', FindAnimeView.as_view()),
    payload -- none

    path('<int:id>/delete', DeleteAnimeView.as_view()),
    payload -- none

    path('<int:id>/update', UpdateAnimeView.as_view()),
    payload -- list of anime data

    Rating based views
    path('<int:userId>/rate/<int:animeId>', UserAnimeRatingView.as_view()),
    payload -- score: 1-10

# still need to add a call to retrieve user rating
# reviews for each anime seperate model?




# unfinished
    path('link/<int:arr>/<str:id>', AnimeListLinkView.as_view())
# navigate to run:
python manage.py runserver
npm run start
.\djangoenv\Scripts\activate
djangoenv\Scripts\deactivate.bat
8000 for production build and api
5173 for react development




# User Model {plans}

img?
user
email
password
background color
favorites
/media link rating from user
/friends link


##### WORK ON MEDIA MDOEL FIRST #########
# Anime Model {plans}

img?
Type:{tv, movie, etc}
studio
premire season
air date to end date
demographic
rating
title
(
    Japaense(kanji)
    japanese(roamanized)
    english
)
genre
global rating?
rating user?
episode length
episode number
description
reviews user?
adaptaion
sequel / prequel?
status user?


Score: 8.921 (scored by 200,890 users) Ranked: #1822 based on the top anime page. Please note that 'Not yet aired' and 'R18+' titles are excluded.
Popularity: #569
Members: 404,709
Favorites: 15,094


episode and episode name?
recommended algo?

# Manga Model {plans}

img?

# Global stats api



notifications for air dates and end dates?
link format
[test](https://test.com)