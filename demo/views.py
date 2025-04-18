from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework_simplejwt.views import TokenObtainPairView


from demo.models import User
from demo.serializers import UserSerializer, EmailTokenObtainPairSerializer


class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MeView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer