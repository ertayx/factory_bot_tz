from rest_framework import generics, response, permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt import views
from drf_yasg import openapi
from . import serializers


class RegistrationView(generics.GenericAPIView):

    serializer_class = serializers.RegisterSerializer

    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(serializer.data, status=201)
    

class LoginView(views.TokenObtainPairView):
    permission_classes = (permissions.AllowAny, )


class LogoutView(generics.GenericAPIView):
    serializer_class = serializers.RefreshTokenSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args):
        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return response.Response(status=204)
    
        
class TokenUpdateView(generics.GenericAPIView):
    serializer_class = serializers.TokenSerializer
    permission_classes = (permissions.IsAuthenticated, )

    @swagger_auto_schema(
        operation_description="generate new telegram token"
    )
    def put(self, request, *args, **kwargs):
        user = request.user
        user.generate_telegram_token()
        user.save()
        return response.Response('успешно обновлено')
    
    
    def get(self, request):
        return response.Response(request.user.telegram_token)
        