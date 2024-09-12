from rest_framework import viewsets

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
