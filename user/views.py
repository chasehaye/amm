from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
import jwt, datetime

from .serializers import UserSerializer, WatchedEpisodesSerializer
from .models import User, WatchedEpisodes


from django.shortcuts import get_object_or_404
from anime.models import Anime, Rating
from anime.serializers import AnimeSerializer

# UserViews

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        payload = {
            'id': user.id,
            'name': user.name,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.data = {
            'jwt': token,
        }

        return response
    
class LoginView(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("User not found")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")
        
        payload = {
            'id': user.id,
            'name': user.name,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.data = {
            'jwt': token
        }
    
        return response

class UserView(APIView):
    def get(self, request):
        token = request.headers.get('Authorization')
        if not token:
            # Return 200 OK with no content if token is missing
            return Response(None, status=status.HTTP_200_OK)
        
        token = token.split(' ')[1]

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.data = {
            'message': 'Successfully logged out'
        }
        return response
    
class PermissionView(APIView):
    def get(self, request):
        token = request.headers.get('Authorization')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        token = token.split(' ')[1]
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = User.objects.filter(id=payload['id']).first()
        if user.is_admin:
            return Response(True)
        else:
            return Response(False)














#User Anime relation views
class LinkAnimeToUserListView(APIView):
    def post(self, request, username):


        user_id = request.GET.get('user_id')
        anime_id = request.GET.get('anime_id')
        list_type = request.GET.get('list_type')

        if not user_id or not anime_id or not list_type:
            return Response({"message": "Missing required parameters."}, status=400)

        user = get_object_or_404(User, id=user_id)
        anime = get_object_or_404(Anime, id=anime_id)

        user.currently_watching.remove(anime)
        user.completed.remove(anime)
        user.plan_to_watch.remove(anime)
        user.dropped.remove(anime)
        user.interested_in.remove(anime)
        user.on_hold.remove(anime)

        if list_type == '1':
            user.currently_watching.add(anime)
        elif list_type == '2':
            user.completed.add(anime)
        elif list_type == '3':
            user.plan_to_watch.add(anime)
        elif list_type == '4':
            user.dropped.add(anime)
        elif list_type == '5':
            user.interested_in.add(anime)
        elif list_type == '6':
            user.on_hold.add(anime)
        elif list_type == '7':
            pass
        else:
            return Response({"message": "Invalid list type provided."}, status=400)
        return Response({
            "message": f"success"
        })
    
class GetAnimeListForUserView(APIView):
    def get(self, request, username):
        user_id = request.GET.get('user_id')
        list_type = request.GET.get('list_type')

        if not user_id or not list_type:
            return Response({"message": "Missing required parameters."}, status=400)
        user = get_object_or_404(User, id=user_id)
        if list_type == '0':
                anime_list = (
                    list(user.currently_watching.all()) +
                    list(user.completed.all()) +
                    list(user.plan_to_watch.all()) +
                    list(user.dropped.all()) +
                    list(user.interested_in.all()) +
                    list(user.on_hold.all())
                )
        elif list_type == '1':
            anime_list = user.currently_watching.all()
        elif list_type == '2':
            anime_list = user.completed.all()
        elif list_type == '3':
            anime_list = user.plan_to_watch.all()
        elif list_type == '4':
            anime_list = user.dropped.all()
        elif list_type == '5':
            anime_list = user.interested_in.all()
        elif list_type == '6':
            anime_list = user.on_hold.all()
        else:
            return Response({"message": "Invalid list type provided."}, status=400)
        
        serializer = AnimeSerializer(anime_list, many=True)
        return Response(serializer.data, status=200)
    
class RateAnimeForUserView(APIView):
    def post(self, request, username, animeId):
        anime = get_object_or_404(Anime, id=animeId)

        score = request.GET.get('score')
        userId = request.GET.get('userId')

        if userId is None:
            return Response({"error": "User Id is required."}, status=400)
        user = get_object_or_404(User, id=userId)
        if score is None:
            return Response({"error": "Score is required."}, status=400)
        try:
            score = int(score)
            if score < 1 or score > 10:
                raise ValueError
        except ValueError:
            return Response({"error": "Score must be an integer between 1 and 10."}, status=400)


        rating = Rating.objects.filter(user=user, anime=anime).first()
        if rating:  # If rating exists, update it
            rating.score = score  # Update the user's score
            rating.save()  # Save the updated rating
        else:  # If no rating exists, create a new one
            Rating.objects.create(user=user, anime=anime, score=score)

        return Response({"rating": f"{score}"})

class SetAnimeWatchNumberView(APIView):
    def post(self, request, username, animeId):

        anime = get_object_or_404(Anime, id=animeId)
        watchedEpisodeCount = request.GET.get('watchedEpisodeCount')
        userId = request.GET.get('userId')
        user = get_object_or_404(User, id=userId)

        if userId is None:
            return Response({"error": "User Id is required."}, status=400)
        
        try:
            watchedEpisodeCount = int(watchedEpisodeCount)
        except ValueError:
            return Response({"error": "watchedEpisodeCount must be a valid integer"}, status=400)
        watched_instance, created = WatchedEpisodes.objects.get_or_create(user=user, anime=anime)
        watched_instance.episodes_watched = watchedEpisodeCount
        watched_instance.save()

        
        return Response({"episodeCount": watched_instance.episodes_watched}, status=201 if created else 200)

        

    # finsih so it sets episode count when either created or updated
    # silently handle all inputs if it is NAN return an error
    # save the creation



class GetUserInfoForAnime(APIView):
    def get(self, request, username, animeId):
        anime = get_object_or_404(Anime, id=animeId)
        userId = request.GET.get('userId')

        if userId is None:
            return Response({"error": "User Id is required."}, status=400)
        user = get_object_or_404(User, id=userId)



        rating = Rating.objects.filter(user=user, anime=anime).first()

        watched_episode = WatchedEpisodes.objects.filter(user=user, anime=anime).first()
        watched_episode_count = watched_episode.episodes_watched if watched_episode else None

        list_name = None
        if anime in user.currently_watching.all():
            list_name = "Currently Watching"
        elif anime in user.completed.all():
            list_name = "Completed"
        elif anime in user.plan_to_watch.all():
            list_name = "Plan To Watch"
        elif anime in user.dropped.all():
            list_name = "Dropped"
        elif anime in user.interested_in.all():
            list_name = "Interested In"
        elif anime in user.on_hold.all():
            list_name = "On Hold"

        response_data = {
            "rating": rating.score if rating else None,
            "list": list_name,
            "episodeCount": watched_episode_count
        }

        return Response(response_data)