from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
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
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise serializers.ValidationError("Credenciales incorrectas.")
        else:
            raise serializers.ValidationError("Debe incluirse 'username' y 'password'.")
        
        data['user'] = user
        return data     
