from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnimeSerializer
from .models import Anime
import jwt
from django.conf import settings
from datetime import datetime, timedelta
from amm.utils.token_util import validate_token
from rest_framework.exceptions import AuthenticationFailed

# Create your views here.

class CreateAnimeView(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Authentication token missing')
        try:
            payload = validate_token(token)
            serializer = AnimeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            anime = serializer.save()
            # Use payload as needed
            return Response({'message': 'success'})
        except AuthenticationFailed as e:
            return Response({'error': str(e)}, status=401)