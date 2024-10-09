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

#User Anime rating view
class UserAnimeRatingView(APIView):
    def post(self, request, userId, animeId):
        # Retrieve the user by userId
        user = get_object_or_404(User, id=userId)
        anime = get_object_or_404(Anime, id=animeId)
        score = request.data.get('score')
        if score is None:
            return Response({"error": "Score is required."}, status=400)
        # Validate score range (assuming a rating scale from 1 to 10)
        if not isinstance(score, int) or score < 1 or score > 10:
            return Response({"error": "Score must be an integer between 1 and 10."}, status=400)
        # Check if a rating already exists and update or create it
        rating, created = Rating.objects.update_or_create(
            user=user,
            anime=anime,
            defaults={'score': score}
        )
        if created:
            return Response({"message": f"Rating of {score} added for anime '{anime.titleEnglish}'."})
        else:
            return Response({"message": f"Rating updated to {score} for anime '{anime.titleEnglish}'."})
























#User Anime views
        
class AnimeListLinkView(APIView):
    def post (self, request, arr, id):

        user = validate_retrieve_user(request)

        list_types = {
            0: 'currently_watching',
            1: 'completed',
            2: 'plan_to_watch',
            3: 'dropped',
            4: 'interested_in',
            5: 'on_hold'
        }

        if arr not in list_types:
            return Response({"error": "Invalid list type"}, status=400)
        
        list_type = list_types[arr]
        anime = get_object_or_404(Anime, id=id)

        for lt in list_types.values():
            list_field = getattr(user, lt)
            if anime in list_field.all():
                list_field.remove(anime)

        list_field = getattr(user, list_type)
        list_field.add(anime)


        return Response({
            'message': f'Anime with ID {id} added to {list_type.replace("_", " ")} list.'
        })
    


    