from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nombre', 'apellido', 'correo_electronico', 'telefono', 'imagen_perfil')
