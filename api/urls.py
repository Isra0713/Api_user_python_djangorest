from django.urls import path, include
from rest_framework import routers
from api import views  # Importa el módulo views completo
from api.views import SamsungPhoneViewSet, XiaomiPhoneViewSet, OppoPhoneViewSet, IphonePhoneViewSet  # Importa las vistas

# Crea el router para registrar las rutas
router = routers.DefaultRouter()
router.register(r'telefono', views.TelefonoViewSet)  # Registro para los teléfonos
router.register(r'samsung', SamsungPhoneViewSet)  # Registro para los Samsung
router.register(r'xiaomi', XiaomiPhoneViewSet)  # Registro para los Xiaomi
router.register(r'oppo', OppoPhoneViewSet)  # Registro para los Oppo
router.register(r'iphone', IphonePhoneViewSet)  # Registro para los iphone

# Define las URLs y conecta el router
urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas del router
]
