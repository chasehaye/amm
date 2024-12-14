from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

from .serializers import UserSerializer
from .models import User


from django.shortcuts import get_object_or_404
from anime.models import Anime, Rating
from anime.serializers import AnimeSerializer
from amm.utils.token_util import validate_retrieve_user

# UserViews

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        payload = {
            'id': user.id,
            'name': user.name,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
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
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
    
        return response

class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
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
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
    
class PermissionView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
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

class GetUserRatingForAnime(APIView):
    def get(self, request, username, animeId):
        anime = get_object_or_404(Anime, id=animeId)
        userId = request.GET.get('userId')
        if userId is None:
            return Response({"error": "User Id is required."}, status=400)
        user = get_object_or_404(User, id=userId)

        rating = Rating.objects.filter(user=user, anime=anime).first()

        if rating:
            return Response({"rating": rating.score})  # Send the user's rating
        else:
            return Response({"message": "No rating found for this anime."}, status=404)