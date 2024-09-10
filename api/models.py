from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    imagen_perfil = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
   



