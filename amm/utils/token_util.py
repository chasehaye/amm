import jwt
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

def validate_token(token):
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token has expired')
    except jwt.InvalidTokenError:
        raise AuthenticationFailed('Invalid token')