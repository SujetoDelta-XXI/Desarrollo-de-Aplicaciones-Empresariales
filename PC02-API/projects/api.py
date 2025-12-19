from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Evento, Ubicacion, Registro
from .serializers import EventoSerializer, UbicacionSerializer, RegistroSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    @action(detail=False, methods=['get'])
    def filtrar(self, request):
        queryset = Evento.objects.all()
        fecha = request.query_params.get('fecha')
        ubicacion = request.query_params.get('ubicacion')
        precio = request.query_params.get('precio')

        if fecha:
            queryset = queryset.filter(fecha__date=fecha)
        if ubicacion:
            queryset = queryset.filter(ubicacion__nombre__icontains=ubicacion)
        if precio:
            queryset = queryset.filter(precio__lte=precio)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer

    @action(detail=True, methods=['post'])
    def confirmar_asistencia(self, request, pk=None):
        registro = get_object_or_404(Registro, pk=pk)
        registro.asistencia_confirmada = True
        registro.save()
        return Response({'mensaje': 'Asistencia confirmada'}, status=status.HTTP_200_OK)
