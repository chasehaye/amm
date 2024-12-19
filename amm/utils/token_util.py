import jwt
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from user.models import User


def validate_token(request):
    token = request.headers.get('Authorization')
    if not token:
        raise AuthenticationFailed('Authentication token missing')
    # Remove the 'Bearer ' part of the token
    token = token.split(' ')[1] if token.startswith('Bearer ') else token
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token has expired')
    except jwt.InvalidTokenError:
        raise AuthenticationFailed('Invalid token')
    
def validate_admin(request):
    token = request.headers.get('Authorization')
    if not token:
        raise AuthenticationFailed('Authentication token missing')
    # Remove the 'Bearer ' part of the token
    token = token.split(' ')[1] if token.startswith('Bearer ') else token
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user_id = payload.get('id')
        if not user_id:
            raise AuthenticationFailed('User ID not found in token')
        
        user = User.objects.get(id=user_id)
        if user.is_admin:
            return user
        else:
            raise AuthenticationFailed('You do not have admin rights')

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token has expired')
    except jwt.InvalidTokenError:
        raise AuthenticationFailed('Invalid token')
    except User.DoesNotExist:
        raise AuthenticationFailed('User not found')
    
def validate_retrieve_user(request):
    token = request.headers.get('Authorization')
    if not token:
        raise AuthenticationFailed('Authentication token missing')
    # Remove the 'Bearer ' part of the token
    token = token.split(' ')[1] if token.startswith('Bearer ') else token
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user_id = payload.get('id')
        if not user_id:
            raise AuthenticationFailed('User not found in token')
        
        user = User.objects.get(id=user_id)
        return user

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token has expired')
    except jwt.InvalidTokenError:
        raise AuthenticationFailed('Invalid token')
    except User.DoesNotExist:
        raise AuthenticationFailed('User not found')