from rest_framework import routers
from .api import EventoViewSet, UbicacionViewSet, RegistroViewSet

router = routers.DefaultRouter()
router.register('eventos', EventoViewSet, basename='eventos')
router.register('ubicaciones', UbicacionViewSet, basename='ubicaciones')
router.register('registros', RegistroViewSet, basename='registros')

urlpatterns = router.urls