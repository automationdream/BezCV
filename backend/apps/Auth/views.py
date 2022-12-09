from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site

from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from . import serializers
from .models import User

import jwt

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': _('Incorrect email or password')
    }
    def get_token(cls, user):
        if user.is_verified == False:
            raise AuthenticationFailed('Activate your account')
            
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        
        token['id'] = user.id
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['phone'] = user.phone

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class SignUpView(views.APIView):
    serializer_class = serializers.SignUpSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            token = jwt.encode({'id': user.id}, 'secret_key', algorithm='HS256')
            
            email_message = EmailMessage(
                subject='Potwierdź swoją rejestrację',
                body='Aby potwierdzić swoją rejestrację, kliknij w link: https://' + get_current_site(request).domain + '/verify?token={}'.format(token),
                to=[user.email]
            )
            email_message.send()
            
            return Response({'User created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyView(views.APIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(pk=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            payload = jwt.decode(token, settings.SECRET_KEY,  algorithms=['HS256'], options={"verify_signature": False})
            if User.objects.filter(pk=payload['user_id']).exists() == True:
                user = User.objects.get(pk=payload['user_id'])
                if user.is_verified:
                    return Response({'User is already verified'}, status=status.HTTP_400_BAD_REQUEST)
                User.objects.get(pk=payload['user_id']).delete()
            return Response({'Activation link expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(views.APIView):
    def post(self, request):
        try:
            refresh_token = request.data
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)