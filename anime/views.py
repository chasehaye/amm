from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, NotFound
from .serializers import AnimeSerializer
from .models import Anime
import jwt
from django.conf import settings
from datetime import datetime, timedelta
from amm.utils.token_util import validate_admin
# Create your views here.

class CreateAnimeView(APIView):
    def post(self, request):
        try:
            #validate admin
            user = validate_admin(request)
            if not user:
                return Response({'error': 'You do not have permission'}, status=status.HTTP_403_FORBIDDEN)
            
            serializer = AnimeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            anime = serializer.save()

            # Use payload as needed
            return Response({'message': 'success'})
        except AuthenticationFailed as e:
            return Response({'error': str(e)}, status=401)
        
class IndexAnimeView(APIView):
    def get(self, request):
            animes = Anime.objects.all()
            serializer = AnimeSerializer(animes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
class FindAnimeView(APIView):
    def get(self, request, id):
        try:
            anime = Anime.objects.get(pk=id)
        except Anime.DoesNotExist:
            raise NotFound(detail="not found", code=404)
        serializer = AnimeSerializer(anime)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class DeleteAnimeView(APIView):
    def delete(self, request, id):
        try:
            #validate admin
            user = validate_admin(request)
            if not user:
                return Response({'error': 'You do not have permission'}, status=status.HTTP_403_FORBIDDEN)
            
            anime = Anime.objects.get(pk=id)
            anime.delete()
            return Response({'message': 'deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Anime.DoesNotExist:
            raise NotFound(detail="not found", code=404)
        
class UpdateAnimeView(APIView):
    def put(self, request, id):
        try:
            #validate admin
            user = validate_admin(request)
            if not user:
                return Response({'error': 'You do not have permission'}, status=status.HTTP_403_FORBIDDEN)
            
            anime = Anime.objects.get(pk=id)
        except Anime.DoesNotExist:
            raise NotFound(detail="not found", code=404)
        serializer = AnimeSerializer(anime, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)