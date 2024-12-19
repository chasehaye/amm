from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, NotFound, ValidationError
from django.db.models import Q
from .serializers import AnimeSerializer, StudioSerializer, GenreSerializer, AnimeAbbrvSerializer
from .models import Anime, Studio, Genre
from django.conf import settings
from amm.utils.token_util import validate_admin
from django.shortcuts import get_object_or_404

import logging

logger = logging.getLogger(__name__)


# Create your views here.
class CreateAnimeView(APIView):
    def post(self, request):
        try:
            user = validate_admin(request)
            if not user:
                return Response({'error': 'You do not have permission'}, status=status.HTTP_403_FORBIDDEN)

            serializer = AnimeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            anime = serializer.save()


            return Response({'message': 'success'})
        except ValidationError as e:
            logger.error(f'Validation failed: {e.detail}')
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)

        except AuthenticationFailed as e:
            logger.error(f'Authentication failed: {str(e)}')
            return Response({'error': str(e)}, status=401)

        except Exception as e:
            logger.error(f'Unexpected error: {str(e)}')
            return Response({'error': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class IndexAnimeView(APIView):
    def get(self, request):
            animes = Anime.objects.all().order_by('-created_at')
            serializer = AnimeSerializer(animes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
class OrderIndexAnimeView(APIView):
    def get(self, request):
        # retrieve fileds
        order_by = request.query_params.get('order_by', 'titleJpRoman')
        order = request.query_params.get('order', 'desc')

        # set and fill filter
        filters = {}
        queryset = Anime.objects.filter(**filters)

        if order == 'asc':
            queryset = queryset.order_by(order_by)
        else:
            queryset = queryset.order_by(f'-{order_by}')

        serializer = AnimeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class SearchIndexAnimeView(APIView):
    def get(self, request):
        searchQueryTitleEng = request.query_params.get('titleEnglish', None)
        searchQueryTitleJpRom = request.query_params.get('titleJpRoman', None)
        searchQueryIdPre = request.query_params.get('idPre', None)
        searchQueryIdSeq = request.query_params.get('idSeq', None)

        if not any([searchQueryTitleEng, searchQueryTitleJpRom, searchQueryIdPre, searchQueryIdSeq]):
            return Response(
                {"error": "At least one query parameter is required (searchQueryTitleEng, searchQueryTitleJpRom, searchQueryIdPre, searchQueryIdSeq)."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if searchQueryTitleEng or searchQueryTitleJpRom or searchQueryIdPre or searchQueryIdSeq:
            query = Q()
            if searchQueryTitleEng:
                query |= Q(titleEnglish__icontains=searchQueryTitleEng)
            if searchQueryTitleJpRom:
                query |= Q(titleJpRoman__icontains=searchQueryTitleJpRom)
            if searchQueryIdPre:
                query |= Q(id=searchQueryIdPre)
            if searchQueryIdSeq:
                query |= Q(id=searchQueryIdSeq)
            animes = Anime.objects.filter(query)
        else:
            animes = Anime.objects.all()

        serializer = AnimeSerializer(animes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class FindAnimeAbbrvView(APIView):
    def get(self, request, id):
        try:
            anime = Anime.objects.get(pk=id)

        except Anime.DoesNotExist:
            raise NotFound(detail="not found", code=404)
        serializer = AnimeAbbrvSerializer(anime)
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
            user = validate_admin(request)
            if not user:
                return Response({'error': 'You do not have permission'}, status=status.HTTP_403_FORBIDDEN)
            
            anime = Anime.objects.get(pk=id)
            anime.delete()

            return Response({'message': 'success'}, status=status.HTTP_200_OK)
        except Anime.DoesNotExist:
            raise NotFound(detail="not found", code=404)
        
class UpdateAnimeView(APIView):
    def put(self, request, id):
        try:
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
    

# Studio related views
    
class CreateStudioView(APIView):
    def post(self, request):
        try:
            user = validate_admin(request)
            if not user:
                return Response({'error': 'You do not have permission'}, status=status.HTTP_403_FORBIDDEN)
            
            serializer = StudioSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            studio = serializer.save()

            return Response({'message': 'success'})
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except AuthenticationFailed as e:
            return Response({'error': str(e)}, status=401)
        
class IndexStudioView(APIView):
    def get(self, request):
            studios = Studio.objects.all().order_by('name')
            serializer = StudioSerializer(studios, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
    
class DeleteStudioView(APIView):
    def delete(self, request, studio_id):
        try:
            user = validate_admin(request)
            if not user:
                return Response({'error': 'You do not have permission'}, status=status.HTTP_403_FORBIDDEN)

            studio = Studio.objects.filter(id=studio_id).first()
            if not studio:
                return Response({'error': 'Studio not found'}, status=status.HTTP_404_NOT_FOUND)
            studio.delete()

            return Response({'message': 'Studio deleted successfully'}, status=status.HTTP_200_OK)
        except AuthenticationFailed as e:
            return Response({'error': str(e)}, status=401)
        except Exception as e:
            return Response({'error': 'An unexpected error occurred: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

# Genre related views
    
class CreateGenreView(APIView):
    def post(self, request):
        try:
            user = validate_admin(request)
            if not user:
                return Response({'error': 'You do not have permisson'}, status=status.HTTP_403_FORBIDDEN)
            
            serializer = GenreSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            genre = serializer.save()

            return Response({'message': 'success'})
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except AuthenticationFailed as e:
            return Response({'error': str(e)}, status=401)
        
class IndexGenreView(APIView):
    def get(self, request):
        genres = Genre.objects.all().order_by('name')
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class DeleteGenreView(APIView):
    def delete(self, request, genre_id):
        try:
            user = validate_admin(request)
            if not user:
                return Response({'error': 'You do not have permission'}, status=status.HTTP_403_FORBIDDEN)
            
            genre = Genre.objects.get(id=genre_id)
            genre.delete()
            
            return Response({'message': 'Genre deleted successfully'}, status=status.HTTP_200_OK)
        except Genre.DoesNotExist:
            return Response({'error': 'Genre not found'}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except AuthenticationFailed as e:
            return Response({'error': str(e)}, status=401) 