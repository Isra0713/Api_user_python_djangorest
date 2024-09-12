from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import LoginSerializer

from .serializers import TelefonoSerializer
from .models import Telefono

from .serializers import SamsungPhoneSerializer
from .models import SamsungPhone

from .serializers import XiaomiPhoneSerializer
from .models import XiaomiPhone

from .serializers import OppoPhoneSerializer
from .models import OppoPhone

from .serializers import IphonePhoneSerializer
from .models import IphonePhone

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            # Generar o recuperar el token para el usuario autenticado
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TelefonoViewSet(viewsets.ModelViewSet):
    queryset = Telefono.objects.all()
    serializer_class = TelefonoSerializer
    
# ViewSet para SamsungPhone
class SamsungPhoneViewSet(viewsets.ModelViewSet):
    queryset = SamsungPhone.objects.all()
    serializer_class = SamsungPhoneSerializer

# ViewSet para XiaomiPhone
class XiaomiPhoneViewSet(viewsets.ModelViewSet):
    queryset = XiaomiPhone.objects.all()
    serializer_class = XiaomiPhoneSerializer

# ViewSet para OppoPhone
class OppoPhoneViewSet(viewsets.ModelViewSet):
    queryset = OppoPhone.objects.all()
    serializer_class = OppoPhoneSerializer
    
class IphonePhoneViewSet(viewsets.ModelViewSet):
    queryset = IphonePhone.objects.all()
    serializer_class = IphonePhoneSerializer

# Create your views here.
