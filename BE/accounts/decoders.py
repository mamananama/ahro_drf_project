import jwt
from django.conf import settings
from rest_framework import authentication, exceptions


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get('HTTP_AUTHORICATION')
            if token is None:
                return None
            # header에서 받은 token 내용에 선행값 (ex. Bearer)이 있다면 token값이랑 분리 시켜준다.
            user, jwt_token = token.split(' ')
            print(user)
            print(jwt_token)
            # SECRET_KEY는 django의 SECRET_KEY를 사용함
            decoded = jwt.decode(token, settings.SECRET_KEY,
                                 algorithm=[settings.SIMPLE_JWT["ALGORITHM"]])
            pk = decoded.get('pk')
            return user, None
        except jwt.exceptions.DecodeError:
            raise exceptions.AuthenticationFailed('JWT Format Invalid')
