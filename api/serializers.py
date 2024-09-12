from rest_framework import serializers
from .models import Telefono
from .models import SamsungPhone
from .models import XiaomiPhone
from .models import OppoPhone
from .models import IphonePhone


class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefono
        fields = ('id', 'marca', 'precio', 'unidades_disponibles', 'imagen_perfil')
        

class SamsungPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = SamsungPhone
        fields =  ('id', 'marca', 'precio', 'unidades_disponibles', 'imagen_perfil') 
        
class XiaomiPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = XiaomiPhone
        fields = ('id', 'marca', 'precio', 'unidades_disponibles', 'imagen_perfil')  
        
class OppoPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = OppoPhone
        fields =   ('id', 'marca', 'precio', 'unidades_disponibles', 'imagen_perfil')  
        
class IphonePhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = IphonePhone
        fields =  ('id', 'marca', 'precio', 'unidades_disponibles', 'imagen_perfil')              
