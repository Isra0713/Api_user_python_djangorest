from django.db import models

class Telefono(models.Model):
    marca = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Mejor precisión para precios
    unidades_disponibles = models.IntegerField()  # Unidades debe ser un campo numérico
    imagen_perfil = models.ImageField(upload_to='perfiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.marca} - ${self.precio}"

# Clase SamsungPhone hereda de Telefono
class SamsungPhone(Telefono):  
    tecnologia_5g = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.marca} (Samsung) - ${self.precio}"

# Clase XiaomiPhone hereda de Telefono
class XiaomiPhone(Telefono):  
    version_miui = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.marca} (Xiaomi) - ${self.precio}"

# Clase OppoPhone hereda de Telefono
class OppoPhone(Telefono):  
    carga_rapida = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.marca} (Oppo) - ${self.precio}"
    
class IphonePhone(Telefono):
    bateria = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.marca} (Oppo) - ${self.precio}"

    
    
    
    
  
    
        




